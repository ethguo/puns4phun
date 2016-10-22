import pickle

from flask import Flask, request
app = Flask(__name__)

words = pickle.load(open("words.dat", "rb"))
inverseWords = pickle.load(open("inversewords.dat", "rb"))
relatedPhenomes = pickle.load(open("relatedPhenomes", "rb"))

# def phenomeSearch(word):
#     return 

# def reverseSearch(phenomes):

#     return inverseWordsDB[phenomes]

indexHTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Puns 4 Phun</title>
</head>
<body style="font-family: "Comic Sans MS", cursive, sans-serif;">
<h1>PUNS 4 PHUN</h1>
<form action="/results" method="POST" accept-charset="utf-8">
    <input type="text" name="word" value="READ" />
    <input type="submit" value="Submit" />
</form>
</body>
</html>
"""

@app.route("/", methods=["GET"])
def getIndex():
    return indexHTML

@app.route("/results", methods=["POST"])
def getResults():
    word = request.form["word"]
    return str([inverseWordsDB[phenomes] for phenomes in wordsDB[word]]) 


if __name__ == "__main__":
    app.run(debug=True)