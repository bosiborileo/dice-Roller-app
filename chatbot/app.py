import keras
import nltk
import pickle
import json

from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

from keras.models import load_model
model=load_model('model.h5')
with open('chatbot\intents.json') as file:
  data = json.load(file)
#intents = json.loads(open('intents.json'))
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('chatbot\classes.pkl','rb'))

import chat

