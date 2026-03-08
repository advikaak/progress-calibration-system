import streamlit as st
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))
from progress_model import ProgressModel

st.set_page_config(page_title="Progress Calibration System", layout="centered")

st.title("Progress Calibration System")
st.write(
    "This tool helps users evaluate progress using actions, outcomes, comparison exposure, and time horizon."
)

actions_completed = st.number_input("Actions completed", min_value=0, value=5)
goals_completed = st.number_input("Goals completed", min_value=0, value=2)
comparison_exposure = st.number_input("Comparison exposure", min_value=0, value=3)
time_horizon_weeks = st.number_input("Time horizon (weeks)", min_value=1, value=4)

if st.button("Analyze Progress"):
    model = ProgressModel(
        actions_completed=actions_completed,
        goals_completed=goals_completed,
        comparison_exposure=comparison_exposure,
        time_horizon_weeks=time_horizon_weeks,
    )

    st.subheader("Results")
    st.write(f"**Process Score:** {model.calculate_process_score()}")
    st.write(f"**Outcome Score:** {model.calculate_outcome_score()}")
    st.write(f"**Time Horizon Score:** {model.calculate_time_horizon_score()}")
    st.write(f"**Alignment Score:** {model.calculate_alignment_score()}")
    st.write(f"**Distortion Risk:** {model.get_distortion_risk()}")
    st.write(f"**Progress Status:** {model.get_progress_status()}")