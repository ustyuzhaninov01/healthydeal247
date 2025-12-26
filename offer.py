import streamlit as st
import requests
from urllib.parse import urlencode
from streamlit_autorefresh import st_autorefresh
import time
import streamlit.components.v1 as components
import base64

# ==============================
# AD COMBO FUNCTION (MUST BE FIRST)
# ==============================
def send_adcombo_order(name, phone, ip):
    API_URL = "https://api.adcombo.com/api/v2/order/create/"

    params = {
        "api_key": "32c12748901cfea93fe7cc2d175afbac",
        "name": name,
        "phone": phone,
        "ip": ip,
        "country_code": "MA",
        "offer_id": "40302",
        "referrer": "http://my-click-site.com",
        "price": "399",
        "base_url": "http://my-domain.com/"
    }

    response = requests.get(API_URL, params=params, timeout=10)
    return response.json()


# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="healthydeal247",
    page_icon="📞",
    initial_sidebar_state="collapsed",
)

# ==============================
# HIDE STREAMLIT UI
# ==============================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ==============================
# HEADER
# ==============================
st.markdown("""
<div style="
    text-align:center;
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
    padding:40px;
    border-radius:30px;
    font-size:2.5em;
    font-weight:bold;
    color:white;
">
🏥 HEALTHY DEAL 24/7 📞
</div>
""", unsafe_allow_html=True)

# ==============================
# AUTO REFRESH
# ==============================
st_autorefresh(interval=5000, limit=None, key="timer")

if "start_time" not in st.session_state:
    st.session_state.start_time = time.time()

# ==============================
# VIDEO
# ==============================
st.video("diabete1.mp4")

# ==============================
# MAIN CONTENT (AFTER 2s)
# ==============================
if time.time() - st.session_state.start_time >= 2:

    components.html("""
    <div style="text-align:center;padding:24px;border-radius:14px;
        background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);color:white;">
        <h1>🔥 LIMITED OFFER TIME</h1>
        <h1 id="timer">14:53:00</h1>
    </div>

    <script>
    let time = 53580;
    setInterval(() => {
        if (time < 0) return;
        let h = Math.floor(time / 3600);
        let m = Math.floor((time % 3600) / 60);
        let s = time % 60;
        document.getElementById("timer").innerHTML =
            `${String(h).padStart(2,'0')}:${String(m).padStart(2,'0')}:${String(s).padStart(2,'0')}`;
        time--;
    }, 1000);
    </script>
    """, height=240)

    st.image("pack.png", width=550)

    st.markdown("""
    <div style="text-align:center;padding:20px;border-radius:14px;
        background:linear-gradient(135deg,#0f2027,#203a43,#2c5364);color:white;">
        <h1>🔥 NEW PRICE 399 MAD</h1>
    </div>
    """, unsafe_allow_html=True)

    # ==============================
    # FORM
    # ==============================
    name = st.text_input("Name", placeholder="Name", label_visibility="collapsed")
    phone = st.text_input("Phone", placeholder="Phone", label_visibility="collapsed")

    if st.button("Ask a Call"):
        if not name or not phone:
            st.warning("Please enter your name and phone")
        else:
            try:
                ip = requests.get("https://httpbin.org/ip", timeout=5).json().get("origin", "102.207.32.0")
            except:
                ip = "102.207.32.0"

            response = send_adcombo_order(name, phone, ip)

            if response.get("code") == "ok":
                st.success(f"✅ Order created. ID: {response.get('order_id')}")
            else:
                st.error("❌ Try again")
                st.write(response)

# ==============================
# COMMENTS
# ==============================
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.markdown("<h2 style='text-align:center;color:#2c5364;'>💬 Real reviews</h2>", unsafe_allow_html=True)

comments = [
    ("Brahim", "I feel much better now!", "cm1.svg"),
    ("Mhamed", "My sugar level dropped.", "cm2.svg"),
    ("Ahmed", "Life changed completely.", "cm4.svg"),
    ("Fatima", "Best decision ever!", "cm3.svg")
]

for name, text, img in comments:
    st.markdown(f"""
    <div style="display:flex;background:#203a43;color:white;padding:15px;
        border-radius:14px;margin-bottom:10px;">
        <img src="data:image/svg+xml;base64,{img_to_base64(img)}"
             style="width:60px;height:60px;border-radius:50%;margin-right:15px;">
        <div><b>{name}</b><br>{text}</div>
    </div>
    """, unsafe_allow_html=True)

# ==============================
# FOOTER
# ==============================
st.markdown("""
---
© 2025 All Rights Reserved |
[Privacy Policy](https://feleo.net/content/shared/html/policy_en.html) |
[Report](https://ac-feedback.com/report_form/)
""", unsafe_allow_html=True)

