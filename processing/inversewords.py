import pickle

import re

inFile = open("cmudict-0.7b.txt")
outFile = open("inversewords.dat", "wb")

outDict = {}

for line in inFile:
	word, phenomesRaw = line.split("  ")
	
	word = word.rstrip("()123")

	phenomes = " ".join([p.rstrip("012") for p in phenomesRaw.split()])

	if phenomes not in outDict:
		outDict[phenomes] = [word]
	else:
		outDict[phenomes].append(word)

	# print("processed", word, phenomes)

print("dumping...")

pickle.dump(outDict, outFile)

print("DONE!")