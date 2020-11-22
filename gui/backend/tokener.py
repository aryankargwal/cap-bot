from tensorflow.keras.preprocessing.text import Tokenizer
from itertools import chain 

caption = ['man', 'with', 'beard', 'and', 'beard', 'standing', 'in', 'front', 'of', 'an', 'building']

def tlk(caption):
    tokenizer = Tokenizer(num_words=1000, oov_token='<UNK>')
    tokenizer.fit_on_texts(caption)

    sequences = tokenizer.texts_to_sequences(caption)
    sequences =list(chain.from_iterable(sequences))

    return sequences

