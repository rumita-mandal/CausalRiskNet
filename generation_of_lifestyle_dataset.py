N = 1000  # number of individuals

data = pd.DataFrame({
    "age": np.random.randint(25, 65, N),
    "bmi": np.random.uniform(18, 38, N),
    "sodium_intake": np.random.uniform(2, 10, N),   # grams/day
    "steps": np.random.randint(2000, 15000, N),
    "sleep_hours": np.random.uniform(4, 9, N),
})
data["treatment"] = np.random.binomial(1, 0.5, N)

# Disease Risk = function of lifestyle parameters + treatment
data["disease_risk"] = (
    0.25 * (data["bmi"] / 38) +
    0.25 * (data["sodium_intake"] / 10) -
    0.25 * (data["steps"] / 15000) -
    0.15 * (data["sleep_hours"] / 9) -
    0.12 * data["treatment"] +
    np.random.normal(0, 0.02, N)
)
