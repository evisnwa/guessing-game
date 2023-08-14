import streamlit as st
import numpy as np
import random

st.image("rolling dice.gif")


st.header("Guessing Game")
st.subheader("Let's have some fun,guess the right number")

x = st. number_input("choose number from 1-6",step=1)
x = int(x)
y = np.random.randint(1,7)


def gg(x,y):
    if x > 6:
      return("Invalid number,Choose number from 1-6")
    else:
        st.write(f"Random number is {y}")
        st.write(f"Your choosen number is {x}")

        if x==y:
            st.balloons()
            return("Correct") 
        else:   
            return("Try again")



c1,c2 = st.columns(2)

with c1:
    if st.button("Guess"):
        st.write(gg(x,y))
with c2:
    if st.button("Retry"):
        st.experimental_rerun()
        