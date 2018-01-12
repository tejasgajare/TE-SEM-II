MNT = {}
PTAB = {}
MDT = {}


MACF = 0
with open("code") as f:
	line = []
	while True:
		line = f.readline()
		#Detect EOF
		if line == '':
			break

		line = line.strip('\n').split(' ')
		

		if line[0] == 'MACRO':
			MACF = 1
			continue

		if MACF == 1:
			MacName = line[0]
			param = []
			for i in line:
				if i[0] == '&':
					param.append(i)

			MNT[MacName] = {'#PP' : len(param), '#KP' : 0}

			PTAB[MacName] = [i.strip(',') for i in param]

			MACF = 0

			MDT[MacName] = []

			while line[0] != 'MEND':
				line = f.readline().strip('\n').split(' ')
				MDT[MacName].append(line)
			MDT[MacName].pop()

		if line[0] in MNT:
			MacName = line[0]
			param = line[1].split(',')
			
			
			for L in MDT[MacName]:
				for i in range(len(L)):
					if L[i][0] == '&' :
						
						L[i] = 'P'+str(PTAB[MacName].index(L[i]))

				print()

			IC = []


			print("\nparam = ", param)

				
print("MNT = ", MNT)
print("PTAB = ", PTAB)
print("MDT = ", MDT)