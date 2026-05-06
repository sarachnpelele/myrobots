import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs2.csv"

df = pd.read_csv(CSV_FILE)

# Step 1: average across solutions (within each run)
run_means = df.groupby(["variant", "run", "generation"])["fitness"].mean().reset_index()

# Step 2: average across runs
summary = run_means.groupby(["variant", "generation"])["fitness"].agg(["mean", "std"]).reset_index()

plt.figure(figsize=(10, 6))

for variant in ["A", "B"]:
    data = summary[summary["variant"] == variant].copy()

    x = data["generation"] + 1

    y = data["mean"]

    label = "Low frequency (0.05)" if variant == "A" else "High frequency (100)"
    
    plt.plot(
        x,
        y,
        linewidth=3,
        marker='o',
        label=label
    )
    
    plt.fill_between(
        x,
        y - data["std"],
        y + data["std"],
        alpha=0.1
    )
    
plt.xlabel("Generation")
plt.ylabel("Change in Average Fitness")
plt.title("Effect of CPG Frequency on Locomotion Performance")
plt.grid(True, linestyle='--', alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()

