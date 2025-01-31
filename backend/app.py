from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from loadData import model, vectorizer

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    # Extract symptom text properly
    symptoms_text = data["symptoms"]  # Make sure this is a string

    if not isinstance(symptoms_text, str):
        return jsonify({"error": "Invalid input. Expected a string."}), 400

    # Convert input text into numerical format
    symptoms_transformed = vectorizer.transform([symptoms_text])  # Wrap it in a list

    # Predict disease
    prediction = model.predict(symptoms_transformed)

    print("result", prediction)

    return jsonify({"Predicted Disease": prediction[0]})


if __name__ == '__main__':
    app.run(debug=True)
