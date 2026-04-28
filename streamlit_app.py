import streamlit as st

st.title("🌿 Self-Care Assessment Tool")
st.write("""
This tool aims to:

1- Promote self-awareness and reflection.
2- Support holistic wellbeing.
3- Encourage individuals to identify areas for growth in self-care.
4- Align with holistic approaches to wellbeing in education and professional practice.

Self-assessment is an important reflective process that helps individuals understand their strengths and areas for improvement and supports self-directed learning.
Reflect on each statement and select how often it applies to your current lifestyle.
### Scale:
1 = It has never occurred to me  
2 = Never  
3 = Sometimes  
4 = Fairly Often  
5 = Frequently  
""")
# -----------------------------
# FULL QUESTION SET
# -----------------------------
categories = {

"Physical Self-Care": [
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

"Psychological Self-Care": [
"Make time for self-reflection",
"Go to see a psychotherapist or counsellor for yourself",
"Keep a journal",
"Read literature unrelated to work",
"Do something at which you are a beginner",
"Take a step to decrease stress in your life",
"Notice your inner experience (dreams, thoughts, feelings)",
"Let others know different aspects of you",
"Engage your intelligence in a new area",
"Be curious",
"Say no to extra responsibilities sometimes",
"Spend time outdoors"
],

"Emotional Self-Care": [
"Spend time with others whose company you enjoy",
"Stay in contact with important people",
"Treat yourself kindly (self-talk)",
"Feel proud of yourself",
"Reread favourite books or movies",
"Seek comforting activities, people, places",
"Allow yourself to cry",
"Find things that make you laugh",
"Express your outrage constructively",
"Play with children"
],

"Spiritual Self-Care": [
"Make time for prayer, meditation, reflection",
"Spend time in nature",
"Participate in a spiritual community",
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

"Workplace / Professional Self-Care": [
"Take time to eat lunch",
"Take time to chat with co-workers",
"Make time to complete tasks",
"Do work that promotes growth",
"Set limits with clients and colleagues",
"Balance workload",
"Arrange a comfortable workspace",
"Get supervision and consultation",
"Negotiate for your needs",
"Have a peer support group"
]

}

responses = {}

# -----------------------------
# INPUT SECTION
# -----------------------------
for category, questions in categories.items():
    st.subheader(category)
    for q in questions:
        responses[q] = st.radio(
            q,
            [1, 2, 3, 4, 5],
            horizontal=True,
            key=q
        )

# -----------------------------
# RESULTS
# -----------------------------
if st.button("📊 Calculate My Results"):

    total_score = sum(responses.values())
    max_score = len(responses) * 5
    percentage = (total_score / max_score) * 100

    st.subheader("📊 Your Results")
    st.write(f"**Total Score:** {total_score} / {max_score}")
    st.write(f"**Overall Self-Care Level:** {percentage:.1f}%")

    # Interpretation
    if percentage < 40:
        st.error("⚠️ Low self-care: You may be at risk of burnout. Start with small, manageable steps.")
    elif percentage < 70:
        st.warning("🟡 Moderate self-care: You are practicing some strategies, but there is room to grow.")
    else:
        st.success("🟢 Strong self-care: You are maintaining healthy and consistent self-care practices.")

    # -----------------------------
    # CATEGORY BREAKDOWN
    # -----------------------------
    st.subheader("📌 Category Breakdown")

    for category, questions in categories.items():
        cat_score = sum(responses[q] for q in questions)
        cat_max = len(questions) * 5
        cat_percent = (cat_score / cat_max) * 100

        st.write(f"**{category}:** {cat_score}/{cat_max} ({cat_percent:.1f}%)")





    # -----------------------------
    # REFLECTION (important for your course)
    # -----------------------------
    st.subheader("⚠️ Disclaimer")
st.write("""
This tool is intended for educational and reflective purposes only.
It is not a diagnostic or clinical assessment.
""")
   # reflection = st.text_area(
   #     "What is ONE small action you will take this week to improve your self-care?"
  #  )

#    if reflection:
 #       st.success("Small steps lead to meaningful change 💚")
