import streamlit as st
from openai import OpenAI

st.title("GPT")

api_key = st.text_input("API Key", type="password")
st.session_state.api_key = api_key

client = OpenAI(api_key=api_key)

user_question = st.text_area("Prompt")
if st.button("Submit"):
    response = client.chat.completions.create(
        model="gpt-5-mini",
        messages=[
            {"role": "user", "content": user_question}
            ]
            )
    answer = response.choices[0].message.content
    st.write(answer)
