import nltk
import json
import warnings
import random
import numpy as np
import pickle

nltk.download('punkt')#Sentence tokenizer
from nltk.stem import WordNetLemmatizer

warnings.filterwarnings('ignore')

from keras.models import load_model
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import random

lemmatizer = WordNetLemmatizer()

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open(r"C:\\Users\user\Music\annete\intents.json").read() # read json file
intents = json.loads(data_file) # load json file

with open('words.pkl', 'rb') as f:
     words = pickle.loads(f.read())
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('chatbotmodel.h5')


def clean_up_sentences(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)
                      for word in sentence_words]
    return sentence_words
  
def bagw(sentence):
    sentence_words = clean_up_sentences(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
  
def predict_class(sentence):
    bow = bagw(sentence)
    res = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res)
               if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({'intent': classes[r[0]],
                            'probability': str(r[1])})
        return return_list
  
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result
  
print("Chatbot!")
  
while True:
    message = input("")
    ints = predict_class(message)
    res = get_response(ints, intents)
    print(res)
