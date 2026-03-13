
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
df_d = pd.read_csv("diabetes_binary_health_indicators_BRFSS2015.csv")

diabetes_features = [
    "Age", "Sex", "BMI", "HighBP",
    "HighChol", "PhysActivity", "Smoker"
]

X_d = df_d[diabetes_features]
y_d = df_d["Diabetes_binary"]

X_train, X_test, y_train, y_test = train_test_split(
    X_d, y_d, test_size=0.2, random_state=42, stratify=y_d
)

scaler_d = StandardScaler()
X_train = scaler_d.fit_transform(X_train)

diabetes_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)
diabetes_model.fit(X_train, y_train)


df_h = pd.read_csv("heart.csv")

heart_features = [
    "age", "sex", "cp", "trestbps",
    "chol", "thalach", "exang"
]

X_h = df_h[heart_features]
y_h = df_h["target"]

X_train, X_test, y_train, y_test = train_test_split(
    X_h, y_h, test_size=0.2, random_state=42, stratify=y_h
)

scaler_h = StandardScaler()
X_train = scaler_h.fit_transform(X_train)

heart_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)
heart_model.fit(X_train, y_train)



df_k = pd.read_csv("kidney_disease.csv")
df_k.replace("?", np.nan, inplace=True)
df_k.dropna(inplace=True)

df_k["classification"] = df_k["classification"].map({
    "ckd": 1,
    "notckd": 0
})

kidney_features = ["age", "bp", "al", "bu", "sc", "hemo"]

X_k = df_k[kidney_features]
y_k = df_k["classification"]

X_train, X_test, y_train, y_test = train_test_split(
    X_k, y_k, test_size=0.2, random_state=42, stratify=y_k
)

scaler_k = StandardScaler()
X_train = scaler_k.fit_transform(X_train)

kidney_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)
kidney_model.fit(X_train, y_train)



print("\n===== ENTER USER DETAILS =====\n")

age = int(input("Enter Age: "))
sex = int(input("Enter Sex (1=Male, 0=Female): "))
bmi = float(input("Enter BMI: "))
highbp = int(input("High Blood Pressure? (1=Yes, 0=No): "))
highchol = int(input("High Cholesterol? (1=Yes, 0=No): "))
phys = int(input("Physically Active? (1=Yes, 0=No): "))
smoker = int(input("Smoker? (1=Yes, 0=No): "))

cp = int(input("Chest Pain Type (0–3): "))
trestbps = int(input("Resting BP: "))
chol = int(input("Cholesterol: "))
thalach = int(input("Max Heart Rate: "))
exang = int(input("Exercise Induced Angina (1=Yes,0=No): "))

bp = int(input("Blood Pressure: "))
al = int(input("Albumin (0–5): "))
bu = float(input("Blood Urea: "))
sc = float(input("Serum Creatinine: "))
hemo = float(input("Hemoglobin: "))


# ---------- PREDICTIONS ----------

# Diabetes
diab_input = scaler_d.transform([[
    age, sex, bmi, highbp,
    highchol, phys, smoker
]])
diab_prob = diabetes_model.predict_proba(diab_input)[0][1]

# Heart
heart_input = scaler_h.transform([[
    age, sex, cp, trestbps,
    chol, thalach, exang
]])
heart_prob = heart_model.predict_proba(heart_input)[0][1]

# Kidney
kidney_input = scaler_k.transform([[
    age, bp, al, bu, sc, hemo
]])
kidney_prob = kidney_model.predict_proba(kidney_input)[0][1]



def risk_level(p):
    if p >= 0.7:
        return "HIGH RISK"
    elif p >= 0.4:
        return "MODERATE RISK"
    else:
        return "LOW RISK"


print("\n===== PREDICTION RESULTS =====\n")
print("Diabetes Risk:", risk_level(diab_prob))
print("Heart Disease Risk:", risk_level(heart_prob))
print("Kidney Disease Risk:", risk_level(kidney_prob))


print("\n===== GENERAL GUIDANCE =====\n")
print("• Maintain healthy diet and lifestyle")
print("• Regular physical activity recommended")
print("• Consult a doctor if risk is MODERATE or HIGH")

print("\nDISCLAIMER: This system provides early risk awareness only and does not replace professional medical diagnosis.\n")