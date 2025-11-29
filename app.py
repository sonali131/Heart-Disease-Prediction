import streamlit as st
import pandas as pd
import joblib

# Page config
st.set_page_config(
    page_title="Heart Disease Predictor",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
    <style>
        .main {
            background-color: #f7f9fc;
        }
        .stButton>button {
            background-color: #ff4b4b;
            color: white;
            border-radius: 10px;
            width: 200px;
            height: 50px;
            font-size: 18px;
        }
        .stButton>button:hover {
            background-color: #e04343;
        }
        .card {
            padding: 25px;
            background-color: white;
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }
    </style>
""", unsafe_allow_html=True)

# Load saved model & data
model = joblib.load("knn_heart_model.pkl")
scaler = joblib.load("heart_scaler.pkl")
expected_columns = joblib.load("heart_columns.pkl")

# Title section
st.markdown("<h1 style='text-align:center;color:#d63031;'>❤️Heart Decision Prediction❤️</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;font-size:18px;'>Enter your details below to check your heart stroke risk instantly.</p>", unsafe_allow_html=True)
st.markdown("---")

# Main input area
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Organize inputs into 3 columns
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.slider("Age", 18, 100, 40)
        sex = st.selectbox("Sex", ["M", "F"])
        chest_pain = st.selectbox("Chest Pain Type", ["ATA", "NAP", "TA", "ASY"])
        resting_ecg = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])

    with col2:
        resting_bp = st.number_input("Resting BP (mm Hg)", 80, 200, 120)
        cholesterol = st.number_input("Cholesterol (mg/dL)", 100, 600, 200)
        fasting_bs = st.selectbox("Fasting Blood Sugar > 120 mg/dL", [0, 1])
        st_slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    with col3:
        max_hr = st.slider("Max Heart Rate", 60, 220, 150)
        exercise_angina = st.selectbox("Exercise-Induced Angina", ["Y", "N"])
        oldpeak = st.slider("Oldpeak (ST Depression)", 0.0, 6.0, 1.0)

    st.markdown("</div>", unsafe_allow_html=True)

# Predict button centered
st.markdown("<br>", unsafe_allow_html=True)
col_btn = st.columns(3)[1]

with col_btn:
    predict_clicked = st.button("💡 Predict Risk")

# Prediction logic
if predict_clicked:

    raw_input = {
        'Age': age,
        'RestingBP': resting_bp,
        'Cholesterol': cholesterol,
        'FastingBS': fasting_bs,
        'MaxHR': max_hr,
        'Oldpeak': oldpeak,
        'Sex_' + sex: 1,
        'ChestPainType_' + chest_pain: 1,
        'RestingECG_' + resting_ecg: 1,
        'ExerciseAngina_' + exercise_angina: 1,
        'ST_Slope_' + st_slope: 1
    }

    input_df = pd.DataFrame([raw_input])

    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    input_df = input_df[expected_columns]

    scaled_input = scaler.transform(input_df)
    prediction = model.predict(scaled_input)[0]

    st.markdown("---")

    # Display beautiful result
    if prediction == 1:
        st.error("🚨 **High Risk of Heart Disease Detected!**\nPlease consult a cardiologist immediately.")
        st.markdown("<h3 style='color:#e84118;text-align:center;'>⚠️ Take Action & Stay Safe!</h3>", unsafe_allow_html=True)

    else:
        st.success("🎉 **Your Heart Looks Healthy!**\nNo immediate risk detected.")
        st.markdown("<h3 style='color:#2ecc71;text-align:center;'>✔️ Keep up a healthy lifestyle!</h3>", unsafe_allow_html=True)
