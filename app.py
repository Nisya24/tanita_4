import streamlit as st

# BACKGROUND PINK
st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFC2D1;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# state tombol
if "start" not in st.session_state:
    st.session_state.start = False

# tombol awal (CENTER)
if not st.session_state.start:
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        if st.button("CLICK HERE"):
            st.session_state.start = True
            st.rerun()

# setelah klik → code asli lo
else:
    st.title('HAPPY BIRTHDAY TANITA')
    st.write('Selamat hari lahir ya untuk my teman sahabat dari janin my forever blackpink member. Selamat sdh memulai hidup baru di tahun ke 20 ini, sering-sering ketemuan ya kita. Love you from melbin <3')

    slider_value = st.slider('rating web buatan gweh plis)', min_value=0, max_value=100, value=50)

    if (slider_value > 51):
        VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWc5Dy9C7JPARX5"
    else:
        VIDEO_URL = "https://youtu.be/NndwCpJVurc?si=6eWc5Dy9C7JPARX5"

    st.balloons()
    st.video(VIDEO_URL, start_time=2)
