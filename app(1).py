#imports
import joblib
from keras import models
from tensorflow import keras
from flask import Flask, request, jsonify

app = Flask(__name__)

# Loading your machine learning models
random_forest_model = joblib.load('random_forest_model.pkl')
gradient_boosting_model = joblib.load('gradient_boost_model.pkl')
neural_networks_model = keras.models.load_model("keras_model.h5")

# Define a prediction function
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
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Gradient Boosting prediction function
        result = hotel_prediction(request_json["features"], gradient_boosting_model)

        # Return the result as a JSON response
        return jsonify(result.tolist())  # Convert predictions to a list

    except Exception as e:
        return jsonify({'error': str(e)})


# neural network route
@app.route('/predict_neural_networks', methods=['POST'])
def predict_neural_networks():
    try:
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Neural Networks prediction function
        result = hotel_prediction(request_json["features"], neural_networks_model)

        # Return the result as a JSON response
        return jsonify(result.tolist())  # Convert predictions to a list

    except Exception as e:
        return jsonify({'error': str(e)})

# random forest model
@app.route('/predict_random_forest', methods=['POST'])
def predict_random_forest():
    try:
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Random Forest prediction function
        result = hotel_prediction(request_json["features"], random_forest_model)

        # Return the result as a JSON response
        return jsonify(result.tolist())  # Convert predictions to a list

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)