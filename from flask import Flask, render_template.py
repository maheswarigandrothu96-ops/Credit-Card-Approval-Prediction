from flask import Flask, render_template, request
import joblib
import numpy as np
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Credit Card Fraud Detection"

if __name__ == "__main__":
    app.run(debug=True)

app = Flask(__name__)

# Load trained model
model = joblib.load("credit_model.pkl")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        features = []

        # Read 30 input values
        for i in range(30):
            features.append(float(request.form[f"f{i}"]))

        features = np.array(features).reshape(1, -1)

        prediction = model.predict(features)

        if prediction[0] == 1:
            result = "Fraud Transaction"
        else:
            result = "Normal Transaction"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return render_template("index.html", prediction_text=str(e))

if __name__ == "__main__":
    app.run(debug=True)