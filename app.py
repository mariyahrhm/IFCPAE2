import os
import pandas as pd
import streamlit as st
from datetime import datetime

APP_FOLDER = os.path.dirname(os.path.abspath(__file__))
QUESTIONS_FILE = os.path.join(APP_FOLDER, "questions.csv")
RESULTS_FILE = os.path.join(APP_FOLDER, "results.csv")


def load_questions():
    # encoding avoids common Windows CSV quirks (BOM)
    return pd.read_csv(QUESTIONS_FILE, encoding="utf-8-sig")


def save_result(score, total, percentage):
    new_row = pd.DataFrame([{
        "timestamp": datetime.now().isoformat(timespec="seconds"),
        "score": score,
        "total": total,
        "percentage": percentage
    }])

    try:
        existing = pd.read_csv(RESULTS_FILE)
        combined = pd.concat([existing, new_row], ignore_index=True)
    except (FileNotFoundError, pd.errors.EmptyDataError):
        combined = new_row

    combined.to_csv(RESULTS_FILE, index=False)


# ---------------- Streamlit App ----------------

st.title("Ethics Quiz: Decision‑Making🤷‍♀️❓")

questions = load_questions()
total_questions = len(questions)


if "current_q" not in st.session_state:
    st.session_state.current_q = 0
    st.session_state.score = 0

# Progress bar 
progress = st.session_state.current_q / total_questions if total_questions else 0
st.progress(progress)
st.caption(f"Progress: {st.session_state.current_q} / {total_questions}")

# Finished screen
if st.session_state.current_q >= total_questions:
    percentage = round((st.session_state.score / total_questions) * 100, 1) if total_questions else 0.0

    # evaluating score at end
    if percentage >= 80:
        st.balloons()
        st.success("🌟 Amazing! You’re an Ethics Champion!")
    elif percentage >= 60:
        st.success("✅ Nice work! Solid ethical judgement.")
    else:
        st.info("🧩 Good effort! Try again and see if you can beat your score.")

    st.write(f"**Final score:** {st.session_state.score} / {total_questions}")
    st.write(f"**Percentage:** {percentage}%")

    # Adding fun “badge” system
    if percentage >= 80:
        st.write("🏅 Badge earned: **Ethics Champion**")
    elif percentage >= 60:
        st.write("🎖️ Badge earned: **Good Judgement**")
    else:
        st.write("🎯 Badge earned: **Getting Started**")

    # Save results
    save_result(st.session_state.score, total_questions, percentage)

    st.divider()
    st.subheader("Play again?")
    if st.button("Restart quiz"):
        st.session_state.current_q = 0
        st.session_state.score = 0
        st.rerun()

    st.stop()

# Get the current question from the CSV 
row = questions.iloc[st.session_state.current_q]

st.subheader(f"Question {st.session_state.current_q + 1} of {total_questions}")
st.write(row["question"])

answer = st.radio(
    "Choose one:",
    [row["a"], row["b"], row["c"], row["d"]],
    key=f"q_{st.session_state.current_q}"
)

# Next button
if st.button("Next"):
    if answer.strip() == str(row["correct"]).strip():
        st.session_state.score += 1

    st.session_state.current_q += 1
    st.rerun()