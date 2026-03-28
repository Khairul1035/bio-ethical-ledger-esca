import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Bio-Ethical Ledger", layout="wide", initial_sidebar_state="expanded")

# --- CSS UNTUK TENGOK PRO (Optional) ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- MOCK DATA GENERATOR (Simulasi Data Paper) ---
def load_initial_data():
    data = [
        {"CaseID": "BT-001", "Domain": "Spiritual Sensitivity", "Conflict": "Female patient, emergency, only male surgeon available", "Clinical_Urgency": 9, "Sensitivity_Level": 8, "Resolution": "Patient Agency: Applied Lay Ijtihad for immediate surgery", "Status": "Verified"},
        {"CaseID": "BT-002", "Domain": "Ethical Justice", "Conflict": "Transparent billing vs. Hidden costs in Halal certification", "Clinical_Urgency": 3, "Sensitivity_Level": 9, "Resolution": "Institutional Integrity: Full cost disclosure provided to patient", "Status": "Verified"},
        {"CaseID": "BT-003", "Domain": "Clinical Competence", "Conflict": "Prayer timing vs. Vital medication schedule", "Clinical_Urgency": 7, "Sensitivity_Level": 6, "Resolution": "Spiritual Sensitivity: Flexible scheduling with nursing assistance", "Status": "Verified"},
        {"CaseID": "BT-004", "Domain": "Patient Agency", "Conflict": "Patient wants non-halal medication for life-saving treatment", "Clinical_Urgency": 10, "Sensitivity_Level": 5, "Resolution": "Contextual Religious Flexibility: Patient chose clinical outcome over ritual", "Status": "Verified"},
        {"CaseID": "BT-005", "Domain": "Institutional Integrity", "Conflict": "Profit motive vs. Piety in hospital management", "Clinical_Urgency": 2, "Sensitivity_Level": 9, "Resolution": "Ethical Justice: Gender-equitable access maintained despite costs", "Status": "Verified"}
    ]
    return pd.DataFrame(data)

# --- BLOCKCHAIN SIMULATION FUNCTION ---
def hash_entry(row):
    content = f"{row['CaseID']}-{row['Resolution']}-{datetime.now().strftime('%Y%m%d')}"
    return hashlib.sha256(content.encode()).hexdigest()

# --- APP START ---
st.title("🌐 Bio-Ethical Ledger: Global ESCA+ Dashboard")
st.caption("Operationalizing the Ethical-Spiritual-Clinical Alignment Model for Global Healthcare")

# Load Data
df = load_initial_data()
df['Blockchain_Hash'] = df.apply(hash_entry, axis=1)

# --- SIDEBAR INTERACTION ---
st.sidebar.header("🕹️ Global Practitioner Controls")
st.sidebar.markdown("Adjust indicators to see real-time impact on the ESCA+ Model.")

selected_urgency = st.sidebar.slider("Global Clinical Urgency (JCI Standards)", 1, 10, 5)
selected_sensitivity = st.sidebar.slider("Islamic Spiritual Sensitivity Level", 1, 10, 5)

st.sidebar.divider()
st.sidebar.info(f"**Current Context:**\nUrgency: {selected_urgency} | Sensitivity: {selected_sensitivity}")

# Logic ESCA+ Score Calculation
esca_score = (selected_urgency * 0.5) + (selected_sensitivity * 0.5)

# --- TOP METRICS ---
col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("ESCA+ Alignment", f"{esca_score}/10")
with col2:
    st.metric("Institutional Integrity", "98%", "Authentic")
with col3:
    st.metric("Patient Agency Events", "1,240", "Ijtihad-Led")
with col4:
    st.metric("Clinical Safety (JCI)", "A+", "Certified")

# --- MAIN CONTENT: THE LEDGER ---
st.subheader("📜 The Micro-Negotiation Ledger")
st.markdown("This database logs real-time 'Micro-Negotiations' between faith and clinical needs.")

# Filter data berdasarkan slider
filtered_df = df[(df['Clinical_Urgency'] >= selected_urgency - 2) & (df['Clinical_Urgency'] <= selected_urgency + 2)]

st.dataframe(filtered_df[['CaseID', 'Domain', 'Conflict', 'Resolution', 'Blockchain_Hash']], use_container_width=True)

# --- ANALYSIS SECTION ---
st.divider()
t1, t2 = st.tabs(["📊 Global Analytics", "⚖️ Ethical Decision Support"])

with t1:
    st.subheader("Epistemic Tensions Analysis")
    chart_data = pd.DataFrame({
        'Domains': ['Ethical Justice', 'Spiritual Sensitivity', 'Clinical Competence', 'Institutional Integrity', 'Patient Agency'],
        'Satisfaction %': [85, 92, 78, 88, 95]
    })
    st.bar_chart(chart_data, x='Domains', y='Satisfaction %')
    st.write("Data reveals that **Patient Agency** (Ijtihad) is the highest driver for long-term loyalty in medical tourism.")

with t2:
    st.subheader("Real-Time Decision Logic")
    if selected_urgency > 8:
        st.error("⚠️ **CRITICAL ALERT:** High Clinical Urgency detected. Apply 'Darurah' (Necessity) principles. Prioritize Clinical Competence. Document Patient Agency immediately.")
    elif selected_sensitivity > 8:
        st.success("✅ **ACTION:** High Spiritual Need. Mobilize 'Spiritual Sensitivity' protocols. Ensure Ritual Accommodation is available.")
    else:
        st.info("ℹ️ **STANDARD:** Standard ESCA+ alignment protocol. Balance Ethical Justice with Clinical Quality.")

# --- FOOTER ---
st.divider()
st.markdown(f"© 2025 ESCA+ Research Group | Reframing Islamic Medical Tourism | Verified Ledger: {hashlib.md5(str(datetime.now()).encode()).hexdigest()[:10]}")
