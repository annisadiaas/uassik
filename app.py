import streamlit as st 
from PIL import Image


# --- GENERAL SETTINGS ---
PAGE_TITLE = "CV | Annisa Dias Oktanida"
PAGE_ICON = ":wave:"
NAME = "Annisa Dias Oktanida, S.MIK"
DESCRIPTION = """
Health Coding Analyst, bidang analisis dan diagnosa kode penyakit serta coding BPJS.
"""
EMAIL = "oktanidannisa@gmail.com"
SOCIAL_MEDIA = {
	'YouTube': 'https://youtube.com/@av00cadeo',
	'Twitter': 'https://twitter.com/sforstrawberry',
	'Instagram': 'https://instagram.com/_oissa',
	'Telegram': 'https://t.me/dainosolisthere'
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
	image = Image.open('picture.png')
	st.image(image, width=190)

with col2:
	st.title(NAME)
	st.write(EMAIL)
	st.write(DESCRIPTION)

# --- SOCIAL LINKS ---
st.write('#')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
	cols[index].write(f"[{platform}]({link})")

#####################
# Header
st.markdown('#')
st.subheader('Kualifikasi Profil')
st.info('''
Saya seorang Sarjana Informasi Kesehatan lulusan Universitas Nasional Karangturi Semarang jurusan Manajemen Informasi Kesehatan yang mendapat gelar Dengan Pujian. Saya antusias dengan hal baru serta mampu bekerja secara individu maupun dalam tim. Memiliki pengalaman praktik tentang coding kesehatan dalam bidang penyakit. Memiliki keterampilan dalam administrasi rumah sakit, pengkodean tindakan, serta pengkodean penyakit.
''')

####################
# Biodata
st.markdown('#')
st.subheader('Tentang Saya')

st.markdown('Nama 					: Annisa Dias Oktanida')
st.markdown('Tempat, Tanggal Lahir 	: Kendal, 01 Oktober 2004')
st.markdown('Agama 					: Islam')
st.markdown('Jenis Kelamin 			: Perempuan')
st.markdown('Alamat 				: Jl. Mlatiharo 1, 431 A, Mlatibaru, Semarang Timur')

#########################
st.markdown('#')
st.subheader('Pendidikan')

st.markdown('**Analisis Koding Penyakit** (Manajemen Informasi Kesehatan), Universitas Nasional Karangturi, Semarang, 2022-2025')
st.markdown('''
- GPA : `3.89`
- Menerima penghargaan dalam Program Kreativitas Mahasiswa bidang Karya Inovatif (PKM-KI)
- Menerima penghargaan dalam lomba poster digital dengan tema kesehatan
- Menerima penghargaan dalam jurnal ilmiah oleh Perhimpunan Profesional Perekam Medis dan Informasi Kesehatan Indonesia (PORMIKI)
''')

########################
st.markdown('#')
st.subheader('Pengalaman')

st.markdown('''
- Program Magang Bersertifikat dari MBKM - Klinik Mitrakita
	- Pengelola data kesehatan pasien
- Praktik Kerja Lapangan (PKL) - RSND Diponegoro
	- Divisi rekam medis
- Himpunan Mahasiswa 
- Volunteer 
''')

#########################
st.markdown('#')
st.subheader('Keterampilan')

st.markdown('''
- Digital drawing 
- Bilingual
- Writting skills
- Problem solving
- Time management
- Analisis data
- Design
''')

st.markdown('#')
st.subheader('Kontak')
st.info('''
- Whatsapp : +628978503864
- Email : oktanidannisa@gmail.com
''')