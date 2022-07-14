# Import libraries
import numpy as np
import pickle
from flask import Flask, request, jsonify
from tensorflow.keras.preprocessing.sequence import pad_sequences
from utils import clean
from model import decode_sequence, in_tokenizer

app = Flask(__name__)
  
@app.route('/api/summarize', methods=['POST'])
def summarize():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    # Make prediction using model loaded from disk as per the data. 
    print("Review :",inp_review)

    inp_review = clean(inp_review,"inputs")
    inp_review = ' '.join(inp_review)
    inp_x      = in_tokenizer.texts_to_sequences([inp_review]) 
    inp_x      = pad_sequences(inp_x,  maxlen=max_in_len, padding='post')

    summary    = decode_sequence(inp_x.reshape(1,max_in_len))

    if 'eos' in summary :
        summary=summary.replace('eos','')
        print("\nPredicted summary:",summary);print("\n")

    return jsonify(output)



if __name__ == '__main__':
    app.run(port=5000, debug=True)