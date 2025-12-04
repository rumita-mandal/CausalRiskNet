features = ["age", "bmi", "sodium_intake", "steps", "sleep_hours"]
X = data[features]
treatment = data["treatment"]
y = data["disease_risk"]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
