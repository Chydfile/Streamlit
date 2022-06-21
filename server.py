#!/usr/bin/env python
import streamlit as st
import sys
import numpy as np
import pandas as pd
import openai
import uuid
import os
from gtts import gTTS

st.set_page_config(page_title="Crontab - Shritam")
st.title('Fairytail generation')
st.image("https://i.postimg.cc/yN20YX4F/Stories.png", use_column_width=True)
#keywords = ['Princess stuck in tower', 'Dragon and birds','Little boy, who disobey parent','Sun day','Little plant', 'Dinosaur and men']
keywords = ['Flowers and bees']

# #def GPT_Completion(texts):
#     ## Call the API key under your account (in a secure way)
#     openai.api_key = 'sk-frXvTud0CBEIqZ33z33LT3BlbkFJJTUQammxhA4ppfP8Br'
#     response = openai.Completion.create(
#     engine="text-davinci-002",
#     prompt =  texts,
#     temperature = 0.8,
#     top_p = 1,
#     max_tokens = 2000,
#     frequency_penalty = 0,
#     presence_penalty = 0,
#     n = 1
#     )
#     print(response.choices[0].text)
#     return response.choices[0].text

# add_selectbox = st.sidebar.selectbox(
#     "*Название города",
#     ("Лондон",)
# )
# add_selectbox = st.sidebar.selectbox(
#     "*Язык",
#     ("Русский",)
# )
# st.sidebar.write('*В демонстрационной версии доступен только один город - Лондон и родной язык разработчика.')
# st.sidebar.write('Модель построена с использованием данных c Airbnb, оценивались данные о 40к объектов в Лондоне.')
# st.sidebar.write('В демонстационной версии использованы не все доступные признаки. Инструмент, выбранный для предсказания - Сatboost.')

try:
    form_1 = st.form(key='my-form1')
    command = form_1.selectbox("Choose your hero",
('knight','princess', 'dragon', 'dog', 'king'))
    submit = form_1.form_submit_button('Submit')

    if submit:
        recipe = 'Tell fairy tail about {}.'.format(command)
        #responce = GPT_Completion(recipe)
        #st.text_area('Fairy tail about {}:'.format(command), responce)
        language = 'en'
        myobj = gTTS(text=recipe, lang=language, slow=False)
        myobj.save("welcome.mp3")
        audio_file = open('welcome.mp3', 'rb')
        audio_bytes = audio_file.read()
        st.audio(audio_bytes)
        
except Exception as e:
    st.success(f'Something Went Wrong!😁 {e}')

#print(f'Audio content written to file "{outfile}"')


#responce = GPT_Completion(recipe)
#st.text(responce)

