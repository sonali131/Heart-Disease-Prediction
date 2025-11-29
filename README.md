# 🫀 Heart Disease Prediction

<!-- Badges -->

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit)
![Machine Learning](https://img.shields.io/badge/ML-Model-green?logo=scikitlearn)

---

## 📸 App Screenshot

![App Screenshot]![alt text](<Screenshot 2025-11-29 123141.png>)
using Machine Learning
A simple and interactive **Streamlit web app** that predicts the risk of **heart disease** using a Machine Learning model.

---

## 🚀 Features

- Clean Streamlit UI
- ML Model trained on Heart Disease dataset
- Real-time prediction
- Uses `joblib` for model loading
- Deployable on Streamlit Cloud

---

## 📂 Project Structure

```
HEARTDISEASE/
│
├── app.py                 # Main Streamlit app
├── heart_columns.pkl      # One-hot encoded column list
├── heart_scaler.pkl       # Scaler used during model training
├── knn_heart_model.pkl    # Trained ML model (KNN)
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository

```
git clone https://github.com/your-username/heart-disease-prediction.git
cd heart-disease-prediction
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Run the app

```
streamlit run app.py
```

The app will open at:

```
http://localhost:8501
```

---

## 📦 requirements.txt

```
streamlit
pandas
numpy
scikit-learn
joblib
```

Optional:

```
matplotlib
seaborn
```

---

## 🤖 Model Training (Optional)

```python
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pandas as pd
import joblib

df = pd.read_csv("heart.csv")
X = df.drop("target", axis=1)
y = df["target"]

model = LogisticRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")
```

---

## 🌐 Deployment on Streamlit Cloud

1. Upload your code to GitHub
2. Go to https://share.streamlit.io
3. Select repository & branch
4. Make sure `requirements.txt` is present
5. Deploy 🎉

---

## 🧪 Inputs Used for Prediction

| Feature  | Description             |
| -------- | ----------------------- |
| Age      | Person's age            |
| Sex      | Gender                  |
| Cp       | Chest pain type         |
| Trestbps | Resting blood pressure  |
| Chol     | Cholesterol level       |
| Fbs      | Fasting blood sugar     |
| Restecg  | ECG results             |
| Thalach  | Max heart rate          |
| Exang    | Exercise induced angina |
| Oldpeak  | ST depression           |
| Slope    | Slope of ST             |
| Ca       | Number of vessels       |
| Thal     | Thalassemia             |

---

## 🟢 Output

- **0 → No Heart Disease**
- **1 → Heart Disease Detected**

---

## 👩‍💻 Developer

**Sonali Mishra**

---
