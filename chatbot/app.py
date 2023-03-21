import nltk
import json
import warnings
import random
import numpy as np
import pickle
import chatbot
import requests
import os
import time

from chatbot import app
from flask import Flask
from flask import render_template,flash, request
from _init_ import model,words,classes,intents

warnings.filterwarnings('ignore')

from nltk.stem import WordNetLemmatizer
from keras.models import load_model

lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

with open('words.pkl', 'rb') as f:
     words = pickle.loads(f.read())
classes = pickle.load(open('classes.pkl', 'rb'))
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
  
@app.route('/',methods=['GET','POST'])
#@app.route('/home',methods=['GET','POST'])
def yo():
    return render_template('main.html')

@app.route('/chat',methods=['GET','POST'])
#@app.route('/home',methods=['GET','POST'])
def home():
    return render_template('index.html')

@app.route("/get")
def chatbot():
    userText = request.args.get('msg')
    resp=response(userText)
    return resp
