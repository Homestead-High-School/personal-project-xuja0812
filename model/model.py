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

