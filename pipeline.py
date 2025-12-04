def run_pipeline_for_user(user_idx, sodium_reduction=0.3):
    print("Running Causal Counterfactual Pipeline...\n")

    orig, cf = generate_counterfactual(
        user_idx,
        sodium_reduce_pct=sodium_reduction
    )

    print(f"Original Risk: {orig:.4f}")
    print(f"Counterfactual Risk: {cf:.4f}")
    print(f"Risk Reduction: {orig - cf:.4f}")

    plot_counterfactual(orig, cf, title="Sodium Reduction Counterfactual")
