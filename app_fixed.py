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

# Animasi Lottie (ganti URL dengan animasi bebas)
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json"
lottie_animasi = load_lottieurl(lottie_url)

# Beranda
if menu == "Beranda":
    st.title("SpectroCalc: Kalkulator Konsentrasi Spektrofotometri")
    st.markdown("""
        Aplikasi ini membantu menghitung konsentrasi zat berdasarkan nilai absorbansi dari spektrofotometer.
        Cocok untuk mahasiswa dan laboran kimia dalam analisis kuantitatif.
    """)
    if lottie_animasi:
        st_lottie(lottie_animasi, speed=1, height=300)
    else:
        st.warning("Gagal memuat animasi.")
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Spectrophotometer.jpg/640px-Spectrophotometer.jpg", caption="Alat Spektrofotometer")
