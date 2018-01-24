## Reference: Constructing Large Controlled Nots
## Link: http://algassert.com/circuits/2015/06/05/Constructing-Large-Controlled-Nots.html

## \date: 24-01-2018 - 24-01-2018
## \repo: https://gitlab.com/prince-ph0en1x/QuInE
## \proj: Quantum-accelerated Genome-sequencing

from openql import openql as ql
from random import random
from math import *
import os

def QPD():
    
    nc = [0,1,2,3,4,5,6]
    t = 7
    Q1 = 8

    config_fn = os.path.join('gateConfig.json')
    platform = ql.Platform('platform_none', config_fn)
    
    ancmax = Q1-2
    anc = Q1
    total_qubits = Q1+ancmax
    prog = ql.Program('qg', total_qubits, platform)
    gg = ql.Kernel('QCirc',platform)
    
    nCX(gg,nc,t,anc)  
    nCXb(gg,nc,t,anc)

    prog.add_kernel(gg)

    prog.compile(False, "ASAP", False)
    display()
    #showQasm(1)

def Circ4(k,Q1,anc):
    nc = []
    for sj in range(0,Q1-1):
        nc.append(sj)
    nCX(k,nc,Q1,anc)
    return

def nCXb(k,c,t,b):
    #print([c,t,b])
    nc = len(c)
    if nc == 1:
        #print(["cnot",c[0],t])
        k.gate("cnot",c[0],t)
    elif nc == 2:
        #print(["toffoli",c[0],c[1],t])
        k.toffoli(c[0],c[1],t)
    else:
        nch = ceil(nc/2)
        c1 = c[:nch]
        c2 = c[nch:]
        c2.append(b)
        #print(["-->",c[:nch],b,nch+1])
        nCXb(k,c1,b,nch+1)
        #print(["-->",c[nch:],t,nch-1])
        nCXb(k,c2,t,nch-1)
        #print(["-->",c[:nch],b,nch+1])
        nCXb(k,c1,b,nch+1)
        #print(["-->",c[nch:],t,nch-1])
        nCXb(k,c2,t,nch-1)
    return    
    



def nCX(k,c,t,anc):
    nc = len(c)
    if nc == 1:
        k.gate("cnot",c[0],t)
    elif nc == 2:
        k.toffoli(c[0],c[1],t)
    else:
        k.toffoli(c[0],c[1],anc)
        for i in range(2,nc):
            k.toffoli(c[i],anc+i-2,anc+i-1)
        k.gate("cnot",anc+nc-2,t)
        for i in range(nc-1,1,-1):
            k.toffoli(c[i],anc+i-2,anc+i-1) 
        k.toffoli(c[0],c[1],anc)
    return

def display():
    file = open("test_output/qg.qasm","a")  # Append display at end (simulator directive)
    file.write("display")
    file.close()

def showQasm(r):
    file = open("test_output/qg.qasm","r")
    print("\nCODE FILE\n\n")
    n = r
    for line in file:
        if line[0:7] == '.QCirc2':
            n = 1
        if n == 1:
            print (line,end='')
        if line[0:7] == '.QCirc3':
            n = r
    print ()
    file.close()

def randStr(szA,sz):
    # Generates a random string of length 'sz' over the alphabet of size 'szA' in decimal
    bias = 1/szA    # Improve: add bias here
    rbs = ""
    for i in range(0,sz):
        rn = random()
        for j in range(0,szA):
            if rn < (j+1)*bias:
                rbs = rbs + str(j)  # Improve: BCD version
                break
    return rbs

if __name__ == '__main__':
    QPD()