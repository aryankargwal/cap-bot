from tensorflow.keras.preprocessing.text import Tokenizer
from itertools import chain 
from collections import Counter   

def tlk(caption):
    tokenizer = Tokenizer(num_words=1000, oov_token='<UNK>')
    tokenizer.fit_on_texts(caption)

    sequences = tokenizer.texts_to_sequences(caption)
    sequences =list(chain.from_iterable(sequences))

    return sequences

def checkInFirst(a, b): 

    b = tlk(b)

     #getting count 
    count_a = Counter(a) 
    count_b = Counter(b) 
  
    #checking if element exsists in second list 
    for key in count_b: 
        if key not in  count_a: 
            return False
        if count_b[key] > count_a[key]: 
            return False
    return True