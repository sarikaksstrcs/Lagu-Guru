import streamlit as st
from LG import ml_word
import pandas as pd
# import googletrans
# from googletrans import Translator
# import google.cloud.natural_lanuage

import VrithamClassifier as vc

st.header("Lagu Guru Classifier")

poem_text = st.text_area("Enter your text here")

# Display the entered text
lines = poem_text.split("\n")

poem = ml_word(poem_text)

lagu_guru = st.button("ലഘു ഗുരു തിരിക്കുക")
classify_vritham = st.button("വൃത്തം കണ്ടെത്തുക")

if lagu_guru:
    mathra = []
    for x in poem.laghuguru():
        if x == 'L':
            mathra.append('ലഘു')

        elif x == 'G':
            mathra.append('ഗുരു')

        else:
            mathra.append(' ')

    # print(mathra)
    st.write(poem.syllables())
    data = { 'അക്ഷരങ്ങൾ' : poem.syllables(),
            'മാത്ര' : mathra
    }

    df = pd.DataFrame(data)

    # Convert DataFrame to HTML table string without index column
    table_html = df.to_html(index=False)

    # Display the table using st.markdown()
    st.markdown(table_html, unsafe_allow_html=True)

if classify_vritham:
    vritham = []
    for line in lines:
        poem = ml_word(line)
        akshara = poem.syllables()
        meter = poem.laghuguru()
        if vc.check_kakali(akshara,meter):
            vritham.append("കാകളി")
        elif vc.check_keka(akshara,meter):
            vritham.append("കേക")

    data = { 'വരികൾ' : lines,
            'വൃത്തം' :  vritham
    }
    df = pd.DataFrame(data)

    print(data)
    # Convert DataFrame to HTML table string without index column
    table_html = df.to_html(index=False)

    # Display the table using st.markdown()
    st.markdown(table_html, unsafe_allow_html=True)
