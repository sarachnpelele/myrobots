import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "fitness_all_runs.csv"

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