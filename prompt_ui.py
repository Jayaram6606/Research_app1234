from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo")

st.header("Research app")

user_input = st.text_input("enter your text")

if st.button("Submit"):
    result = model.invoke(user_input)
    st.write(result.content)
