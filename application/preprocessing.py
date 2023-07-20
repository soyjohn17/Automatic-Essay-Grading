import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from bs4 import BeautifulSoup
from string import punctuation
import re
from nltk import word_tokenize

# nlp = spacy.load("en_core_web_lg")
stop_words = set(STOP_WORDS)
stop_words.update(punctuation)

#Function for removing html
def remove_html(tweet):
    return BeautifulSoup(tweet, "lxml").text

def remove_mintions(tweet):
    cleaned_tweet = re.sub(r"@\S+",'',tweet)
    return cleaned_tweet

def remove_duplicated_chars(tweet):
    return re.sub(r'(.)\1+', r'\1\1', tweet)

def remove_tweet_digits(tweet):
    cleaned_tweet = re.sub(r'[d]+', r'', tweet)
    cleaned_tweet = re.sub(r'[0-9]*','',tweet)
    cleaned_tweet = re.sub(r'([0-9]*\-[0-9]*)*', '', cleaned_tweet)
    return cleaned_tweet 

def remove_chars(tweet):
    cleaned_tweet = re.sub(r'[/(){}\[\]\|]', '', tweet)
    cleaned_tweet = re.sub(r'[!$%^?&*><]', '', cleaned_tweet )
    cleaned_tweet = re.sub(r'[\'\"،—.,;+-=]', '', cleaned_tweet )
    cleaned_tweet = re.sub(r'[\n]', '', cleaned_tweet ) # removing \n
    cleaned_tweet =re.sub(r"\s+",' ',cleaned_tweet) # remove_extra_white_space
    return cleaned_tweet

def remove_single_char_func(text, threshold=1):
    threshold = threshold
    words = word_tokenize(text)
    text = ' '.join([word for word in words if len(word) > threshold])
    return text