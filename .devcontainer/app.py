import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="XAUUSD Astro Reversal Terminal",
    page_icon="??",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation
st.sidebar.title("?? Astro Terminal")

menu = st.sidebar.radio(
    "Select Terminal",
    [
        "XAUUSD",
        "BTCUSD",
        "NIFTY SENSEX",
        "SWING TRACKER",
        "POWER TIME",
        "POWER 24 BY 7",
        "XAUUSD SMART TIME"
    ]
)

# Main Page
st.title("?? XAUUSD Astro Reversal Terminal")

st.info(
    "?? FOMOKILLER Astro Terminal: "
    "Kripya apni Authorized Gmail ID aur Access Password dalein."
)

# Login Form
with st.container(border=True):

    username = st.text_input("Username (Gmail ID)")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):
        st.error("Please verify your login credentials.")
