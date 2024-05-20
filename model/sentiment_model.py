import pandas as pd
import sklearn
import os
from text_processor import process

# CREATES PATHS TO INPUT AND OUTPUT FILES IF THEY DO NOT EXIST ALREADY
input_path = 'input'
output_path = 'output'
if(os.path.exists(input_path) is False):
    os.mkdir(input_path)
if(os.path.exists(output_path) is False):
    os.mkdir(output_path)

# probably will have to change this file path later
sentiment_file = 'training.1600000.processed.noemoticon.csv'

columns = ['polarity', 'id', 'post_datetime', 'query', 'user', 'tweet']
df_tweets = pd.read_csv(sentiment_file, encoding='UTF', names=columns, encoding_errors='ignore')

# GETS 2000 TWEETS FROM THE DATASET
df = df_tweets[['polarity', 'tweet']].sample(n=2000, random_state=0)

# CREATE OUTPUT FILE
df.to_csv("output/selected_tweets2000.csv", index=False)

print(df_tweets.polarity.value_counts())

# SPLIT DATA INTO TRAIN AND TEST DATA
from sklearn.model_selection import train_test_split
x = df.tweet.values
y = df.polarity.replace(4, 1)

# SPLIT THE DATA
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
