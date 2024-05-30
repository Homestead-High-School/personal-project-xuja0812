from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
# from text_processor import process
from fb_scraper import scrape

def sentiment_score(review, tokenizer, model):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return float(torch.argmax(result.logits)) + 1

# CREATE TOKENIZER AND MODEL FROM PRETRAINED SOURCES
def model_data(url, n):
    tokenizer = AutoTokenizer.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')
    model = AutoModelForSequenceClassification.from_pretrained('nlptown/bert-base-multilingual-uncased-sentiment')

    # SCRAPE THE DATA
    print("HELLO")
    df = scrape(url, n)

    pd.set_option('display.max_columns', 7)
    df['sentiment'] = df['texts'].apply(lambda x: sentiment_score(x[:512], tokenizer, model))

    with open(f'/Users/jasmi/Downloads/personal-project-xuja0812-3/model/FINAL_DATA.txt',"w", encoding="utf-8") as data_file:
        dfAsString = df.to_string(header=False, index=False)
        data_file.write(dfAsString)

    return df.to_string(header=False, index=False)
