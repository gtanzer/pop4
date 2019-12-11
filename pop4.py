import sympy as sp
import numpy as np
from sys import argv
import matplotlib.pyplot as plt
from collections import Counter

def trial(k, c):
    npackets = 0
    unsolved = set([i for i in range(c)])
    clusters = [int(np.ceil(k/float(c))) for _ in range(c)]
    i = 0
    while sum(clusters) > k:
        clusters[i] -= 1
        i += 1
    rows = [np.zeros((1, clusters[i])) for i in range(c)]
    while True:
        i = np.random.randint(c)
        npackets += 1
        if i in unsolved:
            row = np.random.randint(2, size=(1, clusters[i]))
            rows[i] = np.concatenate((rows[i], row))
            if len(rows[i]) >= clusters[i]:
                _, inds = sp.Matrix(rows[i]).T.rref()
                rows[i] = rows[i][inds,:]
            if len(rows[i]) == clusters[i]:
                unsolved.remove(i)
        if len(unsolved) == 0:
            break
    return npackets

def repeatN(N, fn, args):
    ret = np.array([fn(*args) for _ in range(N)])
    return np.mean(ret), np.std(ret)

if len(argv) == 2:
    ks = [int(argv[1])]
elif len(argv) == 3:
    ks = range(int(argv[1]), int(argv[2]))
else:
    ks = [i for i in range(2,100)]

N = 25
#nfs = [lambda k: np.ceil(k / np.log2(k))]
#nfs = [lambda k: np.ceil(k / np.square(np.log2(k)))]
nfs = [lambda k: 1]
cfs = [lambda k:np.exp2(np.ceil(np.log2(k)))]

rets = []
for nf in nfs:
    for cf in cfs:
        for k in ks:
            n = int(nf(k))
            c = int(cf(n))
            print "k: ", k
            print "c: ", c
            ret = repeatN(N, trial, (k, c))
            print ret
            rets.append(ret)
print ",".join([str(ret[0]) for ret in rets])
print ",".join([str(ret[1]) for ret in rets])
            

