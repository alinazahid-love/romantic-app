import streamlit as st
import time

st.title("🌹 A Special Surprise for My Love 💖")

st.write("Hey, beautiful! I have something sweet for you. 😊")

name = st.text_input("First, tell me your beautiful name:")

if name:
    st.write(f"Hello, {name}! You're the most amazing person in my life! ❤️")

    st.write("I have a few cute questions for you! 💌")

    question1 = st.radio("How much do you love me?", ["A little", "A lot", "More than anything! 😍"])
    
    if question1 == "A little":
        st.write("Oh no! I need more love! 😢")
    elif question1 == "A lot":
        st.write("That makes me so happy! But guess what? I love you even more! 🥰")
    elif question1 == "More than anything! 😍":
        st.write("You just made my heart melt! You're my everything! 💘")

    time.sleep(1)
    st.write("Let's see if you know me well... 🤔")

    question2 = st.radio("What is my favorite thing about you?", ["Your smile 😊", "Your kindness 💖", "Your eyes 👀", "Everything about you! 😍"])

    if question2 == "Everything about you! 😍":
        st.write("Yesss! You're absolutely perfect to me! ❤️")
    else:
        st.write("Haha, that’s cute, but the real answer is: EVERYTHING! 😍")
    
    st.balloons()
    st.write("No matter what, I love you endlessly! 💖")
