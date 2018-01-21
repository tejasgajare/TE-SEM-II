from pass1 import SYMBOL_TABLE
 
with open("output.txt", 'r') as out:
	for line in out:
		line = line.strip('\n').split('\t')
		for word in line:
			if word[0] == 'S':
				