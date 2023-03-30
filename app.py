from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates
import datetime

app = Flask(__name__)
cr = CurrencyRates()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def convert():
    user_input = float(request.form["npr"])
    inr = cr.convert("AUD", "INR", user_input)
    npr = round(inr * 1.60, 2)
    current_datetime = datetime.datetime.now()
    cur_time = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", aud=npr, time=cur_time)

if __name__ == "__main__":
    app.run(debug=True)
