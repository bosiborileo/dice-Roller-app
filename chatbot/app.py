from flask import Flask, render_template, jsonify, request


app = Flask(__name__)
import keras
import nltk
import pickle
import json
from keras.models import load_model
from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()

model=load_model('chatbot_model')
with open('chatbot\intents.json') as file:
  data = json.load(file)
#intents = json.loads(open('intents.json'))
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('chatbot\classes.pkl','rb'))


from chatbot import chat


app.config['SECRET_KEY'] = 'enter-a-very-secretive-key-3479373'

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template('index.html', **locals())

@app.route('/',methods=['GET','POST'])
#@app.route('/home',methods=['GET','POST'])
def main():
    return render_template('main.html')

@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():
    if request.method == 'POST':
        the_question = request.form['question']

        response = chat.chatbot_response(the_question)

    return jsonify({"response": response })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
