causal_model.fit(
    X=X_scaled,
    treatment=treatment.values,
    y=y.values
)

print("Causal Model Training Complete.")
