import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs2.csv"  # change if needed
VARIANT = "A"

df = pd.read_csv(CSV_FILE)

df = df[df["variant"] == VARIANT]

run_means = df.groupby(["run", "generation"])["fitness"].mean().reset_index()
summary = run_means.groupby("generation")["fitness"].agg(["mean", "std"]).reset_index()

x = summary["generation"] + 1
y = summary["mean"]

plt.figure(figsize=(10, 6))

plt.plot(x, y, linewidth=3, marker="o", label="Low frequency CPG (0.05)")



plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.title("Evolution Improves Locomotion in the Low-Frequency Variant")
plt.grid(True, linestyle="--", alpha=0.4)
plt.legend()
plt.tight_layout()
plt.show()