import streamlit as st
import pandas as pd

st.set_page_config(layout = "wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=300)

with col2:
    st.title("ADITYA KENDRE")
    content = """
    Hi, I am Aditya! I am a curious, motivated and lazy(only if task isn't intresting) student.
      I am currently learning DSA and full stack development.
"""
    st.info(content) # can use .write also but text won't be highlighted

content2 = """Below are some of the projects I made"""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])

df = pd.read_csv("data.csv",sep = ",")

with col3:
    for index, row in df[:6].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width= 150)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[6:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], width= 150)
        st.write(f"[Source Code]({row['url']})")


