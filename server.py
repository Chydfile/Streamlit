import streamlit as st
import sys
import numpy as np
import pandas as pd
st.title('Fairytail generation')
st.image("https://s.wsj.net/public/resources/images/BN-IS945_london_G_20150603154805.jpg", use_column_width=True)


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
('Dragon', 'Princess', 'Knight', 'Dog', 'King'))

