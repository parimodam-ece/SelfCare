import streamlit as st

st.set_page_config(page_title="Self-Care Assessment", layout="centered")

# -----------------------------
# SESSION STATE
# -----------------------------
if "q_index" not in st.session_state:
    st.session_state.q_index = 0

if "responses" not in st.session_state:
    st.session_state.responses = {}

# -----------------------------
# STYLE
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background-color: #C8F7E5;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TITLE
# -----------------------------
st.title("🌿 Self-Care Assessment Tool 🌿")

st.markdown("""
Reflect on your self-care across different areas of your life.

### Scale
1 = Never  
2 = Rarely  
3 = Sometimes  
4 = Often  
5 = Always  
""")

# -----------------------------
# QUESTION SET (WITH ICONS)
# -----------------------------
categories = {

"💪 Physical Self-Care": [
"Eat regularly",
"Eat a balanced diet",
"Exercise regularly",
"Get enough sleep",
"Take breaks when sick",
"Take vacations",
"Reduce screen/stress time"
],

"🧠 Psychological Self-Care": [
"Self-reflection",
"Keep a journal",
"Learn new things",
"Manage stress",
"Set boundaries",
"Spend time outdoors"
],

"💛 Emotional Self-Care": [
"Spend time with loved ones",
"Treat yourself kindly",
"Express emotions",
"Do things that make you happy",
"Laugh often"
],

"🌿 Spiritual Self-Care": [
"Spend time in nature",
"Meditation or prayer",
"Express gratitude",
"Reflect on meaning and purpose",
"Engage in inspiring activities"
],

"🏢 Workplace Self-Care": [
"Take breaks at work",
"Manage workload",
"Set boundaries at work",
"Ask for support",
"Maintain work-life balance"
]

}

# Flatten questions
all_questions = []
for category, questions in categories.items():
    for q in questions:
        all_questions.append((category, q))

total_questions = len(all_questions)

# -----------------------------
# PROGRESS
# -----------------------------
st.progress(st.session_state.q_index / total_questions)
st.write(f"Question {st.session_state.q_index + 1} of {total_questions}")

# -----------------------------
# TXT REPORT FUNCTION
# -----------------------------
def create_txt_report():
    responses = st.session_state.responses

    total_score = sum(responses.values())
    max_score = len(all_questions) * 5
    percentage = (total_score / max_score) * 100

    report = []

    report.append("SELF-CARE ASSESSMENT REPORT")
    report.append("=" * 50 + "\n")

    report.append(f"Total Score: {total_score}/{max_score}")
    report.append(f"Overall Score: {percentage:.1f}%\n")

    if percentage < 40:
        report.append("Level: Low self-care (risk of burnout)\n")
    elif percentage < 70:
        report.append("Level: Moderate self-care\n")
    else:
        report.append("Level: Strong self-care\n")

    report.append("\nDETAILED RESPONSES")
    report.append("=" * 50 + "\n")

    for category, questions in categories.items():
        report.append(f"\n{category}")
        report.append("-" * len(category))

        for q in questions:
            answer = responses.get(q, "No response")
            report.append(f"{q}")
            report.append(f"Answer: {answer}\n")

    report.append("\nCATEGORY BREAKDOWN")
    report.append("=" * 50 + "\n")

    for category, questions in categories.items():
        cat_score = sum(responses.get(q, 0) for q in questions)
        cat_max = len(questions) * 5
        cat_percent = (cat_score / cat_max) * 100

        report.append(f"{category}")
        report.append(f"{cat_score}/{cat_max} ({cat_percent:.1f}%)\n")

    report.append("\nDISCLAIMER")
    report.append("This tool is for educational purposes only.")

    return "\n".join(report)

# -----------------------------
# MAIN FLOW
# -----------------------------
if st.session_state.q_index < total_questions:

    category, question = all_questions[st.session_state.q_index]

    st.subheader(category)
    st.write(question)

    response = st.radio(
        "Select your answer:",
        [1, 2, 3, 4, 5],
        horizontal=True,
        key=f"q_{st.session_state.q_index}"
    )

    st.session_state.responses[question] = response

    col1, col2 = st.columns(2)

    with col1:
        if st.session_state.q_index > 0:
            if st.button("⬅ Back"):
                st.session_state.q_index -= 1
                st.rerun()

    with col2:
        if st.button("Next ➡"):
            st.session_state.q_index += 1
            st.rerun()

# -----------------------------
# RESULTS SCREEN
# -----------------------------
else:

    responses = st.session_state.responses

    total_score = sum(responses.values())
    max_score = len(all_questions) * 5
    percentage = (total_score / max_score) * 100

    st.subheader("📊 Your Results")
    st.write(f"**Total Score:** {total_score}/{max_score}")
    st.write(f"**Self-Care Level:** {percentage:.1f}%")

    if percentage < 40:
        st.error("⚠️ Low self-care: Risk of burnout.")
    elif percentage < 70:
        st.warning("🟡 Moderate self-care: Room for improvement.")
    else:
        st.success("🟢 Strong self-care: Healthy self-care habits.")

    st.subheader("📌 Category Breakdown")

    for category, questions in categories.items():
        cat_score = sum(responses.get(q, 0) for q in questions)
        cat_max = len(questions) * 5
        cat_percent = (cat_score / cat_max) * 100

        st.write(f"**{category}:** {cat_score}/{cat_max} ({cat_percent:.1f}%)")

    # -----------------------------
    # DOWNLOAD TXT
    # -----------------------------
    st.download_button(
        label="📄 Download Full TXT Report",
        data=create_txt_report(),
        file_name="self_care_assessment.txt",
        mime="text/plain"
    )

    # -----------------------------
    # RESTART
    # -----------------------------
    if st.button("🔄 Restart Assessment"):
        st.session_state.q_index = 0
        st.session_state.responses = {}
        st.rerun()
