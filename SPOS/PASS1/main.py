from pass1 import SYMBOL_TABLE
 
with open(".output1.txt", 'r') as inp, open("output.txt", 'w+') as out:
	for line in inp:
		line = line.strip('\n').split('\t')
		IC = []
		for word in line:
			if word == '':
				continue
			if word[0] == 'S':
				idx = int(word[1:])-2
				IC.append(SYMBOL_TABLE[1][idx])
			else:
				IC.append(word)

		print(*IC, sep='\t', file = out)