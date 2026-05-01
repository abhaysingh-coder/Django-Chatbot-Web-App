import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, '..', 'Model', 'chatbot.pkl')
model_path = os.path.abspath(model_path)

with open(model_path, 'rb') as f:
    model = pickle.load(f)

def prediction(text):
    return model.predict([text])[0][-1]