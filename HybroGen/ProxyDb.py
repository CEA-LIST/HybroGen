#!/usr/bin/env python3

import psycopg2
from psycopg2 import ProgrammingError
# from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE
import json
import datetime
import sys
import getpass

class ProxyDb:
    dbSchema = {
        "insertiondate":{
        	"archname":  		("TEXT", "primary key"),
                "insertiondate":  	("TIMESTAMP",),
        	},
        "insns":{
                "name":      		("TEXT", "not null"),
                "vectorlen":		("INT",  "not null"),
                "wordlen":   		("INT",  "not null"),
                "extension": 		("TEXT", "not null"),
                "semname":   		("TEXT", "not null"),
                "arith":     		("TEXT", "not null"),
                "parameters":     	("TEXT",),
                "operand":     	        ("TEXT",),
                "archname":  		("TEXT", "not null" , "references insertiondate(archname)"),
                "macroname": 		("TEXT","primary key" ),
                "encoding":  		("TEXT",),
      		},
         "instructionlen":{
        	"archname":  		("TEXT", "references insertiondate(archname)"),
                "insnlen":  		("INT",),
        	},
        "register":{
        	"archname":  		("TEXT", "references insertiondate(archname)"),
                "extension":  		("TEXT", "not null"),
                "number":  		("INT",  "not null"),
                "name":  		("TEXT",  "not null"),
                "arith":  		("TEXT", "not null"),
                "width":  		("INT",  "not null"),
                "function":  		("TEXT", "not null"),
        	},
         }

    indexlist = {
        "register": ("archname", "extension", "name", "arith", "function"),
    }

    def __init__ (self, host, dbname, user, passwd, debug=False):
        self.queryDebug = debug
        self.c = psycopg2.connect("host=%s dbname=%s user=%s password=%s"%(host, dbname, user, passwd))
        self.dbCursor = self.c.cursor()
        for i in self.dbSchema:
            query = self.createTable(i)
            self.execQueries((query,))
        self.schemaInsertInsn = self.buildSchemaInsertIntoInsns("insns")
        self.columnList = []
        for columnName in self.dbSchema["insns"]:
            self.columnList.append(columnName)
        for ind in self.indexlist:
            lcol = []
            for c in self.indexlist[ind]:
                lcol.append(c)
        query= 'create unique index if not exists %s_index on %s(%s);'%(ind, ind, ", ".join(lcol))
        self.execQueries((query,))

    def traceQuery (self, listQuery):
        if not self.queryDebug:
            return
        if isinstance(listQuery, tuple):
            print ("Query list (%d): %s"%(len (listQuery), str(listQuery)))
        elif isinstance(listQuery, str):
            print ("Simple query: %s"%str(listQuery))

    def buildSchemaInsertIntoInsns(self, tableName):
        typesList = []
        nameList = []
        for l in self.dbSchema[tableName]:
            columnName = l
            columnType = self.dbSchema[tableName][l][0]
            nameList.append(columnName)
            if columnType in ("INT"):
                typesList.append("%d")
            elif columnType in ("TIMESTAMP", "TEXT"):
                typesList.append("'%s'")
            else:
                raise Exception("Unknown datatype '%s'"%columnType)
        return 'insert into %s (%s) values (%s)  ;'%(tableName, ', '.join(nameList), ", ".join(typesList))

    def __exit__ (self):
        print('Db deconnection')
        self.dbCursor.close()
        self.c.close()

    def createTable(self, tablename):
        """Create Table in the table base if not exists    """
        columnsNameAndType = []
        for a in self.dbSchema[tablename]:
            attribut = a
            for p in self.dbSchema[tablename][a]:
                attribut = " ".join((attribut, p))
            columnsNameAndType.append(attribut)
        return 'CREATE TABLE IF NOT EXISTS %s (%s);\n'%(tablename, ",".join(columnsNameAndType))

    def getWordSize(self, archname):
        """Return word size list for architecture define by archname    """
        q = "select distinct insnlen from instructionlen where archname='%s';"%(archname)
        l = self.execGetQueries(q)
        return [r[0] for r in l]

    def getInsnVariant(self, archname, insnSemName):
        query = 'select distinct wordlen, arith, vectorlen from insns where archname = \'%s\' and semname=\'%s\' ;'%(archname, insnSemName)
        result = self.execGetQueries(query)
        return result

    def getInsnSemList(self, isaName):
        """Return instruction semantic list for architecture define by archname"""
        query = 'select distinct semname from Insns where archname = \'%s\' ;'%isaName
        result = self.execGetQueries(query)
        return result

    def getInsnSemantic(self, archname, extList, insnSemName, arith):
        """Return instruction list maps to instruction semantic name for architecture define by archname"""
        ext = "( extension = '" + extList[0] + "' "
        for i, e in enumerate(extList):
            if i != 0:
                ext += " or extension = '" + e + "' "
        ext +=")"
        query = 'select * from insns where archname = \'%s\' and upper(semname)=\'%s\' and arith = \'%s\' and %s order by wordlen;'%(archname, str.upper(insnSemName), arith, ext)
        self.traceQuery (query)
        result = self.execGetQueries(query)
        insnDictList = self.fromResultToDictList(result)
        return insnDictList

    def setInstruction(self, i, archname):
        """Insert or update instruction i for architecture archname.
Update if the same MacroName exists with different values for another column"""
        query = 'select * from insns where macroname = \'%s\';'%(i.getMacroName())
        result = self.execGetQueries(query)
        encoding =json.dumps(i.getBinEncoding())
        operand = json.dumps(i.getOperand())
        #Insert instruction
        if len(result) == 0 :
            req = self.schemaInsertInsn%(i.getName(), i.getVLen(), i.getWSize(), i.getExtName(), i.getSemName(), i.getArith(), i.getParameter(), operand, archname, i.getMacroName(), encoding)
            self.execQueries((req,))
        elif len(result) == 1:
            values = (i.getName(), i.getVLen(), i.getWSize(), i.getExtName(), i.getSemName(), i.getArith(), i.getParameter(), operand, archname, i.getMacroName(), encoding)
            #Update instruction
            if values != result[0]:
                req = 'update insns set name = \'%s\', extension = \'%s\', vectorlen = \'%s\', wordlen = \'%s\', semname = \'%s\', arith = \'%s\', parameters = \'%s\', operand = \'%s\', encoding = \'%s\' where  macroname = \'%s\' ;'%(i.getName(),i.getExtName(), i.getVLen(), i.getWSize(), i.getSemName(), i.getArith(), i.getParameter(), operand, encoding, i.getMacroName())
                self.execQueries((req,))

    def getInsnList(self, archName):
        """Return instruction list with all information from database for this architecture"""
        query = "select * from insns where archname = '%s' ;"%archName
        result = self.execGetQueries(query)
        columnList = []
        insnDictList = self.fromResultToDictList(result)
        return insnDictList

    def setLastInsertDate(self, archName, unixfiletime):
        """Insert into insertiondate isa file date for the architecture defined by archName """
        fileTS = datetime.datetime.utcfromtimestamp(unixfiletime).strftime('%Y-%m-%d %H:%M:%S')
        query = 'insert into InsertionDate values (\'%s\', \'%s\') on conflict (archname) do update set insertiondate=\'%s\';'%(archName, fileTS, fileTS)
        self.execQueries((query,))

    def getLastInsertDate(self, archName):
        """Return the date of the last isa file in database for the architecture defined by archName """
        query  = self.getSelectSqlReq("insertiondate", "InsertionDate", "archname", "'" + archName + "'", " order by insertiondate desc")
        result = self.execGetQueries(query)
        r = [i[0].timestamp() for i in result]
        return r

    def getSelectSqlReq(self, columnName, tableName, columnReqName, value, opt=""):
        selectPattern = 'select %s from %s where %s = %s %s;'
        query = selectPattern%(columnName, tableName, columnReqName, value, opt)
        return query

    def getInsnParameters(self, archName, semName):
        query = 'select distinct parameters from insns where archname = \'%s\' and upper(semname)=\'%s\';'%(archName, str.upper(semName),)
        result = self.execGetQueries(query)
        return result

    def setInstructionLen(self, archName, insnLen):
        """Insert into instructionlen one instruction lenght for  the architecture defined by archName """
        query = 'insert into instructionlen values (\'%s\', \'%s\');'%(archName, insnLen)
        self.execQueries((query,))

    def setRegister(self, archName, extension, number, name, width, datatype, function):
        query = 'insert into register values (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\');'%(archName, extension, number, name, datatype, width, function)
        try:
            self.execQueries((query,))
        except (psycopg2.IntegrityError, psycopg2.InternalError):
            pass

    def getRegisterList(self, archName, abi, func, arith):
        query = 'select number, name from register where archname = \'%s\' and arith = \'%s\' and extension = \'%s\' and function like \'%s%%\' order by function;'%(archName, arith, abi, str.upper(func),)
        result = self.execGetQueries(query)
        rNumber = [i[0] for i in result]
        rName = [i[1] for i in result]
        return rNumber, rName

    def execQueries(self, listQuery):
        self.traceQuery(listQuery)
        if isinstance(listQuery, tuple):
            self.dbCursor.execute("begin;")
            for q in listQuery:
                self.dbCursor.execute(q)
            self.dbCursor.execute("commit;")
        elif isinstance(listQuery, str):
            self.dbCursor.execute(listQuery)
        else:
            print("Unknown data type for query :",type(listQuery))

    def execGetQueries(self, theQuery):
        self.traceQuery (theQuery)
        try:
            self.dbCursor.execute(theQuery)
            result = self.dbCursor.fetchall()
            return result
        except Exception as e:
            print("Error with %s"%(self.dbCursor.query))
            return 0

    def fromResultToDictList(self, result):
        insnDictList = []
        for r in result:
            insnDict = {}
            i = 0
            for c in self.columnList:
                if c == "encoding":
                    insnDict[c] = json.loads(r[i])
                else:
                    insnDict[c] = r[i]
                i += 1
            insnDictList.append(insnDict)
        return insnDictList

    def dropDb(self):
        for t in self.dbSchema:
            query = 'drop table %s cascade;'%(t)
            self.execQueries((query,))

def usage(msg):
    print ("Error : %s"%msg)
    sys.exit(-1)

if __name__ == '__main__':
    import sys, os
    arglen = len(sys.argv)
    localUser = getpass.getuser()
    if arglen < 2:
        usage("Give a parameter")
