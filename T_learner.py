control_model = RandomForestRegressor(
    n_estimators=200, max_depth=6, random_state=42
)

treatment_model = RandomForestRegressor(
    n_estimators=200, max_depth=6, random_state=42
)

causal_model = BaseTRegressor(
    learner=treatment_model,
    control_learner=control_model
)
