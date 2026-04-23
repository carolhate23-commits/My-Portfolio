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



st.title("🛠️:green[Skills]")
st.subheader(":red[Programming]")
st.progress(70)
st.write("Python")

st.progress(70)
st.write("JavaScript")

st.subheader(":red[Web development]")
st.progress(75)
st.write("HTML/CSS")

st.subheader(":red[Design]")
st.progress(75)
st.write("Canva / UI Design")
st.subheader(":red[Tools]")
st.write("- GitHub")
st.write("- VS Code")
st.write("- Streamlit")
