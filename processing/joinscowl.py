import pickle

fa = open("final/english-words.10")
fb = open("final/english-words.20")
fc = open("final/english-words.35")

fo = open("allwords.txt", "wb")

out = set(fa) | set(fb) | set(fc)

out = set([i.upper()[:-1] for i in out])

print(out)

input()

print("dumping...")

pickle.dump(out, fo)

print("DONE!")