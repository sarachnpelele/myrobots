import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs2.csv"

df = pd.read_csv(CSV_FILE)

# Best solution in each run/generation
best_per_run = df.groupby(["variant", "run", "generation"])["fitness"].max().reset_index()

# Average the best values across runs
best_summary = best_per_run.groupby(["variant", "generation"])["fitness"].agg(["mean", "std"]).reset_index()

plt.figure(figsize=(10, 6))

for variant in ["A", "B"]:
    data = best_summary[best_summary["variant"] == variant].copy()

    x = data["generation"] + 1

    y = data["mean"]
    y_shifted = y - y.iloc[0]

    label = "Low frequency (0.05)" if variant == "A" else "High frequency (100)"

    plt.plot(
        x,
        y_shifted,
        linewidth=3,
        marker="o",
        label=label
    )

    plt.fill_between(
        x,
        y_shifted - data["std"],
        y_shifted + data["std"],
        alpha=0.1
    )

plt.xlabel("Generation")
plt.ylabel("Change in Best Fitness")
plt.title("Best Fitness Across Generations")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()