def plot_counterfactual(original, counterfactual, title="Risk Change"):
    plt.figure(figsize=(6, 4))
    plt.plot(
        ["Current Lifestyle", "Counterfactual"],
        [original, counterfactual],
        marker="o",
        linewidth=3
    )
    plt.title(title)
    plt.ylabel("Predicted Disease Risk")
    plt.grid(True)
    plt.show()
