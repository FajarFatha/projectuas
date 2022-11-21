import streamlit as st

st.set_page_config(
    page_title="Multipage App"
)


st.title('Dasar Teori')
st.write("""<hr>""",unsafe_allow_html=True)
st.write("""
<h3>Data Mining</h1><b3>
<p style="text-align: justify;text-indent: 45px;">Data mining adalah proses pengumpulan dan pengolahan data yang bertujuan untuk mengekstrak informasi penting pada data. Proses pengumpulan dan ekstraksi informasi tersebut dapat dilakukan menggunakan perangkat lunak dengan bantuan perhitungan statistika, matematika, ataupun teknologi Artificial Intelligence (AI). Data mining sering disebut juga Knowledge Discovery in Database (KDD).</p>
<br>
""",unsafe_allow_html=True)

st.write("""
<h3>Klasifikasi</h1><b3>
<p style="text-align: justify;text-indent: 45px;">Terdapat beberapa metode dalam melakukan data mining, salah satunya adalah klasifikasi. Klasifikasi data mining adalah sebuah proses menemukan definisi kesamaan karakteristik dalam suatu kelompok atau kelas. Klasifikasi adalah salah satu metode yang paling umum untuk digunakan dalam data mining.</p>
<p style="text-align: justify;text-indent: 45px;">Metode ini dilakukan bertujuan untuk memperkirakan kelas dari suatu objek yang labelnya belum diketahui. Terdapat beberapa metode klasifikasi yang sering digunakan, yaitu Logistic Regression, Naïve Bayes, Decision Tree, Random Forest, K-Nearest Neighbour, dan Artificial Neural Network. Berikut pengertian dari beberapa klasifikasi tersebut</p>
<br>
""",unsafe_allow_html=True)

st.write("""
<h6>K-Nearest Neighbour (KNN)</h6><b3>
<p style="text-align: justify;text-indent: 45px;">K-NN merupakan kepanjangan dari K-Nearest Neighbor. Algoritma K-NN merupakan algoritma klasifikasi yang bekerja dengan mengambil sejumlah K data terdekat (tetangganya) sebagai acuan untuk menentukan kelas dari data baru. Algoritma ini mengklasifikasikan data berdasarkan similarity atau kemiripan atau kedekatannya terhadap data lainnya.</p>
<p>Algoritma K-NN :</p>
<ol>
<li>Menentukan nilai K</li>
<li>Menghitung jarak anatar data uji dengan data latih</li>
<li>mengurutkan data berdasarkan jarak secara ascending</li>
<li>mengambil data sebanyak k terdekat</li>
<li>memilih kelas mayor</li>
</ol>
<p style="text-align: justify;text-indent: 45px;">Pada implementasi yang digunakan di website ini menggunakan jumlah neighbors = 3</p>
<br>
""",unsafe_allow_html=True)

st.write("""
<h6>Naive Bayes</h6><b3>
<p style="text-align: justify;text-indent: 45px;">Naive Bayes adalah metode yang cocok untuk klasifikasi biner dan multiclass. Metode yang juga dikenal sebagai Naive Bayes Classifier ini menerapkan teknik supervised klasifikasi objek di masa depan dengan menetapkan label kelas ke instance/catatan menggunakan probabilitas bersyarat. Probabilitas bersyarat adalah ukuran peluang suatu peristiwa yang terjadi berdasarkan peristiwa lain yang telah (dengan asumsi, praduga, pernyataan, atau terbukti) terjadi.</p>
<p style="text-align: justify;text-indent: 45px;">Istilah supervised merujuk pada klasifikasi training data yang sudah diberi label dengan kelas. Misalnya, sebuah transaksi penipuan telah ditandai sebagai data transaksional. Kemudian, jika Anda ingin mengklasifikasikan transaksi di masa depan menjadi fraudulent/non-fraudulent (penipuan/non-penipuan), maka jenis klasifikasi itu akan disebut sebagai supervised.</p>
<p style="text-align: justify;text-indent: 45px;">Nah, model machine learning yang diterapkan pada program tersebut menggunakan teorema Bayes yang dirumuskan sebagai berikut:</p>
""",unsafe_allow_html=True)
st.latex(r'''P(A \mid B) = \frac{P(B \mid A) \, P(A)}{P(B)}''')

st.write("""
<br>
<h6>Random Forest</h6><b3>
<p style="text-align: justify;text-indent: 45px;">Random Forest adalah algoritma dalam machine learning yang digunakan untuk pengklasifikasian data set dalam jumlah besar. Salah satu algoritma terbaik dalam machine learning ini menggunakan decision tree atau pohon keputusan untuk melangsungkan proses seleksi, di mana tree atau pohon decision tree akan dibagi secara rekursif berdasarkan data pada kelas yang sama. Dalam hal ini, penggunaan tree yang semakin banyak akan memengaruhi akurasi yang didapat menjadi lebih optimal. Penentuan klasifikasi dengan Random Forest dilakukan berdasarkan hasil voting dan tree yang terbentuk. </p>
<p style="text-align: justify;text-indent: 45px;">Random Forest adalah algoritma untuk pengklasifikasian. Lalu, seperti apa cara kerjanya? Random Forest bekerja dengan membangun beberapa decision tree dan menggabungkannya demi mendapatkan prediksi yang lebih stabil dan akurat. ‘Hutan’ yang dibangun oleh Random Forest adalah kumpulan decision tree di mana biasanya dilatih dengan metode bagging. Ide umum dari metode bagging adalah kombinasi model pembelajaran untuk meningkatkan hasil keseluruhan</p>
<p style="text-align: justify;text-indent: 45px;">Algoritma Random Forest meningkatkan keacakan pada model sambil menumbuhkan tree. Alih-alih mencari fitur yang paling penting saat memisahkan sebuah node, Random Forest mencari fitur terbaik di antara subset fitur yang acak. Alhasil, cara ini menghasilkan keragaman yang luas dan umumnya menghasilkan model yang lebih baik.</p>
<p style="text-align: justify;text-indent: 45px;">Pada implementasi yang digunakan di website ini menggunakan jumlah estimators = 100</P>
""",unsafe_allow_html=True)

st.write("""
<br>
<h6>Ensemble Stacking</h6><b3>
<p style="text-align: justify;text-indent: 45px;">Stacking merupakan cara untuk mengkombinasi beberapa model, dengan konsep meta learner. dipakai setelah bagging dan boosting. tidak seperti bagging dan boosting, stacking memungkinkan mengkombinasikan model dari tipe yang berbeda. Ide dasarnya adalah untuk train learner tingkat pertama menggunakan kumpulan data training asli, dan kemudian menghasilkan kumpulan data baru untuk melatih learner tingkat kedua, di mana output dari learner tingkat pertama dianggap sebagai fitur masukan sementara yang asli label masih dianggap sebagai label data training baru. Pembelajar tingkat pertama sering dihasilkan dengan menerapkan algoritma learning yang berbeda.</p>
<p style="text-align: justify;text-indent: 45px;">Dalam fase training pada stacking, satu set data baru perlu dihasilkan dari classifier tingkat pertama. Jika data yang tepat yang digunakan untuk melatih classifier tingkat pertama juga digunakan untuk menghasilkan kumpulan data baru untuk melatih classifier tingkat kedua. proses tersebut memiliki risiko yang tinggi yang akan mengakibatkan overfitting. sehingga disarankan bahwa contoh yang digunakan untuk menghasilkan kumpulan data baru dikeluarkan dari contoh data training untuk learner tingkat pertama, dan prosedur crossvalidasi.</p>
<p style="text-align: justify;text-indent: 45px;"> Dalam website ini estimator yang digunakan untuk stacking yaitu Random Forest dengan jumlah estimator 10 dan KNN dengan jumlah neighbors 10, sedangkan untuk final estimator menggunakan Naive Bayes</p>
""",unsafe_allow_html=True)





