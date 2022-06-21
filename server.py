import streamlit as st
import sys
import numpy as np
import pandas as pd
!pip install openai
!git clone https://github.com/AI-Fairytales/GPT3
!wget https://raw.githubusercontent.com/AI-Fairytales/GPT-3/master/merged_clean2.txt
st.title('Fairytail generation')
st.image("https://i.postimg.cc/yN20YX4F/Stories.png", use_column_width=True)


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

