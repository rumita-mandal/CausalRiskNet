ite_values = causal_model.predict_ite(X_scaled)

data["ITE"] = ite_values
print(data.head())
