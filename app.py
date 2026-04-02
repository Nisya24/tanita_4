import streamlit as st

st.set_page_config(layout="centered")

# state tombol
if "start" not in st.session_state:
    st.session_state.start = False

# tombol awal
if not st.session_state.start:
    st.markdown("<h1 style='text-align:center;'>🎁 Birthday Surprise</h1>", unsafe_allow_html=True)

    if st.button("CLICK HERE 🎉"):
        st.session_state.start = True
        st.rerun()

# setelah klik
else:
    st.markdown("""
    <style>
    body {
        background-color: white;
    }

    .fade {
        animation: fadeIn 2s ease-in forwards;
        opacity: 0;
    }

    @keyframes fadeIn {
        to { opacity: 1; }
    }

    .balloon {
        position: fixed;
        bottom: -100px;
        font-size: 30px;
        animation: floatUp 10s linear infinite;
        z-index: 0;
    }

    @keyframes floatUp {
        0% { transform: translateY(0); opacity: 1; }
        100% { transform: translateY(-120vh); opacity: 0; }
    }

    .cake {
        position: relative;
        margin: 50px auto;
        width: 200px;
        height: 200px;
        z-index: 2;
    }

    .layer {
        position: absolute;
        left: 50%;
        transform: translateX(-50%);
        border-radius: 50%;
        background: pink;
    }

    .bottom {
        width: 200px;
        height: 60px;
        bottom: 0;
        background: #ff9ecb;
    }

    .middle {
        width: 150px;
        height: 50px;
        bottom: 60px;
        background: #ffb6d9;
    }

    .top {
        width: 100px;
        height: 40px;
        bottom: 110px;
        background: #ffcce6;
    }

    .plate {
        position: absolute;
        bottom: -15px;
        left: 50%;
        transform: translateX(-50%);
        width: 220px;
        height: 20px;
        background: #ccc;
        border-radius: 50%;
    }

    .candle {
        position: absolute;
        width: 10px;
        height: 40px;
        background: red;
        top: -40px;
    }

    .flame {
        width: 10px;
        height: 15px;
        background: orange;
        border-radius: 50%;
        margin: auto;
        animation: flicker 0.3s infinite alternate;
    }

    @keyframes flicker {
        from { transform: scale(1); }
        to { transform: scale(1.3); }
    }

    .blow .flame {
        animation: none;
        opacity: 0;
    }

    </style>
    """, unsafe_allow_html=True)

    # BALON LOOP
    for i in range(10):
        st.markdown(f'''
        <div class="balloon" style="left:{i*10}%; animation-delay:{i}s;">
        🎈
        </div>
        ''', unsafe_allow_html=True)

    # KUE
    st.markdown("""
    <div class="cake fade" id="cake">
        <div class="layer bottom"></div>
        <div class="layer middle"></div>
        <div class="layer top"></div>
        <div class="plate"></div>

        <div style="position:absolute; top:70px; left:80px;">
            <div class="candle"><div class="flame"></div></div>
        </div>
        <div style="position:absolute; top:70px; left:110px;">
            <div class="candle"><div class="flame"></div></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("Tiup Lilin 🎂"):
        st.markdown("""
        <script>
        document.getElementById("cake").classList.add("blow");
        </script>
        """, unsafe_allow_html=True)

    st.markdown("""
    <h1 class="fade" style="text-align:center; color:black;">
    🎉 HAPPY BIRTHDAY TANITA 🎉
    </h1>
    """, unsafe_allow_html=True)

    st.video("https://youtu.be/NndwCpJVurc", start_time=2)
