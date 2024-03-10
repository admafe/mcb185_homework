# 65transmembrane.py by Adele Ferrer
# Co-Author: Marle Lamountry 

for defline, seq in mcb185.read_fasta(sys.argv[1]):
	protein = list(seq)

for i in range(len(protein)):
	for j in range(protein[:30], -signallength +1):
	window = prot[j: j - signallength]
	avgKDH = #calculate hydrophobcity for each 