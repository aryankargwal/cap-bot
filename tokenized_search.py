import numpy as np
from itertools import chain 
from tensorflow.keras.preprocessing.text import Tokenizer
from collections import Counter
import ast 
import pandas as pd

tokenizer = Tokenizer(num_words=1000, oov_token='<UNK>')

def fit_tokenizer_csv(df):
  tokenizer.fit_on_texts(df.iloc[:,0])

def preprocess(text):  
  sequences = tokenizer.texts_to_sequences(text)
  return sequences

def test_preprocess(test_text):  #tokenizing the keywords
  search = preprocess(test_text)
  search = list(chain.from_iterable(search))
  return search
 
def token_search(a, b):  
    count_a = Counter(a)  #getting all the elements of a and b
    count_b = Counter(b) 
  
    for key in count_b:   #checking if first list exsists in second list 
        if key not in count_a: 
            return False
        if count_b[key] > count_a[key]: 
            return False
    return True

def generate(df,keywords):  #displaying the camera and time
    k=-1
    for i in df.iloc[:,0]:
      i = ast.literal_eval(i)   #converting the row values from class string to class list
      res = token_search(i, test_preprocess(keywords))  #searching through the tokenized captions
      k+=1
      if res == True:
        return df.iloc[k][1],df.iloc[k][2]