import streamlit as st
import random

st.title("나의 위키 앱")

st.text("\n\n")



while True:
  검색 = input("")
  if 검색==stop:
    break
  
  st.write(f"나무위키:https://namu.wiki/w/{검색}")
  st.write(f"나무위키:https://ko.wikipedia.org/wiki/{검색}")
  
  
