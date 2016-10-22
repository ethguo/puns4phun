import pickle
import requests
import random

from flask import Flask, request, render_template

app = Flask(__name__)

words = pickle.load(open("words.dat", "rb")) #set
wordPhenomes = pickle.load(open("wordphenomes.dat", "rb"))
inverseWords = pickle.load(open("inversewords.dat", "rb"))
relatedPhenomes = pickle.load(open("relatedphenomes.dat", "rb"))

azureUrl = "https://api.datamarket.azure.com/Bing/Search/"
azureAccountKey = "Ik3BvLpK4JOlYRrFXsgICaI1/hBudlGvUz7RB7NMojc"

def getPuns(word):

    punProns = []
    for pron in wordPhenomes[word]:
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

    print("prewords", puns)

    puns = set(puns) & words # Remove non-dictionary words

    try: puns.remove(word) # Remove original word
    except KeyError: pass

    return puns

@app.route("/", methods=["GET"])
def getIndex():

    return render_template("index1.html")

@app.route("/results", methods=["POST"])
def getResults():
    word = request.form["word"]
    phrase = request.form["phrase"]

    print(word)

    # requests.get(imgSearchUrl)

    puns = getPuns(word)
    print(puns)

    pun = random.choice(list(puns))

    phrase = phrase.replace(word.lower(), pun.lower())

    return str(phrase)



if __name__ == "__main__":
    app.run(debug=True)
#    app.run(host="0.0.0.0", port=80)
