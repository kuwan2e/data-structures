import json
from operator import itemgetter
class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items) - 1]
    def size(self):
        return len(self.items)
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def delete(self):
        self.items = []
class BTreeNode(object):
    def __init__(self):
        self.Lnext = None
        self.Rnext = None
        self.w = 0
        self.key = ""
        self.dict = {}
        self.data = (self.key,self.w)
def hfmInit(InitJsonFile):
    wjson = open(InitJsonFile)
    wtext = json.load(wjson)
    wtext = sorted(wtext.items(), key=itemgetter(1), reverse=True)
    wStack = Stack()
    wStack.items = wtext
    for i in range(len(wtext)-1):

        '''head = BTreeNode()
        LTnode = BTreeNode()
        RTnode = BTreeNode()
        T = BTreeNode()
        rt = wStack.pop()
        lt = wStack.pop()
        LTnode.key = lt[0]
        LTnode.w = lt[1]
        LTnode.data = (lt[0],lt[1])
        RTnode.key = rt[0]
        RTnode.w = rt[1]
        RTnode.data = (rt[0].rt[1])'''
        wStack.items = sorted(wStack.items,key=itemgetter(1),reverse=True)
        head = BTreeNode()
        T = BTreeNode()
        lt = wStack.pop()
        rt = wStack.pop()
        T.Lnext = lt
        T.Rnext = rt
        #print(type(rt))
        if(type(rt[0]) == BTreeNode):
            #print("shijiedian")
            Tdict = {}
            Tdict.update(rt[0].dict)
            for key in Tdict.keys():
                Tdict[key] = str(Tdict[key] + "1")
            T.dict.update(Tdict)
        if(type(lt[0]) == BTreeNode):
            Tdict = {}
            Tdict.update(lt[0].dict)
            for key in Tdict.keys():
                Tdict[key] = str(Tdict[key] + "0")
            T.dict.update(Tdict)
        if (type(rt[0]) != BTreeNode):
            T.dict[rt[0]] = "1"
        if (type(lt[0]) != BTreeNode):
            T.dict[lt[0]] = "0"
        print(lt,end=" ")
        print(rt,end=" ")
        print(T.dict,end="\n\n\n")
        wStack.push((T,rt[1] + lt[1]))
        head = T
    for key in head.dict:
        head.dict[key] = strback(head.dict[key])
    #head.dict = dict(sorted(head.dict.items(),key=itemgetter(0),reverse=False))
    f = open('hfmTree.json', 'w')
    f.write(str(json.dumps(head.dict,indent=4)))
    f.close()
    return head
def hfmEncoding(hfmanTreeFile,ToBeTranFile):
    initjson = open(hfmanTreeFile)
    init = json.load(initjson)
    with open(ToBeTranFile) as f:
        strr = ""
        tobe = list(f.read())
        print(tobe)
        for t in tobe:
            if (t != '\n'):
                strr += init[t]
        print(strr)
        cf = open('CodeFile.txt', 'w')
        cf.write(strr)
        cf.close()
def decode(astr,hfmTreedict):
    for key in hfmTreedict.keys():
        if (astr == hfmTreedict[key]):
            return key
    return 0
def hfmDecoding(hfmanTreeFile,CodeFile):
    initjson = open(hfmanTreeFile)
    init = json.load(initjson)
    with open(CodeFile) as de:
        dec = list(de.read())
        decostr = ""
        decolist = []
        # print(dec)
        for e in dec:
            decostr += e
            if (decode(decostr, init) != 0):
                decolist.append(decode(decostr, init))
                decostr = ""
        print("".join(decolist))
#def outputHFMTree(headNode):
def strback(anstr):
    strlist = list(anstr)
    strStack = Stack()
    while(strlist != []):
        strStack.push(strlist.pop())
    return "".join(strStack.items)
#def hfmDecoding()
InitJsonFile = "Init.json"
h = hfmInit(InitJsonFile)
hfmTreeFile = "hfmTree.json"
ToBeTranFile = "ToBeTran.txt"
CodeFile = "CodeFile.txt"
hfmEncoding(hfmTreeFile,ToBeTranFile)
hfmDecoding(hfmTreeFile,CodeFile)
'''print(h.Lnext)
print(h.Rnext[0].Lnext[0].Rnext)
print(h.Rnext[0].Rnext)
print(h.dict)'''
#if(type(wtext[0]) == tuple):
 #   print(1)
