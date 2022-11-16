import streamlit as st

st.set_page_config(
    page_title="Multipage App"
)

st.title('Data Understanding')
st.write("""
Pengertian dan penjelasan algoritma yang digunakan
""")

st.markdown("""
Link Dataset
<a href="https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset"> https://www.kaggle.com/datasets/akshaydattatraykhare/diabetes-dataset</a>
""", unsafe_allow_html=True)

st.markdown("""
Link Repository Github
<a href="https://github.com/FajarFatha/projectuas">https://github.com/FajarFatha/projectuas</a>
""", unsafe_allow_html=True)