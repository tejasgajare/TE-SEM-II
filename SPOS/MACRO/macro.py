import json

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
					param.append(i.strip(','))

			MNT[MacName] = {'#PP' : len(param), '#KP' : 0}

			PTAB[MacName] = []
			PTAB[MacName].append([i.strip(',') for i in param])

			MACF = 0

			MDT[MacName] = []

			while line[0] != 'MEND':
				line = f.readline().strip('\n').split(' ')
				MDT[MacName].append(line)
			MDT[MacName].pop()

		if line[0] in MNT:
			MacName = line[0]
			param = line[1].split(',')
			PTAB[MacName].append(param)
			
			
			for L in MDT[MacName]:
				Pass1 = []
				Pass2 = []
				for i in range(len(L)):
					if L[i][0] == '&' :
						
						I = PTAB[MacName][0].index(L[i])
						Pass2.append(PTAB[MacName][1][I])
						L[i] = 'P'+str(PTAB[MacName][0].index(L[i]))
						
					else:
						Pass2.append(L[i])

					Pass1.append(L[i])
					

				print(*Pass1, sep='\t', end="")
				print("\t", *Pass2, sep='\t')

			print("\n")

			print(MDT[MacName])

			


			print("\nparam = ", param)

				
print("MNT = ", json.dumps(MNT ,sort_keys=True, indent=4))
print("PTAB = ", json.dumps(PTAB,sort_keys=True, indent=4))
print("MDT = ", json.dumps(MDT,sort_keys=True, indent=4))