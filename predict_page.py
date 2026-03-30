#Predict_page
import pickle
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler




def load_model():
    with open ("Saved_steps.pkl", 'rb') as file:
        data = pickle.load(file)
    return data

data = load_model()

rfc = data["model"]
sc = data["scaler"]
chest_pain_type = ["Typical Angina","Atypical Angina","Non-Anginal Pain", "Asymptomatic"]
def show_predict_page():
    st.title("Heart Failure Detection ")
    st.write("""We need clinical data for the diagnosis""")
    age = st.slider("Age", min_value=1,max_value=115)
    sex = st.selectbox("Sex", ["Male", "Female"])

    

    chest_pain = st.selectbox("Chest pain type",chest_pain_type)
    

    bloodpressure = st.slider("Resting blood pressure (in mm Hg on admission to hospital)",min_value=10,max_value=250)

    cholesterol = st.slider("Serum Cholesterol in mg/dl",min_value=100,max_value=450)

    fasting_bloodsugar = st.selectbox("Is the fasting bloodsugar > 120 mg/dl",["Yes", "No"])


    ecg = st.selectbox("ECG",["Normal", "Having ST-T wave abnormality", "Left ventricular hypertrophy"])


    max_heart_rate = st.slider("Maximum heart rate",min_value=50,max_value=250)

    exercise_angina = st.selectbox("Exercise induced angina",["Yes", "No"])


    old_peak = st.selectbox("Old peak (ST slope induced by exercise relative to rest)",[0,1,1.5,2])

    st_slope = st.selectbox("ST Slope (Slope of the peak exercise ST slope segment)",["Upsloping", "Flat", "Downsloping"])


    

    ok = st.button("Calculate the risk")
    
    if ok:
        # Encode categorical variables
        if sex == "Male":
            sex_enc = 1 
        else:
            sex_enc = 0
        if chest_pain == "Typical Angina":
            chest_pain_enc = 1
        elif chest_pain == "Atypical Angina":
            chest_pain_enc = 2
        elif chest_pain == "Non-Anginal Pain":
            chest_pain_enc = 3
        else:  # Asymptomatic
            chest_pain_enc = 0
        if fasting_bloodsugar == "Yes":
            fasting_bloodsugar_enc = 1
        else:
            fasting_bloodsugar_enc = 0
        if ecg == "Normal":
            ecg_enc = 0
        elif ecg == "Having ST-T wave abnormality":
            ecg_enc = 1
        else:  # Left ventricular hypertrophy
            ecg_enc = 2
        if exercise_angina == "Yes":
            exercise_angina_enc = 1
        else:
            exercise_angina_enc = 0
        if st_slope == "Upsloping":
            st_slope_enc = 1
        elif st_slope == "Flat":
            st_slope_enc = 2
        else:  # Downsloping
            st_slope_enc = 3

        # Numerical features
        X_num = np.array([[age, bloodpressure, cholesterol, max_heart_rate, old_peak]])
        X_num_scaled = sc.transform(X_num)

        # Categorical features
        X_cat = np.array([sex_enc, chest_pain_enc, fasting_bloodsugar_enc, ecg_enc, exercise_angina_enc, st_slope_enc])

        # Combine
        X = np.concatenate([X_num_scaled[0], X_cat])

        prediction = rfc.predict([X])
        if prediction[0] == 0:
            st.subheader("No major risk found")
        else:
            st.subheader("High risk of heart disease.")



    



