from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")  # טוען את הקובץ index.html מתוך תיקיית templates

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # אם השרת דורש פורט מסוים (כמו ב-Render) נשתמש בו
    app.run(host="0.0.0.0", port=port)
