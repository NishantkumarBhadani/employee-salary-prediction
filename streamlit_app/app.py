import streamlit as st
import pandas as pd
import joblib

# Load model and columns
model = joblib.load("models/salary_model.pkl")
model_columns = joblib.load("models/model_columns.pkl")

# Title and layout
st.set_page_config(page_title="Employee Income Predictor", layout="centered")
st.markdown("## 💼 Employee Income Prediction App")
st.markdown("Fill out the form below to predict if an employee earns more than 50K.")

# Use a form to group input fields
with st.form("prediction_form"):
    st.markdown("### 📋 Input Employee Information")

    # Split into two columns
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("Age", min_value=18, max_value=100, step=1)
        education_num = st.number_input("Education Number", min_value=1, max_value=20, step=1)
        hours_per_week = st.number_input("Hours per Week", min_value=1, max_value=100, step=1)
        capital_gain = st.number_input("Capital Gain", min_value=0, step=1)
        capital_loss = st.number_input("Capital Loss", min_value=0, step=1)

    with col2:
        workclass = st.selectbox("Workclass", [
            "Federal-gov", "Local-gov", "Private", "Self-emp-inc",
            "Self-emp-not-inc", "State-gov", "Without-pay"
        ])

        marital_status = st.selectbox("Marital Status", [
            "Divorced", "Married-AF-spouse", "Married-civ-spouse",
            "Married-spouse-absent", "Never-married", "Separated", "Widowed"
        ])

        occupation = st.selectbox("Occupation", [
            "Adm-clerical", "Armed-Forces", "Craft-repair", "Exec-managerial",
            "Farming-fishing", "Handlers-cleaners", "Machine-op-inspct",
            "Other-service", "Priv-house-serv", "Prof-specialty", "Protective-serv",
            "Sales", "Tech-support", "Transport-moving"
        ])

        relationship = st.selectbox("Relationship", [
            "Husband", "Not-in-family", "Other-relative", "Own-child", "Unmarried", "Wife"
        ])

        race = st.selectbox("Race", [
            "Amer-Indian-Eskimo", "Asian-Pac-Islander", "Black", "Other", "White"
        ])

        gender = st.selectbox("Gender", ["Female", "Male"])

        native_country = st.selectbox("Native Country", [
            "Cambodia", "Canada", "China", "Columbia", "Cuba", "Dominican-Republic",
            "Ecuador", "El-Salvador", "England", "France", "Germany", "Greece",
            "Guatemala", "Haiti", "Holand-Netherlands", "Honduras", "Hong", "Hungary",
            "India", "Iran", "Ireland", "Italy", "Jamaica", "Japan", "Laos", "Mexico",
            "Nicaragua", "Outlying-US(Guam-USVI-etc)", "Peru", "Philippines", "Poland",
            "Portugal", "Puerto-Rico", "Scotland", "South", "Taiwan", "Thailand",
            "Trinadad&Tobago", "United-States", "Vietnam", "Yugoslavia"
        ])

    # Submit button
    submitted = st.form_submit_button("🔮 Predict Income")

    if submitted:
        # Input DataFrame
        raw_input = pd.DataFrame([{
            'age': age,
            'educational-num': education_num,
            'hours-per-week': hours_per_week,
            'capital-gain': capital_gain,
            'capital-loss': capital_loss,
            'workclass': workclass,
            'marital-status': marital_status,
            'occupation': occupation,
            'relationship': relationship,
            'race': race,
            'gender': gender,
            'native-country': native_country
        }])

        # One-hot encoding and alignment
        input_df = pd.get_dummies(raw_input)
        for col in model_columns:
            if col not in input_df:
                input_df[col] = 0
        input_df = input_df[model_columns]

        # Prediction
        prediction = model.predict(input_df)[0]
        result = ">50K" if prediction == 1 else "<=50K"
        st.success(f"🎯 **Predicted Income:** {result}")
