import streamlit as st
from openai import OpenAI

st.title("GPT")

api_key = st.text_input("API Key", type="password")

if api_key:
    st.session_state["OPENAI_API_KEY"] = api_key
    client = OpenAI(api_key=api_key)
    st.session_state["openai_client"] = client
else:
    st.write("API 키를 입력하세요")

user_question = st.text_area("Prompt")
if st.button("Submit"):
    response = response = client.responses.create(
        model="gpt-5-mini",
        input=user_question
    )
    answer = response.output_text
    st.write(answer)
