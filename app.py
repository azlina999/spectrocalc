import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import requests

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

st.set_page_config(page_title="SpectroCalc", layout="centered", page_icon=":microscope:")

# Load CSS eksternal
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Sidebar navigasi
menu = st.sidebar.radio("Navigasi", ["Beranda", "Kalkulator", "Fungsi", "Latar Belakang", "Referensi"])

# Beranda
if menu == "Beranda":
    st.title("SpectroCalc: Kalkulator Konsentrasi Spektrofotometri")
    st.markdown("""
        Aplikasi ini membantu menghitung konsentrasi zat berdasarkan nilai absorbansi dari spektrofotometer.
        Cocok untuk mahasiswa dan laboran kimia dalam analisis kuantitatif.
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Spectrophotometer.jpg/640px-Spectrophotometer.jpg", caption="Gambar Spektrofotometer", use_column_width=True)
    lottie_animasi = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tljjahqu.json")
    st_lottie(lottie_animasi, speed=1, height=300)

# Kalkulator
elif menu == "Kalkulator":
    st.header("🔬 Kalkulator Konsentrasi")

    A = st.number_input("Masukkan nilai absorbansi (A)", format="%.3f")
    m = st.number_input("Masukkan kemiringan kurva kalibrasi (m)", format="%.3f")
    b = st.number_input("Masukkan intersep kurva kalibrasi (b)", format="%.3f")

    if st.button("Hitung Konsentrasi"):
        if m != 0:
            C = (A - b) / m
            st.success(f"Nilai konsentrasi (C) terukur: {C:.3f}")
        else:
            st.error("Nilai m tidak boleh nol.")

# Fungsi
elif menu == "Fungsi":
    st.header("📘 Fungsi Aplikasi")
    st.markdown("""
    - Menghitung konsentrasi zat dari absorbansi.
    - Membantu kalibrasi data hasil spektrofotometri.
    - Validasi data input dan hasil secara interaktif.
    """)

# Latar Belakang
elif menu == "Latar Belakang":
    st.header("📚 Latar Belakang")
    st.markdown("""
    Dalam analisis kimia kuantitatif, spektrofotometer digunakan untuk mengukur konsentrasi zat dengan prinsip hukum Lambert-Beer.
    Diperlukan perhitungan dari kurva kalibrasi agar hasilnya akurat.
    """)

# Referensi
elif menu == "Referensi":
    st.header("🔗 Referensi")
    st.markdown("""
    - Skoog, D. A., Holler, F. J., & Crouch, S. R. (2014). *Principles of Instrumental Analysis*.
    - Wikipedia: Spectrophotometry
    - Modul Praktikum Analisis Instrumen
    """)
