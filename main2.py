import streamlit as st

st.title("나의 위키 앱")

st.text("\n\n")



while True:
  if a=="stop":
    break
  a = st.text_input("무엇을 찾고 싶나요?:")


  


  
  st.link_button("Go to 나무위키", f"https://namu.wiki/w/{a}")
  st.link_button("Go to 위키백과",f"https://ko.wikipedia.org/wiki/{a}")
  
  
