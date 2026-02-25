from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

st.header("Research app")

user_input = st.text_input("enter your text")

if st.button("Submit"):
    st.text("Enter random text")