import requests
import os
from dotenv import load_dotenv
from flask import Flask, render_template, jsonify

load_dotenv()

API_KEY = os.getenv("NINJA_API_KEY")
API_URL = "https://api.api-ninjas.com/v1/quotes"

headers = {
    "X-Api-Key": API_KEY
}

app = Flask(__name__)

def generate_ai_quote():
    response = requests.get(API_URL, headers=headers)

    print("STATUS:", response.status_code)
    print("TEXT:", response.text)

    if response.status_code != 200:
        return "API request failed", "Invalid API key or limit reached"

    data = response.json()

    # API Ninjas sometimes returns empty list
    if not data:
        return "No quote available right now", "API Ninjas"

    return data[0].get("quote", "No quote"), data[0].get("author", "Unknown")


@app.route("/")
def home():
    quote, author = generate_ai_quote()
    return render_template("index.html", quote=quote, author=author)


@app.route("/quote")
def quote():
    q, a = generate_ai_quote()
    return jsonify({"quote": q, "author": a})


if __name__ == "__main__":
    app.run(debug=True)