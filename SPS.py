import streamlit as st
import random
import time

# Add a title and instructions
st.title("Stone Paper Scissors Game")
st.markdown("""
    Welcome to the **Stone Paper Scissors Game**. 
    Choose your option and let’s see who wins! 
    - 1 = Stone
    - 2 = Paper
    - 3 = Scissors
""")

# Create a function for the game
class SPSGame:
    def __init__(self):
        self.user_choice = None
        self.system_choice = None

    def get_user_input(self):
        # User chooses between Stone, Paper, or Scissors
        choice = st.radio("Choose your option:", ["Stone", "Paper", "Scissors"])
        return choice

    def generate_system_choice(self):
        # System randomly chooses between Stone, Paper, or Scissors
        options = ["Stone", "Paper", "Scissors"]
        self.system_choice = random.choice(options)
        time.sleep(1)  # Add a delay for suspense
        return self.system_choice

    def display_result(self):
        # Display the result and animation
        if self.user_choice == self.system_choice:
            st.markdown("It's a **Tie**!")
            st.balloons()  # Confetti on tie
        elif (self.user_choice == "Stone" and self.system_choice == "Scissors") or \
             (self.user_choice == "Paper" and self.system_choice == "Stone") or \
             (self.user_choice == "Scissors" and self.system_choice == "Paper"):
            st.success("You **win**!")
            st.image("https://media.giphy.com/media/d2lcHJTG5Tscg/giphy.gif", width=200)
        else:
            st.error("You **lose**!")
            st.image("https://media.giphy.com/media/3oFzmrL0rS5LsJXi7i/giphy.gif", width=200)

        st.write(f"Your choice: {self.user_choice}")
        st.write(f"System's choice: {self.system_choice}")

# Create the game instance and execute
game = SPSGame()

# Prompt user input
user_choice = game.get_user_input()

# Show system's choice with animation delay
if user_choice:
    st.write("The system is choosing...")
    system_choice = game.generate_system_choice()

    # Display the outcome
    game.user_choice = user_choice
    game.display_result()
