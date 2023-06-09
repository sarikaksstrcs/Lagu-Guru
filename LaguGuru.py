import streamlit as st
from LG import ml_word
import pandas as pd
# import googletrans
# from googletrans import Translator
# import google.cloud.natural_lanuage

import VrithamClassifier as vc

st.header("തേന്മാവ് : Malayalam Meter Classifier")

iframe_code = f'<iframe src="https://www.google.com/intl/ml/inputtools/try/" width="1000" height="600"></iframe>'
st.components.v1.html(iframe_code, width=1200, height=200)

poem_text = st.text_area("Enter your text here")

# Display the entered text
lines = poem_text.split("\n")

poem = ml_word(poem_text)

st.write("""
<style>
    .button-container {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
</style>
""", unsafe_allow_html=True)

st.write("<div class='button-container'>", unsafe_allow_html=True)
lagu_guru = st.button("ലഘു ഗുരു തിരിക്കുക")

classify_vritham = st.button("വൃത്തം കണ്ടെത്തുക")

st.write("</div>", unsafe_allow_html=True)

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
    # st.write(poem.syllables())
    data = { 'അക്ഷരങ്ങൾ' : poem.syllables(),
            'മാത്ര' : mathra
    }

    df = pd.DataFrame(data)

    # Convert DataFrame to HTML table string without index column
    table_html = df.to_html(index=False)

    # Display the table using st.markdown()
    st.markdown(table_html, unsafe_allow_html=True)

if classify_vritham:
    got =0
    if len(lines)==2:
        poem = ml_word(lines[0])
        akshara1 = poem.syllables()
        meter1 = poem.laghuguru()

        poem = ml_word(lines[1])
        akshara2 = poem.syllables()
        meter2 = poem.laghuguru()

        if vc.check_kakali(akshara1,meter1) and vc.check_manjari(akshara2,meter2):
                st.write("**മഞ്ജരി**")
                got = 1
        elif vc.check_abhirami(akshara2,meter2):
                st.write("**അഭിരാമി/ഊന്ന കാകളി**")
                got = 1
   
    if len(lines)>1 and not got:
        vritham = []
        for line in lines:
            poem = ml_word(line)
            akshara = poem.syllables()
            meter = poem.laghuguru()

            if vc.check_kakali(akshara,meter):
                vritham.append("കാകളി")
            
            elif vc.check_keka(akshara,meter):
                vritham.append("കേക")

            elif vc.find_len(akshara) == 10:
                vritham.append("മാവേലി")

            else:
                vritham.append("കണ്ടെത്താനായില്ല")

        data = { 'വരികൾ' : lines,
            'വൃത്തം' : vritham,
            }

        df = pd.DataFrame(data)
        table_html = df.to_html(index=False)

        # Display the table using st.markdown()
        st.markdown(table_html, unsafe_allow_html=True)

        for index, row in df.iterrows():
    # Access row data using column names
            if row['വൃത്തം'] == "കണ്ടെത്താനായില്ല":
                st.subheader("Suggestions")
                poem = ml_word(row['വരികൾ'])
                akshara = poem.syllables()
                meter = poem.laghuguru()
                if vc.find_len(akshara) == 14:
                    grouped_akshara,grouped_mathra = vc.divide_list_for_keka(akshara,meter)
                    final_txt = vc.correct_vritham_for_keka(grouped_akshara,grouped_mathra)
                else:
                    grouped_akshara,grouped_mathra = vc.divide_list_for_kakali(akshara,meter)
                    final_txt = vc.correct_vritham_for_kakali(grouped_akshara,grouped_mathra)
                st.markdown(final_txt, unsafe_allow_html=True)
        
        
        
    elif not got:
        poem = ml_word(poem_text)
        akshara = poem.syllables()
        meter = poem.laghuguru()

        if vc.find_len(akshara) == 10:
            st.write("**മാവേലി**")
        elif vc.check_kakali(akshara,meter):
            st.write("**കാകളി**")
        
        elif vc.check_keka(akshara,meter):
            st.write("**കേക**")

        else:
            st.write("**കണ്ടെത്താനായില്ല**")

