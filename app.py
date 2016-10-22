import pickle

from flask import Flask, request, render_template
app = Flask(__name__)

words = pickle.load(open("words.dat", "rb"))
inverseWords = pickle.load(open("inversewords.dat", "rb"))
relatedPhenomes = pickle.load(open("relatedphenomes.dat", "rb"))

def getPuns(word):

	punProns = []
	for pron in words[word]:
		punProns.append(pron)
		pronList = pron.split()
		for i, phenome in enumerate(pronList):
			for newPhenome in relatedPhenomes[phenome]:
				newPron = pronList[:]
				newPron[i] = newPhenome
				newPronStr = " ".join(newPron)
				punProns.append(newPronStr)

	puns = []
	for pron in punProns:
		if pron in inverseWords:
			puns.extend(inverseWords[pron])

	puns = [pun for pun in puns if pun != word] # Remove original word

	return puns



@app.route("/", methods=["GET"])
def getIndex():
    return render_template("index.html")

@app.route("/results", methods=["POST"])
def getResults():
    word = request.form["word"]
    return str(getPuns(word))


if __name__ == "__main__":
    app.run(port=80)