
import os
import csv
import constants as c
from parallelHillClimber import PARALLEL_HILL_CLIMBER

CSV_FILE = "fitness_all_runs.csv"
RUNS_PER_EXECUTION = 5  # change this to 10, 20, etc.


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


for i in range(RUNS_PER_EXECUTION):
    run_number = get_next_run_number()

    print("Starting A/B run", run_number)

    # Run A
    c.frequency = 0.05
    phcA = PARALLEL_HILL_CLIMBER()
    phcA.Evolve()

    # Run B
    c.frequency = 100
    phcB = PARALLEL_HILL_CLIMBER()
    phcB.Evolve()

    # Save only after both complete
    save_matrix_to_csv(phcA.fitnessMatrix, "A", 0.05, run_number)
    save_matrix_to_csv(phcB.fitnessMatrix, "B", 100, run_number)

    print("Saved complete A/B run", run_number)

print("Finished all runs.")
"""
import os
from parallelHillClimber import PARALLEL_HILL_CLIMBER

"""#for i in range(5):
    #os.system("python3 generate.py")
    #os.system("python3 simulate.py")
"""
phc = PARALLEL_HILL_CLIMBER()
phc.Evaluate(phc.parents)
phc.Show_Best()
phc.Evolve() 
phc.Show_Best()
"""