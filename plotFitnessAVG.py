import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("fitness_all_runs.csv")

# Step 1: average across solutions (within each run)
run_means = df.groupby(["variant", "run", "generation"])["fitness"].mean().reset_index()

# Step 2: average across runs
summary = run_means.groupby(["variant", "generation"])["fitness"].agg(["mean", "std"]).reset_index()

for variant in ["A", "B"]:
    data = summary[summary["variant"] == variant]

    plt.plot(
        data["generation"],
        data["mean"],
        linewidth=3,
        label=f"{variant} mean"
    )

    # shading = variability across runs
    plt.fill_between(
        data["generation"],
        data["mean"] - data["std"],
        data["mean"] + data["std"],
        alpha=0.2
    )

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("A/B Testing: Average Across Runs (Mean ± Std)")
plt.legend()
plt.show()