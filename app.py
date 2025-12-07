from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    month = int(request.form["month"])
    pred = model.predict([[month]])
    return render_template("index.html", prediction=round(pred[0],2))

if __name__ == "__main__":
    app.run(debug=True)
