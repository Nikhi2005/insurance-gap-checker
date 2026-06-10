import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(
    page_title="Insurance Policy Issuance Checker",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ Insurance Policy Issuance Checker")
st.subheader("Upload policy documents to detect gaps before binding")

st.divider()

uploaded_files = st.file_uploader(
    "Upload Documents (PDF or Image)",
    type=["pdf", "png", "jpg", "jpeg"],
    accept_multiple_files=True
)

if uploaded_files:
    st.success(f"✅ {len(uploaded_files)} file(s) uploaded!")
    for file in uploaded_files:
        st.write(f"📄 {file.name} — {round(file.size/1024, 1)} KB")
else:
    st.info("📂 Please upload: Proposal Form, KYC, Payment Receipt, Nominee Form")

st.divider()
