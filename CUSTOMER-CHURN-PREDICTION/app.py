import streamlit as st
import joblib
import numpy as np


model = joblib.load("bank_churn_model.pkl")
scalar = joblib.load("scaler.pkl")

st.title("🏦 Bank Customer Churn Prediction")
st.write("Enter customer details below:")


credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
geography = st.selectbox("Geography",["France", "Germany", "Spain"])

gender = st.selectbox("Gender",["Male", "Female"])
age = st.number_input("Age", min_value=18, max_value=100, value=40)
tenure = st.number_input("Tenure", min_value=0, max_value=10, value=5)
balance = st.number_input("Balance", value=50000.0)

num_of_products = st.number_input("Number of Products",min_value=1,max_value=4,value=1)

has_cr_card = st.selectbox("Has Credit Card?",[0,1])

is_active_member = st.selectbox("Is Active Member?",[0,1])

estimated_salary = st.number_input("Estimated Salary",value=50000.0)



Geography_Germany = 0
Geography_Spain = 0

if geography == "Germany":
    Geography_Germany = 1
elif geography == "Spain":
    Geography_Spain = 1

Gender_Male = 1 if gender == "Male" else 0

input_data = np.array([[age,tenure,credit_score,num_of_products,has_cr_card,balance,is_active_member,estimated_salary,Geography_Germany,Geography_Spain,Gender_Male]])

if st.button("Predict"):
    st.write("Input Data:")
    st.write(input_data)
    input_scaled = scalar.transform(input_data)
    prediction = model.predict(input_scaled)
    probability = model.predict_proba(input_scaled)

    if prediction[0] == 1:
        st.error("Customer is likely to leave the bank.")
    else:
        st.success("Customer is likely to stay with the bank.")