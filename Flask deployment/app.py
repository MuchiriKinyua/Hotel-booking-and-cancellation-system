#imports
import joblib
import numpy as np
from keras import models
from tensorflow import keras
from flask import Flask, request, jsonify

app = Flask(__name__)

# Loading the machine learning models
gradient_boosting_model = joblib.load('gradient_boost_model.pkl')
neural_networks_model = keras.models.load_model("keras_model.h5")

# Defining a prediction function
def hotel_prediction(features, model):
    predictions = model.predict(features)  
    return predictions 

# root route
@app.route('/', methods=['GET'])
def index():
    return 'Hello, welcome to Hotel booking platform'

# gradient boost route
@app.route('/predict_gradient_boost', methods=['POST'])
def predict_gradient_boosting():
    try:
        # Getting the request data from the user in JSON format
        request_json = request.get_json()

        # Gradient Boosting prediction function
        result = hotel_prediction(request_json["features"], gradient_boosting_model)

        # Returning the result as a JSON response
        return jsonify(result.tolist())  # Convert predictions to a list

    except Exception as e:
        return jsonify({'error': str(e)})


# neural network route
@app.route('/predict_neural_networks', methods=['POST'])
def predict_neural_networks():
    try:
        # Getting the request data from the user in JSON format
        request_json = request.get_json()

        # Neural Networks prediction function
        result = hotel_prediction(request_json["features"], neural_networks_model)

        # Returning the result as a JSON response
        return jsonify(result.tolist())  

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)