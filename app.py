import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np

data = pd.read_csv('Data/coursesData.csv')


def courseFunction(id):
    id = data['course'][data['id'] == id]

    return list(id)[0]


st.header('Programme Recommender')

form = st.form(key='form')

id = form.selectbox(label='Select course', options=data['id'], format_func=courseFunction)
slider = form.slider('Number of courses',min_value=1,max_value=8,step=1,)
submit = form.form_submit_button()

if submit:
    model = tf.keras.models.load_model('model')
    _, titles = model(np.array([str(id)]))
    courses = []
    for i in range(1,len(titles[0,:])):
        word = str(titles[0,:][i])
        words = word.split("'")
        courses.append(words[1])
    remDupli = set()
    courses = [course for course in courses if not (course in remDupli) or (remDupli.add(course))]
    slider += 1
    if slider > len(courses):
        slider = len(courses)
    for i in range(1,slider):
        st.write(courses[i])

