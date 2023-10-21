import dash
import joblib
import warnings
import numpy as np
from dash import html
from dash import dcc
from tensorflow import keras
from dash import Input, Output
warnings.filterwarnings("ignore")
from sklearn.impute import SimpleImputer


gradient_boosting_model = joblib.load('gradient_boost_model.pkl')
neural_networks_model = keras.models.load_model("keras_model.h5")

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div([
    # New input components for additional features
    dcc.Input(id='input-hotel', type='text', placeholder='Enter Hotel type'),  html.Br(),
    dcc.Input(id='input-market-segment', type='text', placeholder='Enter Market Segment'), html.Br(),
    dcc.Input(id='input-distribution-channel', type='text', placeholder='Enter Distribution Channel'), html.Br(),
    dcc.Input(id='input-is-repeated-guest', type='text', placeholder='Enter Is Repeated Guest'), html.Br(),
    dcc.Input(id='input-deposit-type', type='text', placeholder='Enter Deposit Type'), html.Br(), 
    dcc.Input(id='input-customer-type', type='text', placeholder='Enter Customer Type'), html.Br(),
    dcc.Input(id='input-special-requests', type='text', placeholder='Enter Has Special Requests'), html.Br(),

    # Output component
    html.Div(id='output-prediction')
])


# Define callback to make predictions using the loaded models
@app.callback(
    Output('output-prediction', 'children'),
    [
        Input('input-hotel', 'value'),
        Input('input-market-segment', 'value'),
        Input('input-distribution-channel', 'value'),
        Input('input-is-repeated-guest', 'value'),
        Input('input-deposit-type', 'value'),
        Input('input-customer-type', 'value'),
    ]
)
def make_predictions(
    hotel, market_segment, distribution_channel, is_repeated_guest,
    deposit_type, customer_type
 ):
    try:
        # Combine all input features into a format expected by your model
        features = [
            hotel, market_segment, distribution_channel, is_repeated_guest,
            deposit_type, customer_type
        ]
        
        imputer = SimpleImputer(strategy='mean')

        # Fit the imputer on your data to compute the imputation values
        imputer.fit([features])

        # Reshape your input features into a NumPy array and impute missing values
        input_features_imputed = imputer.transform([features])

        # Make predictions using your machine learning models
        prediction1 = gradient_boosting_model.predict([input_features_imputed[0]])  # Use imputed input
        prediction2 = neural_networks_model.predict([input_features_imputed[0]])  # Use imputed input

        result = f'Model 1 Prediction: {prediction1[0]}, Model 2 Prediction: {prediction2[0]}'
    except Exception as e:
        result = 'Invalid input or error: ' + str(e)

    return result


if __name__ == '__main__':
    app.run_server(port=8051, debug=True)
