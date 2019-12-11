import sympy as sp
import numpy as np
from sys import argv
import matplotlib.pyplot as plt
from collections import Counter

def reconstruct(k, c):
    npackets = 0
    unsolved = set([i for i in range(c)])
    clusters = [int(np.ceil(k/float(c))) for _ in range(c)]
    i = 0
    while sum(clusters) > k:
        clusters[i] -= 1
        i += 1
    cost = sum([n*n*n for n in clusters])
    return cost

if len(argv) == 2:
    ks = [int(argv[1])]
elif len(argv) == 3:
    ks = range(int(argv[1]), int(argv[2]))
else:
    ks = [i for i in range(2,100)]

#nfs = [lambda k: np.ceil(k / np.log2(k))]
#nfs = [lambda k: np.ceil(k / np.square(np.log2(k)))]
nfs = [lambda k: k]
#nfs = [lambda k: 1]
cfs = [lambda k:np.exp2(np.ceil(np.log2(k)))]
#cfs = [lambda k: k]

rets = []
for nf in nfs:
    for cf in cfs:
        for k in ks:
            n = int(nf(k))
            c = int(cf(n))
            print "k: ", k
            print "c: ", c
            ret = reconstruct(k, c)
            print ret
            rets.append(ret)
print ",".join([str(ret) for ret in rets])
            

