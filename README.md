# 🧠 Employee Income Prediction (ML + Streamlit)

This project predicts whether an individual's income exceeds $50K/year based on U.S. Census data. It uses Random Forest machine learning model and a Streamlit web app for interactive predictions.

---

## 📁 Folder Structure

```
employee-salary-prediction/
├── data/
│   └── adult.csv                   # Raw dataset
├── models/
│   ├── salary_model.pkl           # Trained model (e.g. Random Forest)
│   └── model_columns.pkl          # Feature columns used during training
|
├── model_comparison.ipynb     # Jupyter notebook for training and evaluating models
│    
├── streamlit_app/
│   └── app.py                     # Streamlit app for live predictions
├── requirements.txt               # Required Python packages
└── README.md                      # Project documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/NishantkumarBhadani/employee-salary-prediction.git
cd employee-salary-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

> 💡 Don't have Streamlit installed? Use: `pip install streamlit`

---

### 3. Run the Streamlit app

```bash
streamlit run streamlit_app/app.py
```

---

## 💡 How It Works

- **Input**: Age, education, hours worked, job details, etc.
- **Process**: Model trained on `adult 3.csv` dataset classifies income as `<=50K` or `>50K`.
- **Output**: Real-time prediction in the Streamlit interface.

---

## 🧪 ML Models Used

- Logistic Regression
- Random Forest ✅ *(default model used in app)*
- Decision Tree
- Support Vector Machine (SVM)

Each model was trained and evaluated for accuracy. 

---

## 📊 Dataset

- Source: [UCI Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)
- Format: CSV
- Target Variable: `income` (binary classification)

---

## ✍️ Author

- **Nishant Kumar Bhadani**  
- GitHub: [@NishantkumarBhadani](https://github.com/NishantkumarBhadani)

---

## 📌 License

This project is open-source under the MIT License.
