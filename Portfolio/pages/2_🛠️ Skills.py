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

st.title(" 🛠️ :orange[Skills]")
st.subheader("Programming")
st.progress(50)
st.write(" Basic Python")

st.subheader("Web Development")
st.progress(60)
st.write("Basic HTML/CSS")

st.subheader("  Design")
st.progress(70)
st.write("Canva / UI Design")
st.subheader("  Tools")
st.write("- GitHub")
st.write("- VS Code")
st.write("- Streamlit")
