import streamlit as st
import pandas as pd
import tensorflow as tf
import numpy as np
import tensorflow_recommenders as tfrs

data = pd.read_csv('Data/coursesData.csv')


def courseFunction(id):
    id = data['course'][data['id'] == id]

    return list(id)[0]


st.header('Programme Recommender')

form = st.form(key='form')

course = form.selectbox(label='Select course', options=data['course'])
slider = form.slider('Number of courses', min_value=1, max_value=10, step=1,)
submit = form.form_submit_button()

if submit:
    model = tf.keras.models.load_model('model')
    _, titles = model(np.array([course]))
    courses = []

    for i in range(0,len(titles[0,:])):
        word = str(titles[0,:][i])
        words = word.split("'")

        if words[1] != course:
            courses.append(words[1])
    remDupli = set()
    courses = [course for course in courses if not( (course in remDupli) or (remDupli.add(course)))]
    slider += 1
    if slider > len(courses):
        slider = len(courses)
    for i in range(1,slider):
        st.write(courses[i])

