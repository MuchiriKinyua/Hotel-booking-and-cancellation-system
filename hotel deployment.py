from flask import Flask, request, jsonify
import joblib
import json
from sklearn.externals import joblib

# Save Logistic Regression model
joblib.dump(Logistic_Regression, 'logistic_regression_model.joblib')
logistic_regression_model = joblib.load('logistic_regression_model.joblib')

# Logistic Regression prediction route
@app.route('/predict_lr', methods=['POST'])
def predict_lr():
    input_data = request.get_json()
    # ... preprocess input_data as needed
    prediction = logistic_regression_model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

random_forest_model = joblib.load('random_forest_model.joblib')
joblib.dump(Random_Forest, 'random_forest_model.joblib')

# Random Forest prediction route
@app.route('/predict_rf', methods=['POST'])
def predict_rf():
    input_data = request.get_json()
    # ... preprocess input_data as needed
    prediction = random_forest_model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

gradient_boosting_model = joblib.load('gradient_boosting_model.joblib')
joblib.dump(Gradient_Boosting, 'gradient_boosting_model.joblib')

# Gradient Boosting prediction route
@app.route('/predict_gb', methods=['POST'])
def predict_gb():
    input_data = request.get_json()
    # ... preprocess input_data as needed
    prediction = gradient_boosting_model.predict(input_data)
    return jsonify({'prediction': int(prediction[0])})

if __name__ == '__main__':
    app.run(debug=True)

# create new flask app here
app = Flask(__name__)

# helper function here

def hotel_prediction(features):
    """
    Given the features, we can predict booking and cancellation of a hotel
    """

    # Load the model from the file
    with open("model.pkl", "rb") as f:
        model = joblib.load(f)

    # Construct the 2D matrix of values that .predict is expecting
    # X = [[sepal_length, sepal_width, petal_length, petal_width]]

    # Get a list of predictions and select only 1st
    predictions = model.predict(features)
    prediction = int(predictions[0])

    return {"predicted_class": prediction}


# defining routes here

@app.route('/', methods=['GET'])
def index():
    return 'Hello, welcome to Hotel booking platform'

@app.route('/predict', methods=['POST'])
def predict():
    # Get the request data from the user in JSON format
    request_json = request.get_json()

    # Send it to our prediction function using ** to unpack the arguments
    result = hotel_prediction(request_json["features"])

    # Return the result as a string with JSON format
    return json.dumps(result)

