import streamlit as st
import sys
import numpy as np
import pandas as pd
import openai
import uuid

st.title('Fairytail generation')
st.image("https://i.postimg.cc/yN20YX4F/Stories.png", use_column_width=True)
KEY = "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"
#keywords = ['Princess stuck in tower', 'Dragon and birds','Little boy, who disobey parent','Sun day','Little plant', 'Dinosaur and men']
keywords = ['Flowers and bees']


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
district_type = st.selectbox(
"Choose your hero",
('Knight','Princess', 'Dragon', 'Dog', 'King'))

recipe = 'Tell me fairyrail about {district_type}' 

def GPT_Completion(texts):
    ## Call the API key under your account (in a secure way)
    openai.api_key = "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"
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt =  texts,
    temperature = 0.8,
    top_p = 1,
    max_tokens = 2000,
    frequency_penalty = 0,
    presence_penalty = 0,
    n = 1
    )
    print(response.choices[0].text)
    #print(response.choices[1].text)
    return response.choices[0].text

responce = GPT_Completion(recipe)
