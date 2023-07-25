from flask import render_template, request, redirect
from flask import current_app as app
from application.preprocessing import *

from string import punctuation
import re
import spacy
from spacy.lang.en.stop_words import STOP_WORDS
stop_words = set(STOP_WORDS)
stop_words.update(punctuation)

import pickle

# Define route for grading essays
@app.route('/', methods=['GET', 'POST'])
def grade_essay():
    if request.method == 'POST':
        essay = request.files.get('file-upload') or request.form.get('essay')
        essay = essay.lower()
        essay = essay.replace('[^\w\s]','')
        essay = " ".join([w for w in str(essay).split() if not w in stop_words])
        essay = remove_html(essay)
        essay = remove_mintions(essay)
        essay = remove_duplicated_chars(essay)
        essay = remove_tweet_digits(essay)
        essay = remove_chars(essay)
        essay = remove_single_char_func(essay)

        with open('./model/tfid_model.pkl', 'rb') as file:
            tf = pickle.load(file)

        

        features = tf.transform([essay])

        with open('./model/selector.pkl', 'rb') as file:
            selector = pickle.load(file)

        features = selector.transform(features)


        with open('./model/random_forest_model.pkl', 'rb') as file:
            model = pickle.load(file)

        print(model.predict(features))
        
    return render_template('index.html')
    

@app.route('/results', methods=['GET', 'POST'])
def results():
    return render_template('results.html')