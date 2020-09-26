import pandas as pd
import numpy as np
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
from textblob import Word, TextBlob
nltk.download('wordnet')

#=========================================== Pre-Define functions ===============================
def read_data(url:str):
    """read in data from a url
    """
    return pd.read_csv(url).iloc[:,0:2]

def add_col(dataset, colname:str, newcolname:str, function)->None:
  dataset[newcolname] = dataset[colname].apply(function)
  return None

def word_count(review_str)->int:
  """ count number of words in a string of reviews
  """
  return len(review_str.split())


def stopword_count(review_str:str)->int:
  """count number of stop words on a string
  """
  # load list of stop words
  from nltk.corpus import stopwords
  stop_words = stopwords.words("english")
  return len([word for word in review_str.split() if word.lower() in stop_words])


def lower_case(review_str:str)->str:
  """lower case a review string
  """
  return " ".join(word.lower() for word in review_str.split())


def remove_puncatuation(review_str:str)->str:
  """remove puncatuation of a string
  """
  import re
  return re.sub(r'[^\w\s]', '', review_str) 


def remove_length10_word(review_str:str)->str:
  """remove any words have length more than 10 on str
  """
  final_list =[]
  for word in review_str.split():
    if len(word)<10:
      final_list.append(word)
  
  return " ".join(final_list)


def average_word_length(word_list)->int:
    """calculate the average word length in each review
    """
    word_length = []
    for word in word_list.split(): 
        word_length.append(len(word))
    return np.mean(word_length)

def remove_stop_word(review_str:str)->str:
  """remove stop words from a string
  """
  from nltk.corpus import stopwords
  stopwords = stopwords.words("english")
  return " ".join(word for word in review_str.split() if word not in stopwords)

def lemmatize(review_str:str)->str:
    return " ".join(Word(word).lemmatize(pos="v") for word in review_str.split())

def get_polarity(review_str:str)->str:
    return TextBlob(lemmatize(remove_stop_word(remove_length10_word(remove_puncatuation(lower_case(review_str)))))).sentiment[0]

def get_subjecivity(review_str:str)->str:
    return TextBlob(lemmatize(remove_stop_word(remove_length10_word(remove_puncatuation(lower_case(review_str)))))).sentiment[1]

def text_summary(review_str:str)->dict:
    if len(review_str)>0:
      dict_data = {
          "text":review_str,
          "polarity":round(TextBlob(lemmatize(remove_stop_word(remove_length10_word(remove_puncatuation(lower_case(review_str)))))).sentiment[0],2),
          "subjecivity":round(TextBlob(lemmatize(remove_stop_word(remove_length10_word(remove_puncatuation(lower_case(review_str)))))).sentiment[1],2)
      }
      return dict_data
    else:
      return None
   





