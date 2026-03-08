import csv


class ProgressModel:
    def __init__(self, actions_completed, goals_completed, comparison_exposure, time_horizon_weeks):
        self.actions_completed = actions_completed
        self.goals_completed = goals_completed
        self.comparison_exposure = comparison_exposure
        self.time_horizon_weeks = time_horizon_weeks

    def calculate_process_score(self):
        return self.actions_completed * 10

    def calculate_outcome_score(self):
        return self.goals_completed * 20

    def calculate_time_horizon_score(self):
        return self.time_horizon_weeks * 2

    def calculate_alignment_score(self):
        process_score = self.calculate_process_score()
        outcome_score = self.calculate_outcome_score()
        time_horizon_score = self.calculate_time_horizon_score()

        alignment_score = process_score + outcome_score + time_horizon_score - (self.comparison_exposure * 5)
        return alignment_score
    
    def get_distortion_risk(self):
        if self.comparison_exposure >= 7 and self.time_horizon_weeks <= 2:
            return "High distortion risk"
        elif self.comparison_exposure >= 4 and self.time_horizon_weeks <= 4:
            return "Moderate distortion risk"
        else:
            return "Low distortion risk"

    def get_progress_status(self):
        score = self.calculate_alignment_score()

        if score >= 90:
            return "Strong progress"
        elif score >= 60:
            return "Moderate progress"
        else:
            return "Progress may feel low, but the current time horizon may be too short"


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
            comparison_exposure=int(row["comparison_exposure"]),
            time_horizon_weeks=int(row["time_horizon_weeks"])
        )

        print(f"Name: {row['name']}")
        print("  Process Score:", model.calculate_process_score())
        print("  Outcome Score:", model.calculate_outcome_score())
        print("  Time Horizon Score:", model.calculate_time_horizon_score())
        print("  Alignment Score:", model.calculate_alignment_score())
        print("  Distortion Risk:", model.get_distortion_risk())
        print("  Progress Status:", model.get_progress_status())
        print()