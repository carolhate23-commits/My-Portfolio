import streamlit as st

st.markdown("""
<style>
[data-testid="stSidebar"] {
    background-color:pink;
}
[data-testid="stSidebar"] * {
    color: black;
}
.stApp {
   background-color: lightblue;
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



st.title(" 📂:green[My Projects]")

projects = {
    "Personal site": "personal website that showcases my skills,experience,and interests.simple and easy to navigate.",
    "Database": "Boarding house management system.",
}
for name, desc in projects.items():
    with st.expander(name):
       st.write(desc)

