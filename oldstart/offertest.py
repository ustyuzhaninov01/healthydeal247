import streamlit as st
import requests
from urllib.parse import urlencode

# ---------------- CONFIG ----------------
API_URL = "https://api.adcombo.com/api/v2/order/create/"

st.set_page_config(
    page_title="offeronline247",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------- HIDE STREAMLIT UI ----------------
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

.stApp {
    background-color: #0e1117;
}

.vsl-box {
    max-width: 720px;
    margin: auto;
    padding: 20px;
}

h1, p {
    text-align: center;
    color: white;
}

.stTextInput input {
    font-size: 18px;
    height: 50px;
}

.stButton button {
    width: 100%;
    height: 55px;
    font-size: 20px;
    font-weight: bold;
    background-color: #ff3d00;
    color: white;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- API FUNCTION ----------------
def send_adcombo_order(name, phone, ip):
    params = {
        "api_key": "32c12748901cfea93fe7cc2d175afbac",
        "name": name,
        "phone": phone,
        "ip": ip,
        "country_code": "MA",
        "offer_id": "40302",
        "referrer": "http://my-click-site.com",
        "price": "399",
        "base_url": "http://my-domain.com/",
    }

    response = requests.get(API_URL, params=params, timeout=10)
    return response.json()

# ---------------- VSL CONTENT ----------------
with st.container():
    st.markdown('<div class="vsl-box">', unsafe_allow_html=True)

    # 🎥 VSL VIDEO
    st.video(
        "diabetes.mp4",
        autoplay=True,
        muted=True
    )

    # 🧠 HEADLINE
    st.markdown("<h1>This Method Is Helping Diabetics Again</h1>", unsafe_allow_html=True)
    st.markdown("<p>Leave your contact to speak with a specialist</p>", unsafe_allow_html=True)

    # 📋 FORM
    name = st.text_input("", placeholder="Your Name", label_visibility="collapsed")
    phone = st.text_input("", placeholder="Your Phone / WhatsApp", label_visibility="collapsed")

    # 🔥 CTA
    if st.button("📞 ASK FOR A CALL"):
        if not name or not phone:
            st.warning("Please fill in all fields.")
        else:
            try:
                ip = requests.get("https://httpbin.org/ip", timeout=5).json().get("origin", "127.0.0.1")
            except:
                ip = "127.0.0.1"

            result = send_adcombo_order(name, phone, ip)

            if result.get("code") == "ok":
                st.success(f"✅ Request sent successfully! ID: {result['order_id']}")
            else:
                st.error("❌ Something went wrong. Please try again.")

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div style="text-align:center; color:#aaa; font-size:14px; margin-top:40px;">
    © 2025 All Rights Reserved |
    <a href="https://feleo.net/content/shared/html/policy_en.html" target="_blank">Privacy Policy</a> |
    <a href="https://ac-feedback.com/report_form/" target="_blank">Report</a>
    </div>
    """,
    unsafe_allow_html=True
)
