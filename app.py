import streamlit as st
import pickle
import streamlit_option_menu as option_menu
from git.index.util import default_index

classifier= pickle.load(open('model.pkl', 'rb'))
lr= pickle.load(open('heart_disease.pkl', 'rb'))
svmmodel= pickle.load(open('svmmodel.pkl', 'rb'))

with st.sidebar:
    selected= option_menu('Multiple Disease Prediction System',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinson Detection'],default_index=0)




