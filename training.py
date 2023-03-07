import random
import json
import pickle
import numpy as np
import nltk

import nltk
nltk.download('punkt')#sentence tokenizer

from keras.models import Sequential
from nltk.stem import WordNetLemmatizer
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
lemmatizer = WordNetLemmatizer()

nltk.download('wordnet') #lexical database for the English 
nltk.download('omw-1.4')

words=[]
classes = []
documents = []
ignore_words = ['?', '!']
data_file = open("intents.json").read() # read json file
intents = json.loads(data_file) # load json file

for intent in intents['intents']:
    for pattern in intent['patterns']:
        #tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)# add each elements into list
        #combination between patterns and intents
        documents.append((w, intent['tag']))#add single element into end of list
        # add to tag in our classes list
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# lemmatize, lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
# sort classes
classes = sorted(list(set(classes)))
# documents = combination between patterns and intents
print (len(documents), "documents\n", documents, "\n")
# classes = intents[tag]
print (len(classes), "classes\n", classes, "\n")
# words = all words, vocabulary
print (len(words), "unique lemmatized words\n", words, "\n")
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(classes,open('classes.pkl','wb'))

#creating training data
training = []
output_empty = [0]*len(classes)
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(
        word.lower()) for word in word_patterns]
    for word in words:
        bag.append(1) if word in word_patterns else bag.append(0)
          
    # making a copy of the output_empty
    output_row = list(output_empty)
    output_row[classes.index(document[1])] = 1
    training.append([bag, output_row])
random.shuffle(training)
training = np.array(training)
  
# splitting the data
train_x = list(training[:, 0])
train_y = list(training[:, 1])

print("Training data has been created")

from tensorflow.python.framework import ops
ops.reset_default_graph()


    