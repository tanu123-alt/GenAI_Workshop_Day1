import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App")
st.write("Hello Tanushree")
st.text("Let's start")

# --- Greeting ---
name = st.text_input("Enter name:")
if st.button("Greet"):
    st.success(f"Hello, {name}!")

# --- Charts ---
df = pd.DataFrame(np.random.randn(10, 2), columns=["A", "B"])
st.line_chart(df)
st.bar_chart(df)

# --- Sidebar ---
st.sidebar.title("Navigation")
st.sidebar.image("image.png")
st.sidebar.video("https://youtu.be/OuoMJMWM-9o?si=-MKAHhpFCrJiJWMW")

# --- File Upload ---
upload_file = st.file_uploader("Upload a CSV", type="csv")
if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.dataframe(df)

# --- Text Display ---
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**, *Italic*, `Code`, [Link](https://streamlit.io)")
st.code("for i in range(5): print(i)", language="python")

# --- Inputs ---
st.text_input("What's your name?")
st.text_area("Write something...")
st.number_input("Pick a number", min_value=0, max_value=100)
st.slider("Choose a range", 0, 100)
st.selectbox("Select a fruit", ["Apple", "Banana", "Mango"])
st.multiselect("Choose toppings", ["Cheese", "Tomato", "Olives"])
st.radio("Pick one", ["Option A", "Option B"])

if st.checkbox("Show Details"):
    st.info("Here are more details...")

# --- Conditional View ---
option = st.radio("Choose view", ["Show Chart", "Show Table"])

if option == "Show Chart":
    st.line_chart(df)
else:
    st.dataframe(df)

# --- Login Form ---
with st.form("login_form"):
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    submitted = st.form_submit_button("Login")

if submitted:
    st.success(f"Welcome, {username}!")