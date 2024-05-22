from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import numpy as np
from text_processor import process
from fb_scraper import scrape

def sentiment_score(review):
    tokens = tokenizer.encode(review, return_tensors='pt')
    result = model(tokens)
    return torch.argmax(result.logits) + 1

# CREATE TOKENIZER AND MODEL FROM PRETRAINED SOURCES
tokenizer = AutoTokenizer.from_pretrained('URL')
model = AutoModelForSequenceClassification.from_pretrained('URL')

# ENCODE (EXTRACT SENTIMENT)
tokens = tokenizer.encode('I hated this, absolutely the worst', return_tensors='pt')

# PASS ENCODED STRING TO MODEL
result = model(tokens)
torch.argmax(result.logits) + 1

# SCRAPE THE DATA

df = scrape()

#     # REPLACE THIS WITH XPATH

# r = requests.get('URL')
# soup = BeautifulSoup(r.text, 'html.parser')
# regex = re.compile('.*comment.*')
# results = soup.find_all('p',{'class':regex})
# reviews = [result.text for result in results]

#     # PREPROCESS THE DATA

# TURN INTO DATAFRAME
# df = pd.DataFrame(np.array(reviews), columns=['review'])
# df['review'].iloc[0]

df['sentiment'] = df['review'].apply(lambda x: sentiment_score(x[:512]))
