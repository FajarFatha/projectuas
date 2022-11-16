import streamlit as st

import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestClassifier, StackingClassifier
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn import neighbors, datasets

import pickle

from sklearn import metrics

df = pd.read_csv("heart.csv")
X=df.iloc[:,0:13].values
y=df.iloc[:,13].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,stratify=y, random_state=42)

st.set_page_config(
    page_title="Multipage App"
)
st.title('Prediksi Penyakit jantung')
st.write("""
Aplikasi Untuk Memprediksi Kemungkinan Penyakit Jantung
""")
algoritma = st.sidebar.selectbox(
    'pilih algoritma klasifikasi',
    ('KNN','Naive Bayes','Random Forest','Ensemble Stacking')
)
age=st.number_input("umur : ")
sex=st.selectbox(
    'Pilih Jenis Kelamin',
    ('Laki-laki','Perempuan')
)
if sex=='Laki-laki':
    sex=1
elif sex=='Perempuan':
    sex=0
cp=st.selectbox(
    'Jenis nyeri dada',
    ('Typical Angina','Atypical angina','non-anginal pain','asymptomatic')
)
if cp=='Typical Angina':
    cp=0
elif cp=='Atypical angina':
    cp=1
elif cp=='non-anginal pain':
    cp=2
elif cp=='asymptomatic':
    cp=3
trestbps=st.number_input('resting blood pressure / tekanan darah saat kondisi istirahat(mm/Hg)')
chol=st.number_input('serum cholestoral / kolestrol dalam darah (Mg/dl)')
fbs=st.selectbox(
    'fasting blood sugar / gula darah puasa',
    ('Dibawah 120', 'Diatas 120')
)
if fbs=='Dibawah 120':
    fbs=0
elif fbs=='Diatas 120':
    fbs=1
restecg=st.selectbox(
    'resting electrocardiographic results',
    ('normal','mengalami kelainan gelombang ST-T','menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri dengan kriteria Estes')    
)
if restecg=='normal':
    restecg=0
elif restecg=='mengalami kelainan gelombang ST-T':
    restecg=1
elif restecg=='menunjukkan kemungkinan atau pasti hipertrofi ventrikel kiri dengan kriteria Estes':
    restecg=2
thalach=st.number_input('thalach (rata-rata detak jantung pasien dalam satu menit)')
exang=st.selectbox(
    'exang/exercise induced angina',
    ('ya','tidak')
)
if exang=='ya':
    exang=1
elif exang=='tidak':
    exang=0
oldpeak=st.number_input('oldpeak/depresi ST yang diakibatkan oleh latihan relative terhadap saat istirahat')
slope=st.selectbox(
    'slope of the peak exercise',
    ('upsloping','flat','downsloping')
)
if slope=='upsloping':
    slope=0
elif slope=='flat':
    slope=1
elif slope=='downsloping':
    slope=2
ca=st.number_input('number of major vessels')
thal=st.selectbox(
    'Thalassemia',
    ('normal','cacat tetap','cacat reversibel')
)
if thal=='normal':
    thal=0
elif thal=='cacat tetap':
    thal=1
elif thal=='cacat reversibel':
    thal=2

prediksi=st.button("Diagnosis")
if prediksi:
    if algoritma=='KNN':
        model = KNeighborsClassifier(n_neighbors=3)
        filename='knn.pkl'
    elif algoritma=='Naive Bayes':
        model = GaussianNB()
        filename='gaussian.pkl'
    elif algoritma=='Random Forest':
        model = RandomForestClassifier(n_estimators = 100)
        filename='randomforest.pkl'
    elif algoritma=='Ensemble Stacking':
        estimators = [
            ('rf_1', RandomForestClassifier(n_estimators=10, random_state=42)),
            ('knn_1', KNeighborsClassifier(n_neighbors=10))             
        ]
        model = StackingClassifier(estimators=estimators, final_estimator=GaussianNB())
        filename='stacking.pkl'
    model.fit(X_train, y_train)
    Y_pred = model.predict(X_test) 

    score=metrics.accuracy_score(y_test,Y_pred)

    loaded_model = pickle.load(open(filename, 'rb'))
    dataArray = [age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
    pred = loaded_model.predict([dataArray])

    if int(pred[0])==0:
        st.success(f"Hasil Prediksi : Tidak memiliki penyakit Jantung")
    elif int(pred[0])==1:
        st.error(f"Hasil Prediksi : Memiliki penyakit Jantung")

    st.write(f"akurasi : {score}")






