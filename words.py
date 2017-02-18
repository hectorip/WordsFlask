# -*- coding: utf-8 -*-
# Diccionario
from flask import Flask, render_template, jsonify
import requests
import logging

# "/home"
# "/word/<word>"

app = Flask(__name__)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/word/<word>")
def words(word):
    params = get_params_for_word(word)
    return render_template("word.html", **params)

@app.route("/api/word/<word>")
def api_words(word):
    params = get_params_for_word(word)
    return jsonify(params)

def get_params_for_word(word):

    headers = {
        'app_id': 'bc5402cb',
        'app_key': 'fb1da4ae020a29281b1a9a1845c97343'
    }
    response = requests.get("https://od-api.oxforddictionaries.com:443/api/v1/entries/es/" + word.lower(), headers=headers)

    if response.status_code == 200:
        response_dict = response.json()
        results = response_dict["results"][0]
        lexicalEntries = results["lexicalEntries"]
        definitions = []
        for le in lexicalEntries:
            entries = le["entries"]
            for entry in entries:
                senses = entry["senses"]
                for sense in senses:
                    defs = sense["definitions"]
                    for definition in defs:
                        definitions.append(definition)
        # print("algo")
        # definitions = [le["entries"]["senses"][0] for le in lexicalEntries]
    else:
        print("ERROR!!")

    params = {
        "word": word,
        "definitions": definitions
    }
    return params

if __name__ == "__main__":
    app.run(debug=True)
