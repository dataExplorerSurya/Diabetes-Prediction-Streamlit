import streamlit as st
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib


st.set_page_config(page_title="Prediction",page_icon=":⚕️:")
# Load the trained model
model = joblib.load("SVC.pkl")
# Initialize StandardScaler
scaler = StandardScaler()


def classify(data):
    data=scaler.fit_transform(data)
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(data)
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = model.predict(input_data_reshaped)
      
    return prediction[0]



def main():
    st.title("Diabetes Prediction 👨‍⚕️")
    Pregnancies = st.text_input('Number of Pregnancies:',placeholder="Enter number")
    Glucose = st.text_input('Glucose Level:',placeholder="Enter number")
    BloodPressure = st.text_input('Blood Pressure value:',placeholder="Enter number")
    SkinThickness = st.text_input('Skin Thickness value:',placeholder="Enter number")
    Insulin = st.text_input('Insulin Level:',placeholder="Enter number")
    BMI = st.text_input('BMI value:',placeholder="Enter number")
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value:',placeholder="Enter number")
    Age = st.text_input('Age of the Person:',placeholder="Enter number")

    diagnosis = ''

    if st.button('Diabetes Test Result'):
        if Pregnancies=="" or Glucose=="" or BloodPressure=="" or SkinThickness=="" or Insulin=="" or BMI=="" or DiabetesPedigreeFunction=="" or Age=="":
            st.error('Enter Valid Data', icon="🚨")
        else:
            diagnosis = classify([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction,Age]])

            if diagnosis:
                st.warning('The person is diabetic 🤒')
            else:
                st.success("{} ".format("The person is not diabetic 😃"))


    

    
    

if __name__=='__main__':
    main()
