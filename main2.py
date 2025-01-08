pip install openai
import streamlit as st
from openai import OpenAI
API_key = st.text_input("api key:")
client = OpenAI(api_key = API_key)
st.title("나의 위키 앱")

st.text("\n\n")



while True:
  if a=="stop":
    break
  a = st.text_input("무엇을 찾고 싶나요?:")


  completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {"role": "developer", "content": "You are a helpful assistant."},
      {"role": "user", "content": a }
    ]
  )

  print(completion.choices[0].message.content)

  
  st.link_button("Go to 나무위키", f"https://namu.wiki/w/{a}")
  st.link_button("Go to 위키백과",f"https://ko.wikipedia.org/wiki/{a}")
  
  
