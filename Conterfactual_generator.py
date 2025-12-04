def generate_counterfactual(person_idx, sodium_reduce_pct=0.20):
    person = X.iloc[person_idx].copy()

    # Current predicted risk
    current_risk = causal_model.control_learner.predict(
        [scaler.transform([person])[0]]
    )[0]
    person_cf = person.copy()
    person_cf["sodium_intake"] *= (1 - sodium_reduce_pct)
    cf_risk = causal_model.control_learner.predict(
        [scaler.transform([person_cf])[0]]
    )[0]

    return current_risk, cf_risk
