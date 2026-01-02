from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load model files
model = joblib.load("model/disease_model.pkl")
le = joblib.load("model/label_encoder.pkl")
features = joblib.load("model/features.pkl")

@app.route("/")
def home():
    return render_template("index.html", symptoms=features)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    selected_symptoms = data["symptoms"]

    input_vector = np.zeros(len(features))
    for symptom in selected_symptoms:
        if symptom in features:
            input_vector[features.index(symptom)] = 1

    probabilities = model.predict_proba([input_vector])[0]

    results = []
    for i, prob in enumerate(probabilities):
        if prob >= 0.10:
            results.append({
                "disease": le.inverse_transform([i])[0],
                "confidence": round(prob * 100, 2)
            })

    results.sort(key=lambda x: x["confidence"], reverse=True)
    return jsonify(results)

if __name__ == "__main__":
    app.run(debug=True)