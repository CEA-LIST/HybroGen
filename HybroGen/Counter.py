#!/usr/bin/env python3

class Counter:
    """Count object using a dictionnary """
    def __init__(self):
        """Initialize the dictionnary"""
        self.data={}
        
    def __str__(self):
        """ Return a pretty printable version"""
        s = ""
        for k in self.data.keys():
            s += "%s : %s \n"%(k, self.data[k])
        return s
    def add (self, name):
        """ increment the "named" value"""
        if name in self.data.keys():
            self.data[name] = self.data[name] + 1
        else:                
            self.data[name] = 1

if __name__ == '__main__':
    a = Counter ()
    a.add ("ADD")
    a.add ("ADD")
    a.add ("ADD")
    a.add ("SUB")
    a.add ("SUB")
    a.add ("SUB")
    a.add ("MUL")
    print(a)

