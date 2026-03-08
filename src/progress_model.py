import csv


class ProgressModel:
    def __init__(self, actions_completed, goals_completed, comparison_exposure):
        self.actions_completed = actions_completed
        self.goals_completed = goals_completed
        self.comparison_exposure = comparison_exposure

    def calculate_process_score(self):
        return self.actions_completed * 10

    def calculate_outcome_score(self):
        return self.goals_completed * 20

    def calculate_alignment_score(self):
        process_score = self.calculate_process_score()
        outcome_score = self.calculate_outcome_score()
        alignment_score = process_score + outcome_score - (self.comparison_exposure * 5)
        return alignment_score

    def get_progress_status(self):
        score = self.calculate_alignment_score()

        if score >= 80:
            return "Strong progress"
        elif score >= 50:
            return "Moderate progress"
        else:
            return "Progress may feel low, but process needs more context"


def load_progress_data(file_path):
    with open(file_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)
        return list(reader)


if __name__ == "__main__":
    data = load_progress_data("data/sample_progress_data.csv")

    for row in data:
        model = ProgressModel(
            actions_completed=int(row["actions_completed"]),
            goals_completed=int(row["goals_completed"]),
            comparison_exposure=int(row["comparison_exposure"])
        )

        print(f"Name: {row['name']}")
        print("  Process Score:", model.calculate_process_score())
        print("  Outcome Score:", model.calculate_outcome_score())
        print("  Alignment Score:", model.calculate_alignment_score())
        print("  Progress Status:", model.get_progress_status())
        print()