## Add custom plot here
## ploty is the state vector over all qubits with LSQ as q0	

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

# default
def customPlot(ploty):
	
	cstmPloty = ploty
	return cstmPloty