import streamlit as st
from new_model import model_data

company = st.text_input("Enter a reviews link here", "Type here...")
if(st.button("Submit")):
   result = model_data(company)
   st.success(result)

# TO DO: Make the URL work without having to input the whole thing, format
#  the output!
#  also aggregate the total sentiment and return the average