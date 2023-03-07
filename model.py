from keras.models import load_model
from keras.models import Sequential
import numpy as np
import json
from keras.optimizers import SGD

import pandas as pd

# Load JSON file into a pandas DataFrame
with open('intents.json') as f:
    data = json.load(f)
intents = data['intents']

# Normalize the nested JSON data
df = pd.json_normalize(intents, record_path='intents.json', meta=['tag'])


import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
import random

from keras.models import load_model

model = load_model('chatbot_model.h5')

random.shuffle(training)
training = np.array(training)

train_x = list(training[:,0])
train_y = list(training[:,1])

# Create model - 3 layers. First layer 128 neurons, second layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of intents to predict output intent with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))
print("First layer:",model.layers[0].get_weights()[0])

# Compile model. Stochastic gradient descent with Nesterov accelerated gradient gives good results for this model
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])


#fitting and saving the model 
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_model.h5', hist)

print("model created")
