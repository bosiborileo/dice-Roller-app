import json
import random
import numpy as np
import pickle
import warnings
warnings.filterwarnings('ignore')

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

import json
import pickle
from keras.models import load_model

# load intents from JSON file
with open('chatbot\intents.json', 'r') as f:
    intents = json.load(f)

# load pickled data
with open('chatbot\words.pkl', 'rb') as f:
    words = pickle.load(f)
with open('chatbot\classes.pkl', 'rb') as f:
    classes = pickle.load(f)

# load model
try:
    model = load_model('chatbot\model.h5')
except OSError as e:
    print(f"Error loading model: {e}")


'''intents_file = open('intents.json').read()
intents= json.loads('intents_json')
with open('words.pkl', 'rb') as f:
     words = pickle.loads(f.read())
classes = pickle.load(open('classes.pkl', 'rb'))

#loading the model
from keras.models import load_model
model = load_model('chatbot_model')'''

def clean_text(text):
    # tokenize the pattern - split words into array
    tokens = nltk.word_tokenize(text)
    # stem each word - create short form for word
    tokens = [lemmatizer.lemmatize(word.lower()) for word in tokens]
    return tokens
# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bag_of_words(text, vocab):
    # tokenize the pattern
    tokens = clean_text(text)
    # bag of words - matrix of N words, vocabulary matrix
    bow = [0]*len(words) 
    for w in tokens:
        for idx, word in enumerate(vocab):
            if word == w: 
                # assign 1 if current word is in the vocabulary position
                bow[idx] = 1
                
    return(np.array(bow))

def predict_class(text, vocab, labels):
    # filter out predictions below a threshold
    bow = (text, vocab)
    result = model.predict(np.array([bow]))[0]
    ERROR_THRESHOLD = 0.25
    y_pred = [[idx, res] for idx, res in enumerate(result) if res > ERROR_THRESHOLD]
    y_pred.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in y_pred:
       return_list.append(labels[r[0]])
    return return_list

def get_response(intents_list, intents_json): 
    tag = intents_list[0]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents: 
        result= random.choice(i['responses'])
    return result,tag

def chatbot_response(text):
    message = input("")
    ints = predict_class(message, words, classes)
    response = get_response(intents, ints)
    return response

from flask import Flask, render_template, request
app = Flask(__name__, template_folder='template')

@app.route('/',methods=['GET','POST'])
def login():
    return render_template('login.html')

@app.route('/home',methods=['GET','POST'])
def register():
    return render_template('register.html')

@app.route('/chat',methods=['GET','POST'])
def index():
    return render_template('index.html')

@app.route('/get')
@app.route("/get")
def chatbot():
    userText = request.args.get('msg')
    resp=chatbot_response(userText)
    return resp
if __name__ == '__main__':
    app.run(debug=True)        

