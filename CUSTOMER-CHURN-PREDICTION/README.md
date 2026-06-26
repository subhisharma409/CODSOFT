# 🏦 Bank Customer Churn Prediction

A Machine Learning project that predicts whether a customer is likely to leave the bank or stay based on customer information such as credit score, age, balance, geography, activity status, and more.

---
Live demo:
## 📌 Project Overview

Customer churn is one of the biggest challenges faced by banks. This project uses Machine Learning to analyze customer behavior and predict whether a customer is likely to exit the bank.

The project includes:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training
* Model Comparison
* Hyperparameter Tuning
* Streamlit Web Application
* Model Deployment

---

## 📂 Dataset

**Dataset:** `Churn_Modelling.csv`

The dataset contains customer information such as:

* Credit Score
* Geography
* Gender
* Age
* Tenure
* Balance
* Number of Products
* Has Credit Card
* Is Active Member
* Estimated Salary
* Exited (Target Variable)

### Target Variable

* `0` → Customer Stays
* `1` → Customer Leaves

---

## ⚙️ Technologies Used

### Python Libraries

* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* XGBoost
* Joblib
* Streamlit

---

## 🧠 Machine Learning Workflow

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Encoding
4. Train-Test Split
5. Feature Scaling
6. Model Training
7. Model Evaluation
8. Hyperparameter Tuning
9. Save Model
10. Build Streamlit Application

---

## 🤖 Models Used

* Logistic Regression
* Decision Tree Classifier
* Random Forest Classifier
* Gradient Boosting Classifier
* XGBoost Classifier

---

## 📊 Evaluation Metrics

* Accuracy Score
* Precision Score
* Recall Score
* F1 Score
* Confusion Matrix
* Classification Report

---

## 🚀 Best Model

**XGBoost Classifier**

Chosen based on overall performance and F1 Score.

---

## 📁 Project Structure

```text
Bank_Customer_Churn_Prediction
│
├── app.py
├── customer_churn_prediction.ipynb
├── Churn_Modelling.csv
├── bank_churn_model.pkl
├── scaler.pkl
├── README.md
└── requirements.txt
```

---

## ▶️ Run Locally

### Clone Repository

```bash
git clone <repository-link>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 📈 Features

* Predict customer churn
* Probability-based prediction
* Interactive Streamlit UI
* Multiple ML models comparison
* Hyperparameter tuning
* Model persistence using Joblib

---

## 🎯 Future Improvements

* Feature Importance Visualization
* SHAP Explainability
* SMOTE for handling class imbalance
* Advanced Hyperparameter Tuning
* Deployment on Streamlit Cloud
* Improved User Interface

---

## 👨‍💻 Author

**Subhi Sharma**

B.Tech (Artificial Intelligence and Machine Learning)

GL Bajaj Institute of Technology and Management

GitHub: https://github.com/subhisharma409

LinkedIn: https://www.linkedin.com/in/subhi-sharma/

---

## ⭐ If you found this project useful, consider giving it a star!
