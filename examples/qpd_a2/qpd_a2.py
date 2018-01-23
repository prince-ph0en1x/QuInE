## Reference: Fast quantum search algorithms in protein sequence comparison: Quantum bioinformatics - L. Hollenberg
## arXiv:


## \date: 23-01-2018 - __-02-2018
## \repo: https://gitlab.com/prince-ph0en1x/QuInE
## \proj: Quantum-accelerated Genome-sequencing


from openql import openql as ql
from random import random
from math import *
import os


def QPD():
    
    N = 11           # Reference String size
    w = "11001010001" # Reference String      #randStr(2,N)   
    #wm = ["1100","1001","0010","0101","1010","0100","1000","0001"]
    
    M = 4           # Search String size
    dummyp = "0000" # indices out of range will be tagged with dummyp data
    p = "1010"      # Search String         #randStr(2,M)   

    A = 2		# Binary Alphabet {0,1}
    Q1 = ceil(log2(A))*M	# Data Qubits
    Q2 = ceil(log2(N-M+1))	# Tag Qubits 

    config_fn = os.path.join('gateConfig.json')
    platform = ql.Platform('platform_none', config_fn)
    
    ancmax = (Q1+Q2)-1
    total_qubits = 2*Q1+Q2+ancmax
    prog = ql.Program('qg', total_qubits, platform)
    
    # Initialization
    qk1 = ql.Kernel('QCirc1',platform)
    for Qi in range(0,total_qubits):
        qk1.prepz(Qi)
    
    # Kernel 1: Construct Quantum Phone Directory
    for Qi in range(0,Q2):
        qk1.gate("h",Qi)
    nc = []
    for ci in range(0,Q2):
        nc.append(ci)
    for Qi in range(0,N-M+1):
        Qis = format(Qi,'0'+str(Q2)+'b')
        for Qisi in range(0,Q2):
            if Qis[Qisi] == '0':
                qk1.gate("x",Qisi)
        wMi = w[Qi:Qi+M]
        print([Qis,wMi])
        for wisi in range(0,M):
            if wMi[wisi] == '1':
                nCX(qk1,nc,Q2+wisi,2*Q1+Q2)
        for Qisi in range(0,Q2):
            if Qis[Qisi] == '0':
                qk1.gate("x",Qisi)

    # Kernel 2: Calculate Hamming Distance
    for Qi in range(0,M):
        if p[Qi] == '1':
            qk1.gate("x",Q1+Q2+Qi)
    for Qi in range(0,M):
        qk1.gate("cnot",Q1+Q2+Qi,Q2+Qi)

    '''
    (+0.353553,+0.000000) |00-0101-0110-000> +	2
    (+0.353553,+0.000000) |00-0101-1100-100> +	2
    (+0.353553,+0.000000) |00-0101-0001-010> +	1
    (+0.353553,+0.000000) |00-0101-1111-110> +	4
    (+0.353553,+0.000000) |00-0101-0000-001> +	0	Position 4
    (+0.353553,+0.000000) |00-0101-0111-101> +	3
    (+0.353553,+0.000000) |00-0101-0100-011> +	1  
    (+0.353553,+0.000000) |00-0101-1101-111> +	3
    '''
    
    # Oracle to Mark Hamming Distance of 0
    for Qi in range(0,M):
        qk1.gate("x",Q2+Qi) 
    qk1.gate("h",Q2)
    nc = [4,5,6]
    nCX(qk1,nc,Q2,2*Q1+Q2)
    qk1.gate("h",Q2)
    for Qi in range(0,M):
        qk1.gate("x",Q2+Qi)    
    
    # Amplitude Amplification
    qk3 = ql.Kernel('QCirc3',platform)
    Circ3(qk3,Q1,Q2)    

    prog.add_kernel(qk1)
    prog.add_kernel(qk3)
    prog.compile(False, "ASAP", False)
    display()
    #showQasm(1)


def Circ1(k,s,M):
    for Qi in range(0,(s+1)*M):
        k.prepz(Qi)
    for si in range(0,s):
        k.gate("h",si)
    for Mi in range(0,M-1):
        for si in range(0,s):
            k.gate("cnot",Mi*s+si,Mi*s+s+si)
        for si in range(0,s):
            k.gate("x",Mi*s+s-1-si)
            nc = []
            for sj in range(Mi*s+s-1,Mi*s+s-1-si-1,-1):
                nc.insert(0,sj)
            for sj in range(Mi*s+s+s-1,Mi*s+s+s-1-si-1,-1):
                nCX(k,nc,sj,s*M)        
            k.gate("x",Mi*s+s-1-si)
    
def Circ2(k,f,s,q,anc):
    for fi in range(0,len(f)):
        if f[fi]:
            fis = format(fi,'0'+str(s)+'b')
            for fisi in range(0,s):
                if fis[fisi] == '0':
                    k.gate("x",q+fisi)
            k.gate("h",q+s-1)
            nc = []
            for qsi in range(q,q+s-1):
                nc.append(qsi)
            nCX(k,nc,q+s-1,anc)
            k.gate("h",q+s-1)
            for fisi in range(0,s):
                if fis[fisi] == '0':
                    k.gate("x",q+fisi)


def Circ3(k,Q1,Q2):
    for si in range(0,Q1+Q2):
        k.gate("h",si)
        k.gate("x",si)
    k.gate("h",0)
    nc = []
    for sj in range(1,Q1+Q2):
        nc.append(sj)
    nCX(k,nc,0,2*Q1+Q2)
    k.gate("h",0)
    for si in range(0,Q1+Q2):
        k.gate("x",si)
        k.gate("h",si)
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