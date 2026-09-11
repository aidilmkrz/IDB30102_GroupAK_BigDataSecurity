from anonymization_framework import PrivacyFramework

def run_experiment():
    dataset_path = "../05_Data_or_Sample_Input/adult.data"
    framework = PrivacyFramework(dataset_path)
    
    print("[1] Loading Baseline (Raw) Dataset...")
    framework.load_data()
    
    # 1. Baseline Evaluation
    baseline_acc = framework.evaluate_utility(framework.raw_data)
    baseline_risk = framework.calculate_reidentification_risk(
        framework.raw_data, framework.quasi_identifiers
    )
    
    print(f"Baseline Accuracy: {baseline_acc}% | Re-ID Risk: {baseline_risk}%")

    # 2. K-Anonymity Evaluation (k=3)
    print("\n[2] Executing K-Anonymity (k=3)...")
    k_df, k_time = framework.apply_k_anonymity(k=3)
    k_acc = framework.evaluate_utility(k_df)
    k_risk = framework.calculate_reidentification_risk(k_df, framework.quasi_identifiers)
    
    # 3. Differential Privacy Evaluation (epsilon=1.0)
    print("\n[3] Executing Differential Privacy (epsilon=1.0)...")
    dp_df, dp_time = framework.apply_differential_privacy(epsilon=1.0)
    dp_acc = framework.evaluate_utility(dp_df)
    dp_risk = framework.calculate_reidentification_risk(dp_df, framework.quasi_identifiers)

    # Output Final Results
    print("\n" + "="*50)
    print("EXPERIMENTAL EVALUATION SUMMARY")
    print("="*50)
    print(f"Baseline (Raw): Accuracy = {baseline_acc}%, Re-ID Risk = {baseline_risk}%, Time = 0.00 ms")
    print(f"K-Anonymity (k=3): Accuracy = {k_acc}%, Re-ID Risk = {k_risk}%, Time = {k_time:.2f} ms")
    print(f"Differential Privacy (e=1.0): Accuracy = {dp_acc}%, Re-ID Risk = {dp_risk}%, Time = {dp_time:.2f} ms")
    print("="*50)

if __name__ == "__main__":
    run_experiment()