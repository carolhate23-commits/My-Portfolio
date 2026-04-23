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



st.title("📬:green[Contact Me]")

name = st.text_input("Name")
email = st.text_input("Email")
message = st.text_area("Message")
if st.button("Send"):
 if name and email and message:
      st.success("Message sent successfully! ✅")
else:
      st.error("Please fill all fields.")
st.markdown("###🌐Social Links")
st.write("- GitHub: https://github.com/carolhate@23-commits")
st.write("- Facebook: https://facebook.com/carol.ha.te")
