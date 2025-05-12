import streamlit as st
import plotly.graph_objs as go
import numpy as np

# Title of the app
st.title("Welcome to My Streamlit App")

# Input for user
user_input = st.text_input("Enter your name:")

# Display user input
if user_input:
    st.write(f"Hello, {user_input}! Welcome to the app.")

# Example of a simple plot using Plotly
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Plotly figure
fig = go.Figure()

# Add a trace (line) to the figure
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='Sine Wave'))

# Update layout of the figure
fig.update_layout(
    title='Example Plot',
    xaxis_title='X-axis',
    yaxis_title='Y-axis'
)

# Show plot in Streamlit
st.plotly_chart(fig)
