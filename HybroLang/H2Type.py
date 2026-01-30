#!/usr/bin/env python3

class H2Type():
    typeCorrespondances = {
        'int' : 'i',
        'flt' : 'f',
        'uint': 'u',
        'cpl' : 'c',
        'pix' : 'p',
        'ipv4': '4',
        'ipv6': '6',
        'sint': 'i',
        'suint':'u',
        'int[]':'i',
        'flt[]':'i', # flt[] is integer arithmetic
    }

    def __init__(self, a, w, v):
        self.t = {"arith":a, "wordLen":w, "vectorLen":v}

    def __iter__(self):
        return iter(self.t)

    def __str__(self):
        return str(self.t)

    def __getitem__(self, k):
        return self.t[k]

    def getShort(self):
        return "%s-%s-%s"%(self.t["arith"], self.t["wordLen"], self.t["vectorLen"])

    def keys(self):
        return self.t
