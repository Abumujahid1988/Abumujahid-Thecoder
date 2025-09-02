import os
import requests
from flask import Flask, render_template, request, redirect
import mysql.connector
from datetime import datetime

app = Flask(__name__)

# Hugging Face API setup
HUGGINGFACE_API_KEY = os.getenv("HF_API_KEY") or "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"
API_URL = "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english"
HEADERS = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="mooduser",
    password="moodpass123",
    database="mood_journal"
)
cursor = db.cursor(dictionary=True)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        content = request.form["entry"]
        date = datetime.now()

        # 🔹 Send text to Hugging Face API
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": content})
        result = response.json()

        if isinstance(result, list) and len(result) > 0:
            sentiment = result[0]["label"]
            confidence = float(result[0]["score"])
        else:
            sentiment = "UNKNOWN"
            confidence = 0.0

        # Save to MySQL
        cursor.execute(
            "INSERT INTO entries (entry_date, content, sentiment, confidence) VALUES (%s, %s, %s, %s)",
            (date, content, sentiment, confidence)
        )
        db.commit()

        return redirect("/")

    # Fetch all entries for display + chart
    cursor.execute("SELECT * FROM entries ORDER BY entry_date ASC")
    entries = cursor.fetchall()

    return render_template("index.html", entries=entries)

if __name__ == "__main__":
    app.run(debug=True)
