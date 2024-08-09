import streamlit as st
st.header('Stone Paper Scissor Game')
import random


class SPS:

    def __init__(self):
        self.user_choice = 0
        self.system_choice = 0

    def user_input(self):
        st.write('1 = Stone, 2 = Paper, 3 = Scissor')
        self.user_choice = st.number_input('Enter your option: ')


    def sys_out(self):
        self.system_choice = random.randint(1, 3)
        st.write(self.system_choice)


    def win(self):
        if self.user_choice == self.system_choice:
            st.write('Tie')
        elif self.user_choice == 1 and self.system_choice == 2:
            st.write('You loss')
            st.write('System Choice is Paper')
        elif self.user_choice == 2 and self.system_choice == 3:
            st.write('You loss')
            st.write('System Choice is Scissor')
        elif self.user_choice == 3 and self.system_choice == 1:
            st.write('You loss')
            st.write('System Choice is Stone')
        elif self.user_choice == 1 and self.system_choice == 3:
            st.write('You win')
            st.write('System Choice is Scissor')
        elif self.user_choice == 2 and self.system_choice == 1:
            st.write('You win')
            st.write('System Choice is Stone')
        elif self.user_choice == 3 and self.system_choice == 2:
            st.write('You win')
            st.write('System Choice is Paper')

a = SPS()
a.user_input()
a.sys_out()
a.win()