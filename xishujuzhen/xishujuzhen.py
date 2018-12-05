import numpy as np
from operator import itemgetter
class sparse_matrix(object):
    def __init__(self):
        self.data = []
        self.rpos = []
        self.mu = 0
        self.nu = 0
        self.tu = 0
        self.juzhen = [[]]
    def RLSM(self,s):
        data1 = []
        for m in s:
            data1.append(m)
        data = sorted(data1,key=itemgetter(0,1),reverse=False)
        print(data)
        self.data = data
        n = 1
        mu = 1
        nu = 1
        for i in range(1,len(data)):
            if (data[i][0] > mu):
                mu = data[i][0]
            if (data[i][1] > nu): nu = data[i][1]
            n += 1
        self.mu = mu
        self.nu = nu
        self.tu = n
        rpos = np.zeros(mu+1)
        juzhen = np.zeros((mu+1,nu+1))
        k = 0
        for d in data:
            # print(d)
            t = d[0]
            k += 1
            if (rpos[t] == 0):
                rpos[t] = k
            juzhen[d[0]][d[1]] = d[2]
        self.rpos = rpos

        self.juzhen = juzhen
    def sortdata(self):
        self.data = sorted(self.data, key=itemgetter(0, 1), reverse=False)
    def RLSMself(self):
        data = self.data
        n = 1
        mu = 1
        nu = 1
        for i in range(1, len(data)):
            if (data[i][0] > mu):
                mu = data[i][0]
            if (data[i][1] > nu): nu = data[i][1]
            n += 1
        self.mu = mu
        self.nu = nu
        self.tu = n
        rpos = np.zeros(mu + 1)
        juzhen = np.zeros((mu + 1, nu + 1))
        k = 0
        for d in data:
            # print(d)
            t = d[0]
            k += 1
            if (rpos[t] == 0):
                rpos[t] = k
            juzhen[d[0]][d[1]] = d[2]
        self.rpos = rpos
        self.juzhen = juzhen
def addSMatrix(M,N):
    Q = sparse_matrix()
    if(M.mu != N.mu or M.nu != N.nu): return "Error"
    else:
        for mdata in M.data:
            for ndata in N.data:
                if(mdata[0] == ndata[0] and mdata[1] == ndata[1]):
                    Q.data.append((mdata[0],mdata[1],mdata[2]+ndata[2]))
                    M.data.remove(mdata)
                    N.data.remove(ndata)
                    break
        for mdata in M.data:
            Q.data.append(mdata)
        for ndata in N.data:
            Q.data.append(ndata)
    return Q
def subtMatrix(M,N):
    Q = sparse_matrix()
    if (M.mu != N.mu or M.nu != N.nu):
        return "Error"
    else:
        for mdata in M.data:
            for ndata in N.data:
                if (mdata[0] == ndata[0] and mdata[1] == ndata[1]):
                    Q.data.append((mdata[0], mdata[1], mdata[2] - ndata[2]))
                    M.data.remove(mdata)
                    N.data.remove(ndata)
                    break
        for mdata in M.data:
            Q.data.append(mdata)
        for ndata in N.data:
            Q.data.append(ndata)
    return Q
#def multSMatrix(M,N):
    for row in range(1,M.tu):
        if(M.rpos[row+1] != 0):
            for i in range(M.rpos[row],M.rpos[row+1]-1):
                for j in range()
def printMatrix(Q):
    for i in range(1,Q.mu+1):
        print("|",end="")
        for j in range(1,Q.nu+1):
            print(Q.juzhen[i][j],end=" ")
        print("|")
a = ((1,1,3),(1,2,3),(2,3,4),(3,3,5),(4,6,6),(4,5,7))
b = ((1,2,4),(2,6,7),(4,2,2),(4,3,4),(4,5,5))
s = sparse_matrix()
s.RLSM(a)
A = sparse_matrix()
B = sparse_matrix()
A.RLSM(a)
print(A.juzhen)
B.RLSM(b)
Q = subtMatrix(A,B)
Q.RLSMself()
print(B.nu)
print(Q.juzhen)
printMatrix(Q)
print("tu" ,A.rpos)