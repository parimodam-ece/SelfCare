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
        /* Force all text elements to black */
    p, span, label, div, h1, h2, h3 {
        color: black !important;
    }

    /* Streamlit-specific overrides */
    .stRadio label {
        color: black !important;
    }

    .stMarkdown {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# TITLE
# -----------------------------
st.title(" Self-Care Assessment Tool ")

st.markdown("""
This tool aims to:

1. Promote self-awareness and reflection  
2. Support holistic wellbeing  
3. Encourage individuals to identify areas for growth in self-care  
4. Align with holistic approaches to wellbeing in education and professional practice  

This self-care assessment is adapted from the following resource:  
[Self-Care Assessment Tool](https://rise.articulate.com/share/i3RuAxAmlt3AIEi5QS1Fyasu-JYib9LT)  


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
"Eat regularly (e.g. breakfast & lunch)",
"Eat a well balanced, healthy diet",
"Exercise at home or go to the gym",
"Lift weights",
"Practice martial arts",
"Get regular medical care for prevention of health problems",
"Get medical care when needed",
"Take time off when you're sick",
"Get massages to help reduce muscle tension",
"Do physical activity that is fun for you",
"Take time to be sexually intimate",
"Get enough sleep",
"Wear clothes you like",
"Take vacations",
"Take day trips or mini-vacations",
"Get away from stressful technology"
],

"🧠 Psychological Self-Care": [
"Make time for self-reflection",
"Go to see a psychotherapist or counsellor for yourself",
"Keep a journal",
"Read literature unrelated to work",
"Do something at which you are a beginner",
"Take a step to decrease stress in your life",
"Notice your inner experience (dreams, thoughts, feelings)",
"Let others know different aspects of you",
"Engage your intelligence in a new area, cultural activity, sports event, etc",
"Be curious",
"Say no to extra responsibilities sometimes",
"Spend time outdoors"
],

"💛 Emotional Self-Care": [
"Spend time with others whose company you enjoy",
"Stay in contact with important people in your life",
"Treat yourself kindly (supportive inner dialogue or self-talk)",
"Feel proud of yourself",
"Reread favourite books or re-watch favourite movies",
"Seek comforting activities, people, places",
"Allow yourself to cry",
"Find things that make you laugh",
"Express your outrage constructively",
"Play with children"
],

"🌿 Spiritual Self-Care": [
"Make time for prayer, meditation, reflection",
"Spend time in nature",
"Participate in a spiritual gathering, community or group",
"Be open to inspiration",
"Cherish optimism and hope",
"Be aware of intangible aspects of life",
"Be open to mystery",
"Identify what is meaningful to you",
"Sing",
"Express gratitude",
"Celebrate milestones meaningfully",
"Remember loved ones who passed away",
"Nurture others",
"Have 'awesome' experiences",
"Participate in causes you believe in",
"Read inspirational literature",
"Listen to inspiring music"
],

"🏢 Workplace Self-Care": [
"Take time to eat lunch",
"Take time to chat with co-workers",
"Make time to complete tasks",
"Identify tasks that are exciting and rewarding and promote growth",
"Set limits with clients and colleagues",
"Balance workload",
"Arrange your workplace so it is comfortable and comforting",
"Get regular supervision and consultation",
"Negotiate for your needs",
"Have a peer support group"
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
