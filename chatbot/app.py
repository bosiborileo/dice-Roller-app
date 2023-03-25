from flask import Flask, render_template, jsonify, request
import chatbot

app = Flask(__name__)

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

        response = chatbot.chatbot_response(the_question)

    return jsonify({"response": response })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8888', debug=True)
