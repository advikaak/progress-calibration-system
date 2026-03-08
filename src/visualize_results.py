import csv
import matplotlib.pyplot as plt


def load_results(file_path):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


def create_alignment_chart(results, output_path):
    names = [row["name"] for row in results]
    alignment_scores = [int(row["alignment_score"]) for row in results]

    plt.figure(figsize=(10, 6))
    plt.bar(names, alignment_scores)
    plt.title("Alignment Scores by Student")
    plt.xlabel("Student")
    plt.ylabel("Alignment Score")
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()


if __name__ == "__main__":
    results = load_results("results/progress_analysis_results.csv")
    create_alignment_chart(results, "results/alignment_scores_chart.png")
    print("Chart saved to results/alignment_scores_chart.png")