
import os
import pickle

# Set the path to the model
model_path = os.path.join(os.path.dirname(__file__), 'models', 'model.pkl')

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

    
def predict(data):
    return model.predict(data)