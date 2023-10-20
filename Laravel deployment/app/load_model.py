# load_model.py

import pickle

def load_gradient_boost_model():
    model_path = 'gradient_boost_model.pkl'

    with open(model_path, 'rb') as file:
        gradient_boost_model = pickle.load(file)

    return gradient_boost_model

# You can define similar functions for loading other models if needed

if __name__ == "__main__":
    # This allows you to test loading the model when running the script directly
    model = load_gradient_boost_model()
    # Perform any testing or additional logic if needed
