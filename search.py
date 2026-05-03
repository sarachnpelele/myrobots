import os
import csv
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER

CSV_FILE = "fitness_all_runs.csv"


def get_next_run_number():
    if not os.path.exists(CSV_FILE):
        return 0

    run_numbers = []

    with open(CSV_FILE, "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            run_numbers.append(int(row["run"]))

    if len(run_numbers) == 0:
        return 0

    return max(run_numbers) + 1


def save_matrix_to_csv(matrix, variant, frequency, run_number):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, "a", newline="") as f:
        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["run", "variant", "frequency", "solution", "generation", "fitness"])

        for solution in range(matrix.shape[0]):
            for generation in range(matrix.shape[1]):
                writer.writerow([
                    run_number,
                    variant,
                    frequency,
                    solution,
                    generation,
                    matrix[solution, generation]
                ])


run_number = get_next_run_number()

# Run A first, but DO NOT save yet
c.frequency = 0.01
phcA = PARALLEL_HILL_CLIMBER()
phcA.Evolve()

# Run B second, but DO NOT save yet
c.frequency = 0.1
phcB = PARALLEL_HILL_CLIMBER()
phcB.Evolve()

# Only save after BOTH completed successfully
save_matrix_to_csv(phcA.fitnessMatrix, "A", 0.01, run_number)
save_matrix_to_csv(phcB.fitnessMatrix, "B", 0.1, run_number)

print("Saved complete A/B run", run_number)