import streamlit as st 
st.set_page_config(
    page_title="To-do-App",
    page_icon=":smile:"
)
st.header("To-do-App")
st.write("---")


def add_task():
    global text
    if text.isalnum():
        st.checkbox(text)

text = st.text_input("Enter Task: ","")
main_btn = st.button(":heavy_plus_sign: Add",type="primary",on_click=add_task)

