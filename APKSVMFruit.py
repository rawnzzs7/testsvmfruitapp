import pickle
import streamlit as st

# Baca model yang telah disimpan
fruit_model = pickle.load(open('svmfruit_model.sav', 'rb'))

# Judul web
st.title('SVM Tes Web Prediksi Buah')

# Input: Menerima angka sebagai input, konversi ke float
diameter = st.text_input('Input Diameter')
weight = st.text_input('Input Weight')
red = st.text_input('Input Red')
green = st.text_input('Input Green')
blue = st.text_input('Input Blue')

# Memastikan input yang diterima adalah angka dan tidak kosong
if diameter and weight and red and green and blue:
    diameter = float(diameter)
    weight = float(weight)
    red = float(red)
    green = float(green)
    blue = float(blue)

    # code untuk prediksi
    namefruit_diagnosis = ''

    # membuat tombol untuk prediksi
    if st.button('SVM Test Prediksi Nama Buah'):
        # Membuat fitur input yang sesuai dengan format yang diminta oleh model
        features = [[diameter, weight, red, green, blue]]
        
        # Prediksi menggunakan model
        namefruit_prediction = fruit_model.predict(features)

        # Konversi hasil numerik ke nama buah
        if namefruit_prediction[0] == 1:
            namefruit_diagnosis = 'Orange'
        elif namefruit_prediction[0] == 2:
            namefruit_diagnosis = 'Grapefruit'
        else:
            namefruit_diagnosis = 'Tidak Dikenal'

        # Menampilkan hasil prediksi
        st.success(f'Hasil Prediksi: {namefruit_diagnosis}')
else:
    st.warning('Silakan masukkan semua input untuk melakukan prediksi.')
