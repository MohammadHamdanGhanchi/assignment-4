import streamlit as st

# Title of the app
st.title("Welcome to My Streamlit App")

# Input for user
user_input = st.text_input("Enter your name:")

# Display user input
if user_input:
    st.write(f"Hello, {user_input}! Welcome to the app.")

# Example of a simple plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
plt.figure()
plt.plot(x, y, label='Sine Wave')
plt.title('Example Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()

# Show plot in Streamlit
st.pyplot(plt)
