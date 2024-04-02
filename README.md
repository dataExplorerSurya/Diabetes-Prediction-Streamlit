# Diabetes Prediction 🩺💉

This project aims to predict the likelihood of an individual having diabetes based on certain health metrics. The prediction model is built using Support Vector Machine (SVM) algorithm and deployed using Streamlit. The deployed application is hosted on Streamlit Cloud.

## 📋 Project Overview
The project consists of the following main components:
- A Streamlit web application for user interaction and prediction.
- An SVM model trained on a dataset containing health metrics to predict diabetes.
- Deployment of the application on Streamlit Cloud.

## 🚀 How to Run
To run the Streamlit application locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run the Streamlit app using the command `streamlit run stremlit.py`.
4. Access the application in your web browser at the provided URL.

## 📊 Dataset Description
The dataset used for training the prediction model contains the following columns:
1. 👶 Pregnancies: Number of times pregnant
2. 🩸 Glucose: Plasma glucose concentration a 2 hours in an oral glucose tolerance test
3. 💓 BloodPressure: Diastolic blood pressure (mm Hg)
4. 📏 SkinThickness: Triceps skin fold thickness (mm)
5. 💉 Insulin: 2-Hour serum insulin (mu U/ml)
6. 🏋️‍♀️ BMI: Body mass index (weight in kg/(height in m)^2)
7. 🧬 DiabetesPedigreeFunction: Diabetes pedigree function
8. 🎂 Age: Age (years)
9. 🎯 Outcome: Class variable (0 or 1) indicating whether the individual has diabetes or not

## 🌐 Deployment
The application is deployed on Streamlit Cloud and can be accessed [here](https://diabetes-prediction-app-hqukd6c7bfeei5xyclj4tx.streamlit.app/).
