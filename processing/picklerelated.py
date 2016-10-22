import pickle

from pprint import pprint

inFile = open("match.txt")
outFile = open("relatedPhenomes.dat", "wb")

outDict = {}

for line in inFile:

	base, similarRaw = line.split(": ")

	similar = similarRaw[:-1].split(" ")

	if similar == [""]: similar = []

	if base == "STOPS":
		for t in similar:
			outDict[t] = [s for s in similar if s != t]

	else:
		outDict[base] = similar

pprint(outDict)

input("ENTER to dump")

print("dumping...")

pickle.dump(outDict, outFile)

print("DONE!")