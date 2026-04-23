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

st.title("🧑‍💻 :orange[About Me]")

st.write(""" 
I am a 3rd year Computer Science Student at DEBESMSCAT. Currently exploring web development for our thesis project. Im also interested in graphic design.
""")
st.subheader("🎓 :blue[Education]")
st.write("- Bachelor of Science In Computer Science")
st.write("- 3rd Year ")
st.write("- DEBESMSCAT")
st.subheader("🎯 :blue[Goals]")
st.write("- My goal is to finish my studies and improve my skills in programming")
st.write("- I want to build simple application")
