# import arrr
from pyscript import document
import js
from model.new_model import model_data, sentiment_score
# import pyodide_html as html
import requests
import re
import transformers

def display(event):
    out = document.querySelector("#output_div")
    out.innerText = "HELLO"
    input_text = document.querySelector("#email")
    comp = input_text.value.split(" ")
    company = ""
    for word in comp:
        company += word
    url = 'https://www.facebook.com/' + company + '/reviews'
    t = model_data(url)

    out = document.querySelector("#output_div")
    out.innerText = "DONE!"

    # arr = t.split("\n")
    # n = arr.length
    # for j in range(n):
    #     text = arr[j]
    #     rec = ""
    #     review = re.split("[" "]+", text)
    #     index = 0;
    #     while(review[index] != 'recommend' and review[index] != 'recommends'):
    #         rec += review[index] + " ";
    #         index+=1;
    #     rec += review[index];
    #     name = review[index + 1];
    #     rev = "";
    #     for i in range(index+2, review.length -1):
    #         rev += review[i] + " ";
    #     rating = review[review.length-1];
    #     all = document.createElement("div");
    #     all.className = "full-review";
    #     name_e = document.createElement("div");
    #     name_e.innerText = name;
    #     name_e.className = "name";
    #     rec_e = document.createElement("div");
    #     rec_e.innerText = rec;
    #     rec_e.className = "rec";
    #     rev_e = document.createElement("div");
    #     rev_e.innerText = rev;
    #     rev_e.className = "rev";
    #     rating_e = document.createElement("div");
    #     rating_e.innerText = rating;
    #     rating_e.className = "rating";
    #     all.appendChild(name_e);
    #     all.appendChild(rec_e);
    #     all.appendChild(rev_e);
    #     all.appendChild(rating_e);
    #     element = document.getElementById("list");
    #     element.appendChild(all);
    
    