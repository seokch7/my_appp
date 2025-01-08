import streamlit as st
import random

st.title("나의 위키 앱")

st.text("\n\n")



while True:
  a = input("")
  if a==stop:
    break
  
  st.link_button("Go to 나무위키", f"https://namu.wiki/w/{a}")
  st.link_button("Go to 위키백과",f"https://ko.wikipedia.org/wiki/{a}")
  
  
