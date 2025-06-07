import pandas as pd
import streamlit as st
import  joblib
import numpy as np

dataset = pd.read_csv('personality_dataset.csv')

loaded_model = joblib.load('perceptron_model.pkl')

time_spent_alone = st.number_input("Hours spent alone daily (Max:24hrs):", min_value=0,max_value=24 ,value=0, step=1)


Stage_Fear = st.selectbox(
    "You have stage fright:",
    ["Yes", "No"]
)
Stage_Fear_numeric = 0 if Stage_Fear == "Yes" else 1


Social_event_attendance	 = st.slider("Frequency of Social Events:", min_value=0, max_value=10, value=0, step=1)



Going_outside	 = st.slider("Frequency of going outside:", min_value=0, max_value=7, value=0, step=1)


Drained_after_socializing = st.selectbox(
    "Feeling drained after socializing:",
    ["Yes", "No"]
)
Drained_after_socializing_numeric = 0 if Drained_after_socializing == "Yes" else 1



# Creating a slider
Friends_circle_size = st.slider("Number Of Close Friends:", min_value=0, max_value=15, value=0, step=1)




Post_frequency = st.slider("Social media post frequency:", min_value=0, max_value=10, value=0, step=1)




def PredictBehaviour():
    new_feature_loaded = np.array([[time_spent_alone, Stage_Fear_numeric, Social_event_attendance, Going_outside,
                                    Drained_after_socializing_numeric, Friends_circle_size, Post_frequency]])

    predicted_output_loaded = loaded_model.predict(new_feature_loaded)

    st.write("🔮 Predicted Personality Traits:")
    if predicted_output_loaded==0:
        st.write("You Are Extrovert")
    else:
        st.write('You Are Introvert')

data = {
    "time_spent_alone": [time_spent_alone],
    "Stage_Fear_numeric": [Stage_Fear_numeric],
    "Social_event_attendance": [Social_event_attendance],
    "Going_outside": [Going_outside],
    "Drained_after_socializing_numeric": [Drained_after_socializing_numeric],
    "Friends_circle_size": [Friends_circle_size],
    "Post_frequency": [Post_frequency]
}

if st.button("Predict"):
    PredictBehaviour()
    st.write("Your Personality Data")
    df = pd.DataFrame(data)
    st.table(df)
