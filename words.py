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
    respuesta = requests.get("https://991360be.ngrok.io/definition/" + word)

    respuesta = respuesta.json()
    params = {
        "word": word,
        "definition": respuesta.get("definition")
    }
    return params

if __name__ == "__main__":
    app.run(debug=True)
