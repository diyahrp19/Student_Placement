from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Placement Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = [
        data['cgpa'],
        data['aptitude'],
        data['communication'],
        data['projects']
    ]

    prediction = model.predict([features])[0]

    return jsonify({
        'prediction': int(prediction)
    })

if __name__ == '__main__':
    port=int(os.environ.get("PORT",5000))
    app.run(host="0.0.0.0",port=port)