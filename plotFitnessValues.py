"""
import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs2.csv"

df = pd.read_csv(CSV_FILE)

# Debug check: each run should have both A and B
print(df.groupby(["run", "variant"]).size())

runs = sorted(df["run"].unique())

for run in runs:

    A_data = df[(df["run"] == run) & (df["variant"] == "A")]
    A_mean = A_data.groupby("generation")["fitness"].mean()

    plt.plot(A_mean.index, A_mean.values, linewidth=1)
    plt.text(A_mean.index[-1], A_mean.values[-1], f"A{run}", fontsize=8)

    B_data = df[(df["run"] == run) & (df["variant"] == "B")]
    B_mean = B_data.groupby("generation")["fitness"].mean()

    plt.plot(B_mean.index, B_mean.values, linewidth=3)
    plt.text(B_mean.index[-1], B_mean.values[-1], f"B{run}", fontsize=8)

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("A/B Testing: One Line Per Run")
plt.legend()
plt.show()
"""
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

CSV_FILE = "fitness_all_runs15GEN.csv"

df = pd.read_csv(CSV_FILE)

run_means = df.groupby(["variant", "run", "generation"])["fitness"].mean().reset_index()

plt.figure(figsize=(10, 6))

for variant in ["A", "B"]:
    variant_data = run_means[run_means["variant"] == variant]

    color = "blue" if variant == "A" else "orange"
    linewidth = 1.2 if variant == "A" else 2.2
    alpha = 0.25

    for run in sorted(variant_data["run"].unique()):
        data = variant_data[variant_data["run"] == run]
        x = data["generation"] + 1
        y = data["fitness"]

        plt.plot(x, y, color=color, linewidth=linewidth, alpha=alpha)

legend_elements = [
    Line2D([0], [0], color="blue", lw=2, label="Low frequency (0.05) runs"),
    Line2D([0], [0], color="orange", lw=3, label="High frequency (100) runs")
]

plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("A/B Testing: One Line Per Run")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend(handles=legend_elements)
plt.tight_layout()
plt.show()