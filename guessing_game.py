import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# initialize game state
if "correct_number" not in st.session_state:
    st.session_state.correct_number = random.randint(1, 100)
    st.session_state.guess_count = 0

st.write("I am thinking of a number between 1 and 100.")

guess = st.number_input("Enter your guess:",
                        min_value=1, max_value=100, step=1)

if st.button("Submit Guess"):
    st.session_state.guess_count += 1

    if guess < st.session_state.correct_number:
        st.warning("Too low!")
    elif guess > st.session_state.correct_number:
        st.warning("Too high!")
    else:
        st.success(
            f"🎉 Correct! You guessed it in {st.session_state.guess_count} tries."
        )

        if st.button("Play Again"):
            st.session_state.correct_number = random.randint(1, 100)
            st.session_state.guess_count = 0
