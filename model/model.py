import os
import shutil
import tarfile
import tensorflow as tf
from transformers import BertTokenizer, TFBertForSequenceClassification
import pandas as pd
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.offline as pyo
import plotly.graph_objects as go
from wordcloud import WordCloud, STOPWORDS
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from text_processor import process

# LOAD THE MODEL IN 
bert_model = TFBertForSequenceClassification.from_pretrained("PATH")
bert_tokenizer = BertTokenizer.from_pretrained("SAME PATH")

# ClEAN THE TEXT

# TOKENIZE
def convert(words):
    return bert_tokenizer.encode_plus(words,
                                      add_special_tokens = True,
                                      max_length = 128,
                                      pad_to_max_length = True,
                                      return_attention_mask = True)

def map_to_dictionary(input_ids, attention_masks, token_type_ids, label):
    return {
        "input_ids":input_ids,
        "attention_masks":attention_masks,
        "token_type_ids":token_type_ids,
    }, label

def encode(X, y):
    input_ids_list = []
    token_type_ids_list = []
    attention_mask_list = []
    label_list = []
    for text, label in zip(X, y):
        bert_input = convert(text)
        input_ids_list.append(bert_input['input_ids'])
        token_type_ids_list.append()
        attention_mask_list.append()
        label_list.append([label])
    return tf.data.Dataset.from_tensor_slices((input_ids_list, attention_mask_list, token_type_ids_list, label_list)).map(map_to_dictionary)

# TRAIN THE DATA
X_train, X_validation, y_train, y_validation = train_test_split(X_train, y_train, test_size=0.2, random_state=0)
ds_train_encoded = encode(process(X_train), y_train).shuffle(100).batch(32).repeat(2)
ds_val_encoded = encode(process(X_validation), y_validation).batch(32)

# TEST THE DATA
ds_test_encoded = encode(process(X_test), y_test).batch(32)

# COMPILE THE MODEL
learning_rate = 3e-5
optimizer = tf.keras.optimizers.Adam(learning_rate=learning_rate, epsilon=1e-08)
loss = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
metric = tf.keras.metrics.SparseCategoricalAccuracy('accuracy')
bert_model.compile(optimizer=optimizer, loss=loss, metrics=[metric])

# TRAIN AND EVALUATE
bert_model.fit(ds_train_encoded, epochs=2, validation_data=ds_val_encoded)

loss, acc = bert_model.evaluate(ds_test_encoded, verbose = 0)
print("accuracy: {:5.2f}%".format(100 * acc))