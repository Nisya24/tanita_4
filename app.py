import streamlit as st

# state tombol
if "start" not in st.session_state:
    st.session_state.start = False

# tombol awal
if not st.session_state.start:
    if st.button("CLICK HERE"):
        st.session_state.start = True
        st.rerun()

# setelah klik → baru tampil code asli lo
else:
    st.title('HAPPY BIRTHDAY TANITA')
    st.write('Selamat hari lahir ya untuk my teman sahabat dari janin my forever blackpink member. Selamat sdh memulai hidup baru di tahun ini 💖')

    slider_value = st.slider('Select a value', min_value=0, max_value=100, value=50)

    if (slider_value > 51):
        VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWc5Dy9C7JPARX5"
    else:
        VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWc5Dy9C7JPARX5"

    st.balloons()
    st.video(VIDEO_URL, start_time=2)
