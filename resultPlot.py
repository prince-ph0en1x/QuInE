## Add custom plot here
## ploty is the state vector over all qubits with LSQ as q0	

import math

'''
# qpm_a2
def customPlot(ploty):
	
	# rednPloty = [0]*(2**3)
	# addRange = len(ploty)/2**3
	# for i in range(0,2**3):
	# 	for j in range(0,addRange):
	# 		rednPloty[i] = rednPloty[i]+ploty[i+8*j]**2
	# cstmPloty = [0]*(2**3)
	# for i in range(0,2**3):
	# 	fis = format(i,'03b')[::-1]
	# 	cstmPloty[int(fis, 2)] = rednPloty[i]
	# return cstmPloty
	# return ploty
	cstmPloty = [0]*len(ploty)
	for i in range(0,len(ploty)):
		fis = format(i,'014b')[::-1]
		cstmPloty[int(fis, 2)] = ploty[i]
	return cstmPloty
'''

'''
# qpm_a2
def customPlot(ploty):
	qopt = 4
	cstmPloty = [0]*(2**qopt)
	qtot = int(math.log(len(ploty),2))
	for i in range(0,len(ploty)):
		#if ploty[i] > 0.01:
		stot = format(i,'0'+str(qtot)+'b')[::-1]
		sopt = int(stot[0:qopt],2)
		cstmPloty[sopt] = cstmPloty[sopt] + ploty[i]**2
		#print(cstmPloty)
	return cstmPloty
'''

'''
# qpm_a4
def customPlot(ploty):

	cstmPloty = [0]*len(ploty)
	for i in range(0,len(ploty)):
		fis = format(i,'010b')[::-1]
		cstmPloty[int(fis, 2)] = ploty[i]
	return cstmPloty
'''

'''
# qtm_a2
def customPlot(ploty):
	file = open("/mnt/7A06EEA206EE5E9F/GoogleDrive/TUD_CE/Thesis/SimQG/QuInE/b.txt",'w')
	cstmPloty = [0]*len(ploty)
	for i in range(0,len(ploty)):
		fis = format(i,'018b')[::-1]
		cstmPloty[int(fis, 2)] = ploty[i]**2
		if ploty[i] > 0.05:
			print(i)
			file.write(fis+","+str(ploty[i])+"\n")
	file.close()
	return cstmPloty
'''


# default
def customPlot(ploty):
	
	cstmPloty = ploty
	#for i in range(0,len(ploty)):
	#	cstmPloty[i] = ploty[i]**2
	return cstmPloty
