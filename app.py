import streamlit as st
import pandas as pd
import hashlib
from datetime import datetime

# --- CONFIGURATION ---
st.set_page_config(page_title="ESCA+ Global Ledger", layout="wide")

# --- DATABASE SIMULATION (Session State) ---
# Ini membolehkan data kekal walaupun kita tambah kes baru
if 'ledger_db' not in st.session_state:
    initial_cases = [
        {"CaseID": "ESCA-001", "Domain": "Spiritual Sensitivity", "Conflict": "Patient requests female nurse for maternity care", "Urgency": 4, "Sensitivity": 9, "Resolution": "Ritual Accommodation: Assigned female staff immediately", "Status": "Verified"},
        {"CaseID": "ESCA-002", "Domain": "Clinical Competence", "Conflict": "Delaying life-saving surgery for prayer timing", "Urgency": 10, "Sensitivity": 8, "Resolution": "Patient Agency: Applied 'Darurah' (Necessity) logic for immediate surgery", "Status": "Verified"},
        {"CaseID": "ESCA-003", "Domain": "Ethical Justice", "Conflict": "Pricing transparency for international vs local patients", "Urgency": 2, "Sensitivity": 7, "Resolution": "Fair Administration: Full cost breakdown provided per Maqasid principles", "Status": "Verified"},
        {"CaseID": "ESCA-004", "Domain": "Patient Agency", "Conflict": "Choosing male surgeon in emergency when no female available", "Urgency": 9, "Sensitivity": 5, "Resolution": "Lay Ijtihad: Patient prioritized life over gender-congruent care", "Status": "Verified"},
        {"CaseID": "ESCA-005", "Domain": "Institutional Integrity", "Conflict": "Marketing 'Halal' but lacking staff training in Islamic ethics", "Urgency": 3, "Sensitivity": 9, "Resolution": "Structural Ethics: Mandatory staff bio-ethics training implemented", "Status": "Verified"},
        {"CaseID": "ESCA-006", "Domain": "Spiritual Sensitivity", "Conflict": "Request for Halal-certified Insulin/Heparin", "Urgency": 6, "Sensitivity": 8, "Resolution": "Clinical-Spiritual Alignment: Provided certified alternative or explained necessity", "Status": "Verified"},
        {"CaseID": "ESCA-007", "Domain": "Clinical Competence", "Conflict": "JCI efficiency vs Islamic modesty protocols in MRI", "Urgency": 5, "Sensitivity": 9, "Resolution": "Negotiated System: Modified MRI gown to ensure maximum coverage", "Status": "Verified"},
        {"CaseID": "ESCA-008", "Domain": "Ethical Justice", "Conflict": "Gender-equitable access to specialized kidney treatment", "Urgency": 7, "Sensitivity": 6, "Resolution": "Islamic Equity: Resource distribution based on clinical need, not gender", "Status": "Verified"},
        {"CaseID": "ESCA-009", "Domain": "Patient Agency", "Conflict": "Patient interpreting 'Fiqh' to refuse fasting during meds", "Urgency": 8, "Sensitivity": 7, "Resolution": "Contextual Flexibility: Doctor-Patient negotiation on health priority", "Status": "Verified"},
        {"CaseID": "ESCA-010", "Domain": "Institutional Integrity", "Conflict": "Profit-driven regime vs Maqasid Al-Shariah values", "Urgency": 1, "Sensitivity": 10, "Resolution": "Ethical Framework: Strategic shift from symbolic to systemic Shariah governance", "Status": "Verified"}
    ]
    st.session_state.ledger_db = pd.DataFrame(initial_cases)

# --- FUNCTIONS ---
def generate_hash(row):
    content = f"{row['CaseID']}-{row['Resolution']}-{datetime.now()}"
    return hashlib.sha256(content.encode()).hexdigest()

# --- APP START ---
st.title("🌐 Bio-Ethical Ledger: Global ESCA+ Dashboard")
st.markdown("### Reframing Islamic Medical Tourism through the ESCA+ Ethics Model")

# --- SIDEBAR: GLOBAL CONTROLS ---
st.sidebar.header("🕹️ Practitioner Controls")
selected_urgency = st.sidebar.slider("Global Clinical Urgency (JCI)", 1, 10, 5)
selected_sensitivity = st.sidebar.slider("Spiritual Sensitivity Level", 1, 10, 5)

# --- TABS: VIEW LEDGER & SUBMIT CASE ---
tab1, tab2, tab3 = st.tabs(["📜 View Ledger", "📥 Submit New Case", "📊 Global Analytics"])

with tab1:
    st.subheader("The Immutable Micro-Negotiation Ledger")
    # Apply Hash for visual
    display_df = st.session_state.ledger_db.copy()
    display_df['Blockchain_Hash'] = display_df.apply(generate_hash, axis=1)
    
    # Filter display based on slider
    filt_df = display_df[(display_df['Urgency'] >= selected_urgency-2) & (display_df['Urgency'] <= selected_urgency+2)]
    st.dataframe(filt_df, use_container_width=True)

with tab2:
    st.subheader("Log a New Micro-Negotiation")
    with st.form("new_case_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            new_id = st.text_input("Case ID", value=f"ESCA-0{len(st.session_state.ledger_db)+1}")
            new_domain = st.selectbox("ESCA+ Domain", ["Spiritual Sensitivity", "Clinical Competence", "Ethical Justice", "Institutional Integrity", "Patient Agency"])
            new_urgency = st.slider("Clinical Urgency", 1, 10, 5)
        with col_b:
            new_conflict = st.text_area("Ethical Conflict Description")
            new_sensitivity = st.slider("Religious Sensitivity", 1, 10, 5)
            new_resolution = st.text_input("Resolution/Decision Reached")
        
        submit_button = st.form_submit_button("Submit to Ledger")
        
        if submit_button:
            new_data = {
                "CaseID": new_id,
                "Domain": new_domain,
                "Conflict": new_conflict,
                "Urgency": new_urgency,
                "Sensitivity": new_sensitivity,
                "Resolution": new_resolution,
                "Status": "Pending Verification"
            }
            # Append to session state
            st.session_state.ledger_db = pd.concat([st.session_state.ledger_db, pd.DataFrame([new_data])], ignore_index=True)
            st.success(f"Case {new_id} has been securely hashed and added to the Global Ledger!")
            st.balloons()

with tab3:
    st.subheader("Operational Analytics")
    col1, col2 = st.columns(2)
    with col1:
        st.write("Domain Distribution")
        st.bar_chart(st.session_state.ledger_db['Domain'].value_counts())
    with col2:
        st.write("Avg Urgency per Domain")
        avg_urgency = st.session_state.ledger_db.groupby('Domain')['Urgency'].mean()
        st.line_chart(avg_urgency)

# --- FOOTER DECISION SUPPORT ---
st.divider()
st.subheader("⚖️ AI-Assisted Decision Support")
avg_score = (selected_urgency + selected_sensitivity) / 2
if avg_score > 8:
    st.error("⚠️ **POLICY ALERT:** High tension between Clinical Necessity and Spiritual Value. Recommendation: Activate 'Patient Agency' protocol (Ijtihad).")
elif avg_score > 5:
    st.warning("⚠️ **ADVISORY:** Moderate tension. Recommendation: Negotiate 'Spiritual Sensitivity' through institutional sincerity.")
else:
    st.info("ℹ️ **STABLE:** Low tension. Follow standard Shariah-compliant SOP.")
