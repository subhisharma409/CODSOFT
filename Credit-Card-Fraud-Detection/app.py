import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# =====================================
# Load Demo Samples
# ====================================
import os

from pathlib import Path

BASE_DIR = Path(__file__).parent
model = joblib.load(BASE_DIR / "model.pkl")
scaler = joblib.load(BASE_DIR / "scaler.pkl")
encoders = joblib.load(BASE_DIR / "encoders.pkl")
fraud_sample = joblib.load(BASE_DIR / "fraud_sample.pkl")
legit_sample = joblib.load(BASE_DIR / "legitimate_sample.pkl")

# =====================================
# Page Configuration
# =====================================

st.set_page_config(
    page_title="Credit Card Fraud Detection",
    page_icon="💳",
    layout="wide"
)

# =====================================
# Custom CSS
# =====================================

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

h1,h2,h3,h4{
    color:white;
}

.stButton>button{
    width:100%;
    height:55px;
    font-size:20px;
    border-radius:10px;
    background:#0E9F6E;
    color:white;
}

.stButton>button:hover{
    background:#057A55;
}

.css-1d391kg{
    background:#111827;
}

.metric-box{
    background:#1F2937;
    padding:15px;
    border-radius:12px;
    text-align:center;
    color:white;
}

</style>
""", unsafe_allow_html=True)

defaults = {

    "merchant": encoders["merchant"].classes_[0],
    "category": encoders["category"].classes_[0],
    "gender": encoders["gender"].classes_[0],
    "state": encoders["state"].classes_[0],
    "job": encoders["job"].classes_[0],

    "amt": 100.0,
    "zip": 90210,
    "lat": 40.7128,
    "long": -74.0060,
    "city_pop": 50000,
    "merch_lat": 40.7135,
    "merch_long": -74.0010,

    "date": datetime.today().date(),
    "time": datetime.now().time().replace(second=0,microsecond=0)

}

for key,value in defaults.items():

    if key not in st.session_state:

        st.session_state[key] = value

# =====================================
# Demo Buttons
# =====================================

st.sidebar.subheader("🎯 Demo Transactions")

c1,c2 = st.sidebar.columns(2)

if c1.button("🚨 Fraud"):

    row = fraud_sample.iloc[0]

    st.session_state["merchant"] = encoders["merchant"].inverse_transform(
        [int(row["merchant"])]
    )[0]

    st.session_state["category"] = encoders["category"].inverse_transform(
        [int(row["category"])]
    )[0]

    st.session_state["gender"] = encoders["gender"].inverse_transform(
        [int(row["gender"])]
    )[0]

    st.session_state["state"] = encoders["state"].inverse_transform(
        [int(row["state"])]
    )[0]

    st.session_state["job"] = encoders["job"].inverse_transform(
        [int(row["job"])]
    )[0]

    st.session_state["amt"] = float(row["amt"])
    st.session_state["zip"] = int(row["zip"])
    st.session_state["lat"] = float(row["lat"])
    st.session_state["long"] = float(row["long"])
    st.session_state["city_pop"] = int(row["city_pop"])
    st.session_state["merch_lat"] = float(row["merch_lat"])
    st.session_state["merch_long"] = float(row["merch_long"])

    dt = datetime.fromtimestamp(int(row["unix_time"]))

    st.session_state["date"] = dt.date()
    st.session_state["time"] = dt.time().replace(microsecond=0)
    st.session_state["unix_time"] = int(row["unix_time"])
    st.session_state["hour"] = int(row["hour"])
    st.session_state["day"] = int(row["day"])
    st.session_state["month"] = int(row["month"])


if c2.button("✅ Legit"):

    row = legit_sample.iloc[0]

    st.session_state["merchant"] = encoders["merchant"].inverse_transform(
        [int(row["merchant"])]
    )[0]

    st.session_state["category"] = encoders["category"].inverse_transform(
        [int(row["category"])]
    )[0]

    st.session_state["gender"] = encoders["gender"].inverse_transform(
        [int(row["gender"])]
    )[0]

    st.session_state["state"] = encoders["state"].inverse_transform(
        [int(row["state"])]
    )[0]

    st.session_state["job"] = encoders["job"].inverse_transform(
        [int(row["job"])]
    )[0]

    st.session_state["amt"] = float(row["amt"])
    st.session_state["zip"] = int(row["zip"])
    st.session_state["lat"] = float(row["lat"])
    st.session_state["long"] = float(row["long"])
    st.session_state["city_pop"] = int(row["city_pop"])
    st.session_state["merch_lat"] = float(row["merch_lat"])
    st.session_state["merch_long"] = float(row["merch_long"])

    dt = datetime.fromtimestamp(int(row["unix_time"]))

    st.session_state["date"] = dt.date()
    st.session_state["time"] = dt.time().replace(microsecond=0)
    st.session_state["unix_time"] = int(row["unix_time"])
    st.session_state["hour"] = int(row["hour"])
    st.session_state["day"] = int(row["day"])
    st.session_state["month"] = int(row["month"])

# =====================================
# Title
# =====================================

st.title("💳 Credit Card Fraud Detection")

st.write(
    """
Predict whether a transaction is **Fraudulent** or **Legitimate**
using an **XGBoost Machine Learning Model**.
"""
)

# =====================================
# Model Performance
# =====================================

col1,col2,col3,col4,col5 = st.columns(5)

with col1:
    st.metric("Accuracy","99.90%")

with col2:
    st.metric("Precision","90.61%")

with col3:
    st.metric("Recall","83.21%")

with col4:
    st.metric("F1 Score","86.75%")

with col5:
    st.metric("ROC-AUC","99.21%")

st.divider()

# =====================================
# Sidebar
# =====================================

st.sidebar.title("Transaction Details")

st.sidebar.subheader("Customer Information")


# =====================================
# Customer Information
# =====================================

st.sidebar.subheader("Customer Information")

merchant = st.sidebar.selectbox(
    "Merchant",
    encoders["merchant"].classes_,
    key="merchant"
)

category = st.sidebar.selectbox(
    "Category",
    encoders["category"].classes_,
    key="category"
)

gender = st.sidebar.selectbox(
    "Gender",
    encoders["gender"].classes_,
    key="gender"
)

state = st.sidebar.selectbox(
    "State",
    encoders["state"].classes_,
    key="state"
)

job = st.sidebar.selectbox(
    "Job",
    encoders["job"].classes_,
    key="job"
)

city_pop = st.sidebar.number_input(
    "City Population",
    min_value=0,
    key="city_pop"
)

zip_code = st.sidebar.number_input(
    "ZIP Code",
    min_value=0,
    key="zip"
)

st.sidebar.divider()

# =====================================
# Transaction Information
# =====================================

st.sidebar.subheader("Transaction Information")

amt = st.sidebar.number_input(
    "Transaction Amount ($)",
    min_value=0.0,
    key="amt"
)

lat = st.sidebar.number_input(
    "Customer Latitude",
    format="%.4f",
    key="lat"
)

long = st.sidebar.number_input(
    "Customer Longitude",
    format="%.4f",
    key="long"
)

merch_lat = st.sidebar.number_input(
    "Merchant Latitude",
    format="%.4f",
    key="merch_lat"
)

merch_long = st.sidebar.number_input(
    "Merchant Longitude",
    format="%.4f",
    key="merch_long"
)

st.sidebar.divider()

# =====================================
# Transaction Time
# =====================================

st.sidebar.subheader("Transaction Time")

selected_date = st.sidebar.date_input(
    "Select Date",
    key="date"
)

selected_time = st.sidebar.time_input(
    "Select Time",
    key="time"
)



# =====================================
# Time Features
# =====================================

if "unix_time" in st.session_state:

    unix_time = st.session_state["unix_time"]
    hour = st.session_state["hour"]
    day = st.session_state["day"]
    month = st.session_state["month"]

else:

    transaction_datetime = datetime.combine(
        selected_date,
        selected_time
    )

    unix_time = int(transaction_datetime.timestamp())

    hour = transaction_datetime.hour
    day = transaction_datetime.day
    month = transaction_datetime.month

# =====================================
# Encode Categorical Features
# =====================================

merchant_encoded = encoders["merchant"].transform([merchant])[0]

category_encoded = encoders["category"].transform([category])[0]

gender_encoded = encoders["gender"].transform([gender])[0]

state_encoded = encoders["state"].transform([state])[0]

job_encoded = encoders["job"].transform([job])[0]

# =====================================
# Transaction Summary
# =====================================

st.subheader("📋 Transaction Summary")

summary = pd.DataFrame({

    "Feature":[
        "Merchant",
        "Category",
        "Gender",
        "State",
        "Job",
        "Amount",
        "City Population",
        "Latitude",
        "Longitude",
        "Merchant Latitude",
        "Merchant Longitude",
        "Transaction Date",
        "Transaction Time"
    ],

    "Value":[
        merchant,
        category,
        gender,
        state,
        job,
        amt,
        city_pop,
        lat,
        long,
        merch_lat,
        merch_long,
        selected_date,
        selected_time
    ]

})

st.dataframe(
    summary,
    use_container_width=True,
    hide_index=True
)

st.divider()

# =====================================
# Predict Button
# =====================================

predict = st.button("🔍 Predict Transaction")

if predict:

    input_df = pd.DataFrame([{

        "merchant":merchant_encoded,

        "category":category_encoded,

        "amt":amt,

        "gender":gender_encoded,

        "state":state_encoded,
        "zip":zip_code,

        "lat":lat,

        "long":long,

        "city_pop":city_pop,

        "job":job_encoded,

        "unix_time":unix_time,

        "merch_lat":merch_lat,

        "merch_long":merch_long,

        "hour":hour,

        "day":day,

        "month":month

    }])
    # Scale Features

    input_scaled = scaler.transform(input_df)

    # Prediction

    prediction = model.predict(input_scaled)[0]

    probability = model.predict_proba(input_scaled)[0][1]

    legitimate_probability = 1 - probability
        # =====================================
    # Prediction Result
    # =====================================

    st.divider()

    st.subheader("📊 Prediction Result")

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected")
    else:
        st.success("✅ Legitimate Transaction")

    st.write("")

    # =====================================
    # Metrics
    # =====================================

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Fraud Probability",
            f"{probability*100:.2f}%"
        )

    with col2:
        st.metric(
            "Legitimate Probability",
            f"{legitimate_probability*100:.2f}%"
        )

    confidence = max(probability, legitimate_probability)

    with col3:
        st.metric(
            "Prediction Confidence",
            f"{confidence*100:.2f}%"
        )

    st.write("")

    # =====================================
    # Fraud Risk Meter
    # =====================================

    st.subheader("📈 Fraud Risk")

    st.progress(float(probability))

    # =====================================
    # Risk Level
    # =====================================

    if probability < 0.20:

        st.success("🟢 Risk Level : LOW")

    elif probability < 0.50:

        st.warning("🟡 Risk Level : MEDIUM")

    elif probability < 0.80:

        st.warning("🟠 Risk Level : HIGH")

    else:

        st.error("🔴 Risk Level : CRITICAL")

    # =====================================
    # Transaction Summary
    # =====================================

    st.divider()

    st.subheader("📝 Transaction Details")

    display_df = pd.DataFrame({

        "Feature":[
            "Merchant",
            "Category",
            "Amount",
            "Gender",
            "State",
            "Job",
            "City Population",
            "Latitude",
            "Longitude",
            "Merchant Latitude",
            "Merchant Longitude",
            "Transaction Date",
            "Transaction Time"
        ],

        "Value":[
            merchant,
            category,
            f"${amt:.2f}",
            gender,
            state,
            job,
            city_pop,
            lat,
            long,
            merch_lat,
            merch_long,
            selected_date,
            selected_time
        ]

    })

    st.dataframe(
        display_df,
        use_container_width=True,
        hide_index=True
    )

    # =====================================
    # Final Decision
    # =====================================

    st.divider()

    if prediction == 1:

        st.error(
            """
### 🚨 Fraud Alert

The transaction appears **highly suspicious** based on the trained XGBoost model.

**Recommendation**

- Block the transaction temporarily.
- Verify customer identity.
- Contact the customer before approval.
            """
        )

    else:

        st.success(
            """
### ✅ Safe Transaction

The transaction appears **legitimate** according to the trained model.

**Recommendation**

- Transaction can be processed normally.
            """
        )


# =====================================
# Dataset Information
# =====================================

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📄 Dataset : Credit Card Transactions")

with col2:
    st.info("🤖 Algorithm : XGBoost")

with col3:
    st.info("🎯 Task : Binary Classification")

for key in ["unix_time", "hour", "day", "month"]:
    st.session_state.pop(key, None)
# =====================================
# Footer
# =====================================

st.divider()

