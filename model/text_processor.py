import re
from autocorrect import Speller
spell = Speller(lang='en')
import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
lemm = WordNetLemmatizer()

def shorten(words):
    patt = re.compile(r"(.)\1{2,}")
    return patt.sub(r"\1\1", words)

def process(document):

    # MAKES THE DOC LOWERCASE AND REMOVES LINKS, TAGS, MENTIONS
    temp = document.lower()
    temp = re.sub("@[A-Za-z0-9_]+", "", temp)
    temp = re.sub("#[A-Za-z0-9_]+", "", temp)
    temp = re.sub(r"http\S+", "", temp)
    temp = re.sub(r"www.\S+", "", temp)
    temp = re.sub("[0-9]", "", temp)
    temp = re.sub("'", "", temp)

    # TOKENIZE AND SPELLCHECK
    temp = word_tokenize(temp)
    temp = [shorten(w) for w in temp]
    temp = [spell(w) for w in temp]
    temp = [lemm.lemmatize(w) for w in temp]
    temp = [w for w in temp if len(w) > 2]
    temp = " ".join(w for w in temp)

    return temp