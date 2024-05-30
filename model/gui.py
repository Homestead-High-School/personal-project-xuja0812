import streamlit as st
from new_model import model_data
import re

company = st.text_input("Enter a reviews link here", "Type here...")
num = st.text_input("Enter # of reviews here", "Type here...")
if(st.button("Submit")):
   result = model_data(company, num)
   result_split = result.split("\n")
   printable = ""
   sum = 0.0
   for review in result_split:
      words = re.split(r"\s+", review)
      sen = float(words[len(words)-1])
      sum += sen
   for review in result_split:
      words = re.split(r"\s+", review)
      rec = ""
      index = 0
      while words[index] != 'recommend' and words[index] != 'recommends':
         rec += words[index] + " "
         index+=1
      rec += words[index]
      index += 1
      name = words[index]
      index += 1
      rev = ""
      for i in range (index, len(words)-1):
         rev += words[i] + " "
      sentiment = words[len(words)-1]
      printable += "\n" + name + "\n\n" + rec + "\n\n" + rev + "\n\n" + sentiment + "\n"
      # st.success(name)
      # st.success(rec)
      # st.success(rev)
   # st.success(result)
   avg = sum / len(result_split)
   printable = "THE AVERAGE SENTIMENT IS: " + str(avg) + "\n\n\n" + printable
   st.success(printable)

# TO DO: Make the URL work without having to input the whole thing, format
#  the output!
#  also aggregate the total sentiment and return the average
#  also try to train the BERT model myself