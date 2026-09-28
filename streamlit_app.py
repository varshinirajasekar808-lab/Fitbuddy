import streamlit as st

st.set_page_config(
    page_title="FitBuddy",
    page_icon="💪",
    layout="wide"
)

st.title("💪 FitBuddy")
st.subheader("Your Simple Fitness & Wellness Companion")

st.write(
    "FitBuddy is a fitness and wellness web application designed to help "
    "users stay active and maintain a healthy lifestyle."
)

st.divider()

menu = st.sidebar.selectbox(
    "Choose a Section",
    ["Home", "Workout Tips", "Healthy Habits", "About"]
)

if menu == "Home":
    st.header("Welcome to FitBuddy!")
    st.write("Explore simple fitness tips and healthy lifestyle information.")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Focus", "Fitness")
    with col2:
        st.metric("Goal", "Healthy Lifestyle")
    with col3:
        st.metric("Experience", "Simple & User Friendly")

elif menu == "Workout Tips":
    st.header("🏃 Workout Tips")
    st.write("• Start with a warm-up before exercising.")
    st.write("• Choose exercises according to your comfort level.")
    st.write("• Take proper rest between workouts.")
    st.write("• Stay consistent with your activity.")

elif menu == "Healthy Habits":
    st.header("🥗 Healthy Habits")
    st.write("• Drink enough water.")
    st.write("• Eat a balanced diet.")
    st.write("• Get adequate sleep.")
    st.write("• Stay physically active.")
    st.write("• Maintain a regular routine.")

elif menu == "About":
    st.header("📖 About FitBuddy")
    st.write(
        "FitBuddy provides simple fitness and wellness information "
        "through an easy-to-use interface. The project was created to "
        "promote awareness of healthy lifestyle habits."
    )

st.divider()
st.caption("FitBuddy – Fitness & Wellness Project")
