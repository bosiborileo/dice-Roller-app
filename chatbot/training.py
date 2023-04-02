import json
import pickle
import numpy as np
import nltk
import random
import string

nltk.download('punkt')#sentence tokenizer
nltk.download('wordnet') #lexical database for the English 
nltk.download('omw-1.4')

from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD

lemmatizer = WordNetLemmatizer()

words=[]
classes = []
documents = []
ignore_words = ['?', '!', '.', ',']

#loading intents.json
with open('chatbot\intents.json', 'r') as intents:
  data = json.load(intents)

for intent in data['intents']:
    for pattern in intent['patterns']:
        #tokenize each word
        tokens = nltk.word_tokenize(pattern)
        words.extend(tokens)# add each elements into list
        #combination between patterns and intents
        # add single element into end of list
        documents.append(pattern)
        ignore_words.append(intent["tag"])
        # add to tag in our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatize, lower each word and remove duplicates
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in string.punctuation]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

#print words
print (len(words), "unique lemmatized words\n", words, "\n")

#print classes
print (len(classes), "classes\n", classes, "\n")

#words = all words, vocabulary
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#creating training data
training = []
output_empty = [0]*len(classes)

# creating the bag of words model
for idx, doc in enumerate(documents):
    bow = []
    text = lemmatizer.lemmatize(doc.lower())
    for word in words:
        if word in text:
          bow.append(1)
        else:
            bow.append(0)
    # mark the index of class that the current pattern is associated
    output_row = list(output_empty)
    output_row[classes.index(classes[1])] = 1
    # add BoW and associated classes to training 
    training.append([bow, output_row])

random.shuffle(training)
training= np.array(training, dtype=object)
  
# splitting the data
train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

#defining parameters
input_shape = (len(train_x[0]),)
output_shape = len(train_y[0])
epochs = 500

#deep learning model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

history = model.fit(np.array(train_x), np.array(train_y), epochs=500, batch_size=5)
model.save('model.h5', history)
print('model summary')
print("Training data has been created")




    