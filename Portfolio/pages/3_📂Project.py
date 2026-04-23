import streamlit as st
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color: green;
}
[data-testid="stSidebar"] * {
    color: white;
}
.stApp {
   background-color: aliceblue;
}   
.main {
    text-align: center;
}
img {
    border-radius: 50%;
}
.title {
    font-size: 40px;
    font-weight: bold;
}
.subtitle {
    font-size: 20px;
    color: gray;
}
.box {
    background-color: #f0f2f6;
    padding: 15px;
    border-radius: 10px;
    margin-top: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title(" 📂 :orange[My Projects]")

projects = {
    "Simple Calculator": "A basic calculator that can do addition,subtraction, multiplication,division, and modulo.",
    "Personal Site(HTML)": "The website is design to be simple and easy to navigate.It shows my skill,Experiences, and Interest.",
    "Database": "Boarding house management system"
}
for name, desc in projects.items():
    with st.expander(name):
      st.write(desc)
