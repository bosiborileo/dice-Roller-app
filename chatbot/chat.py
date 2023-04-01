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

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words
# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words) 
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tag):
            result = random.choice(i['responses'])
            break
    return result

def chatbot_response(text):
    ints = predict_class(text, model)
    res = getResponse(ints, intents)
    return res


from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get')
def get_response():
    userText = request.args.get('msg')
    if get_response(userText).confidence < 0.5:
        return str("Sorry, I don't understand")
    else:
        get_response(userText).confidence = 1
        return str(get_response(userText))
if __name__ == '__main__':
    app.run(debug=True)


           

