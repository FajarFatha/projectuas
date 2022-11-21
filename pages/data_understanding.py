import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Multipage App"
)

st.title('Data Understanding')

st.markdown("""
Link Dataset
<a href="https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci"> https://www.kaggle.com/datasets/cherngs/heart-disease-cleveland-uci</a>
""", unsafe_allow_html=True)

st.markdown("""
Link Repository Github
<a href="https://github.com/FajarFatha/projectuas">https://github.com/FajarFatha/projectuas</a>
""", unsafe_allow_html=True)
df = pd.read_csv("heart.csv")
st.write("Dataset Heart Disease : ")
st.write(df)
st.write("Penjelasan kolom-kolom yang ada")

st.write("""
<ol>
<li>age : Umur dalam satuan Tahun</li>
<li>sex : Jenis Kelamin (1=Laki-laki, 0=Perempuan)</li>
<li>cp : chest pain type (tipe sakit dada)(0 = typical angina, 1 = atypical angina, 2 = non-anginal pain, 3 = asymptomatic)</li>
<li>trestbps : tekanan darah saat dalam kondisi istirahat dalam mm/Hg</li>
<li>chol : serum sholestoral (kolestrol dalam darah) dalam Mg/dl </li>
<li>fbs : fasting blood sugar (kadar gula dalam darah setelah berpuasa) lebih dari 120 mg/dl (1=Iya, 0=Tidak)</li>
<li>restecg : hasil test electrocardiographic (0 = normal, 1 = memiliki kelainan gelombang ST-T (gelombang T inversi dan/atau ST elevasi atau depresi > 0,05 mV), 2 = menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri dengan kriteria Estes)</li>
<li>thalach : rata-rata detak jantung pasien dalam satu menit</li>
<li>exang :  keadaan dimana pasien akan mengalami nyeri dada apabila berolah raga, 0 jika tidak nyeri, dan 1 jika menyebabkan nyeri</li>
<li>oldpeak : depresi ST yang diakibatkan oleh latihan relative terhadap saat istirahat</li>
<li>Slope : slope dari puncak ST setelah berolah raga. Atribut ini memiliki 3 nilai yaitu 0 untuk downsloping, 1 untuk flat, dan 2 untuk upsloping.</li>
<li>Ca: banyaknya pembuluh darah yang terdeteksi melalui proses pewarnaan flourosopy</li>
<li>Thal: detak jantung pasien. Atribut ini memiliki 3 nilai yaitu 1 untuk fixed defect, 2 untuk normal dan 3 untuk reversal defect</li>
</ol>
""",unsafe_allow_html=True)