from flask import Flask

app = Flask(__name__)

@app.route('/predict_gradient_boosting', methods=['POST'])
def predict_gradient_boosting():
    try:
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Gradient Boosting prediction function
        result = hotel_prediction(request_json["features"], gradient_boosting_model)

        # Return the result as a JSON response
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/predict_neural_networks', methods=['POST'])
def predict_neural_networks():
    try:
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Gradient Boosting prediction function
        result = hotel_prediction(request_json["features"],neural_networks_model)

        # Return the result as a JSON response
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
@app.route('/predict_random_forest', methods=['POST'])
def predict_random_forest():
    try:
        # Get the request data from the user in JSON format
        request_json = request.get_json()

        # Send it to the Random Forest prediction function
        result = hotel_prediction(request_json["features"], random_forest_model)

        # Return the result as a JSON response
        return jsonify(result)

    except Exception as e:
        return jsonify({'error': str(e)})
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)