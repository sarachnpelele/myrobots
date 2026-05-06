import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs2.csv"

# Read CSV
df = pd.read_csv(CSV_FILE)

# Average across solutions within each run/generation
run_means = df.groupby(
    ["variant", "run", "generation"]
)["fitness"].mean().reset_index()

# Average across runs for each variant/generation
summary = run_means.groupby(
    ["variant", "generation"]
)["fitness"].agg(["mean", "std"]).reset_index()

plt.figure(figsize=(10, 6))

for variant in ["A", "B"]:

    data = summary[summary["variant"] == variant].copy()

    # Generations start at 1 instead of 0
    x = data["generation"] + 1

    # Mean fitness
    y = data["mean"]

    # Smooth curve using rolling average
    y_smooth = y.rolling(window=3, min_periods=1).mean()

    label = (
        "Low frequency (0.05)"
        if variant == "A"
        else "High frequency (100)"
    )

    # Plot smooth mean line
    plt.plot(
        x,
        y_smooth,
        linewidth=3,
        marker="o",
        label=label
    )
    """
    # Plot standard deviation shading
    plt.fill_between(
        x,
        y - data["std"],
        y + data["std"],
        alpha=0.15
    )
    """

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("Evolution Improves Locomotion Over Generations")

plt.grid(True, linestyle="--", alpha=0.4)

plt.legend()

plt.tight_layout()

plt.show()