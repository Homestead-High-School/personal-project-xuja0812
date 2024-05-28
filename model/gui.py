import streamlit as st
from new_model import model_data
import re

company = st.text_input("Enter a reviews link here", "Type here...")
if(st.button("Submit")):
   # result = model_data(company)
   # f = open('FINAL_DATA.txt', 'r')
   # result = f.read()
   # reviews = result.split("\n")
   # print_out = ""
   # for j in range(len(reviews)):
   #    arr = re.split("[" "]+", reviews[j])
   #    rec = ""
   #    index = 0
   #    while(arr[index] != 'recommend' and arr[index] != 'recommends'):
   #       rec += arr[index]
   #       index+=1
   #    rec += arr[index]
   #    index+=1
   #    name = arr[index]
   #    rev = ""
   #    for i in range(index + 1, len(arr)):
   #       rev += arr[i]
   #    print_out += name + "\n" + rec + "\n" + rev + "\n"

   # FORMATTING

   # st.success(result)
   st.success(company)

# TO DO: Make the URL work without having to input the whole thing, format
#  the output!
#  also aggregate the total sentiment and return the average