import streamlit as st
import random

st.title("나의 위키 앱")

st.text("\n\n")



while True:
  a = st.text_input("무엇을 찾고 싶나요?:")
  if a==stop:
    break
  
  st.link_button("Go to 나무위키", f"https://namu.wiki/w/{a}")
  st.link_button("Go to 위키백과",f"https://ko.wikipedia.org/wiki/{a}")
  
  
