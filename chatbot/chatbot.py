import json
import random
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

intents = json.loads(open('intents.json').read())
with open('words.pkl', 'rb') as f:
     words = pickle.loads(f.read())
classes = pickle.load(open('classes.pkl', 'rb'))

#loading the model
from keras.models import load_model
model = load_model('chatbot_model')

def clean_up_sentences(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word)
                      for word in sentence_words]
    return sentence_words
  
def bagofwords(sentence):
    sentence_words = clean_up_sentences(sentence)
    bag = [0] * len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
    return np.array(bag)
  
def predict_class(sentence):
    bow = bagofwords(sentence)
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
    #print tag
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i['tag'] == tag:
            result = random.choice(i['responses'])
            break
    return result

def response(text):
    return_list=predict_class(text,model)
    response,_=get_response(return_list,intents,text)
    return response
  
print("Let's chat! (type 'quit' to exit)")


