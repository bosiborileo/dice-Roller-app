import streamlit as st
import tensorflow as tf
import numpy as np

# Define the model and load weights
model = tf.keras.models.load_model('chatbot_model')

# Define the vocabulary and index-to-word mappings
vocab = {0: '<PAD>', 1: '<START>', 2: '<END>', ...}
index2word = {i: w for w, i in vocab.items()}

# Define the function to preprocess the input text
def preprocess_input(text):
    # Tokenize the text
    tokens = text.lower().split()
    # Convert tokens to indices
    indices = [vocab.get(token, vocab['<UNK>']) for token in tokens]
    # Pad or truncate to a fixed length
    max_length = 100
    padded_indices = np.zeros((1, max_length))
    padded_indices[0, :len(indices)] = indices[:max_length]
    return padded_indices

# Define the function to generate a response
def generate_response(text):
    # Preprocess the input text
    input_indices = preprocess_input(text)
    # Generate a response using the model
    output_indices = model.predict(input_indices)[0]
    # Convert indices to words
    output_words = [index2word.get(i, '<UNK>') for i in output_indices]
    # Join the words into a string and return it
    return ' '.join(output_words)

# Define the Streamlit app
def main():
    st.title('Annie')
    st.write('Enter your message below:')
    # Get user input
    user_input = st.text_input('You:', '')
    if user_input:
        # Generate a response
        response = generate_response(user_input)
        # Display the response
        st.write('Bot:', response)

if __name__ == '__main__':
    main()
