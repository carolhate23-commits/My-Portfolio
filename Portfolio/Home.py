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
st.title("🏠 :orange[Home]")
st.image("IMG_20250916_145435.jpg",width=200)

st.header("Hello, I'm Caren")
st.write("I'm Computer Science Student in DEBESMSCAT")


st.info("Welcome to my portfolio!")
