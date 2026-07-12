import streamlit as st
import joblib
import pandas as pd
import plotly.express as px
import datetime
import os
import sys
import time
import numpy as np

# --- PAGE CONFIG ---
st.set_page_config(page_title="SmartShield AI", page_icon="🛡️", layout="wide")

# --- PROFESSIONAL COMMAND CENTER CSS ---
st.markdown("""
    <style>
    /* Force Dark Theme globally */
    .stApp { background-color: #0e1117 !important; }
    
    /* Metrics: White background, black text for high contrast */
    [data-testid="stMetric"] { 
        background-color: #ffffff !important; 
        padding: 20px; 
        border-radius: 12px; 
        box-shadow: 0 4px 10px rgba(0,0,0,0.3);
    }
    [data-testid="stMetricLabel"], [data-testid="stMetricValue"] { 
        color: #000000 !important; 
    }
    
    /* Headers and Body Text */
    h1, h2, h3, .stMarkdown { color: #ffffff !important; }
    
    /* Table styling */
    .stDataFrame { background: rgba(255,255,255,0.05); }
    </style>
    """, unsafe_allow_html=True)

# --- SETUP ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.preprocessing import clean_text

@st.cache_resource
def load_assets():
    return joblib.load('models/spam_model.pkl'), joblib.load('models/tfidf_vectorizer.pkl')

model, vectorizer = load_assets()

# --- SIDEBAR ---
st.sidebar.markdown("## 🛡️ SmartShield AI")
page = st.sidebar.radio("Navigation", ["Dashboard", "Detection Engine", "History Log"])
st.sidebar.markdown("---")
latency_container = st.sidebar.empty()
latency_container.metric("Latency", "0.00 ms")
st.sidebar.caption("Status: 🟢 Operational")

# --- FUNCTIONS ---
def save_to_history(msg, pred, conf):
    if not os.path.exists('data'): os.makedirs('data')
    file_path = 'data/history.csv'
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if not os.path.exists(file_path):
        pd.DataFrame(columns=['message', 'prediction', 'confidence', 'timestamp']).to_csv(file_path, index=False)
    new_data = pd.DataFrame([[msg, pred, f"{conf:.2f}%", timestamp]], 
                            columns=['message', 'prediction', 'confidence', 'timestamp'])
    new_data.to_csv(file_path, mode='a', header=False, index=False)

# --- MAIN PAGES ---
if page == "Dashboard":
    st.title("📊 Enterprise Command Center")
    if os.path.exists('data/history.csv'):
        df = pd.read_csv('data/history.csv')
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        
        c1, c2, c3 = st.columns(3)
        c1.metric("Total Scans", len(df))
        spam = len(df[df['prediction'] == 'SPAM'])
        c2.metric("Spam Detected", spam)
        c3.metric("Spam Rate", f"{(spam/len(df)*100):.1f}%" if len(df) > 0 else "0%")
        
        st.markdown("<br>", unsafe_allow_html=True)
        st.subheader("Real-time Detection Trend")
        
        trend = df.groupby(df['timestamp'].dt.date).size().reset_index(name='counts')
        fig = px.line(trend, x='timestamp', y='counts', markers=True)
        fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", font_color="#ffffff")
        fig.update_traces(line_color='#00e5ff', marker=dict(size=12, color='#00e5ff'))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("System initializing... Perform a scan to activate the Command Center.")

elif page == "Detection Engine":
    st.title("🛡️ Secure Message Scanner")
    threshold = st.slider("Sensitivity Threshold", 0.5, 0.99, 0.7)
    user_input = st.text_area("Input SMS content:", height=150, placeholder="Paste suspicious message here...")
    
    if st.button("Run Analysis", type="primary"):
        if user_input:
            start = time.time()
            cleaned = clean_text(user_input)
            vec = vectorizer.transform([cleaned])
            
            # XAI Logic
            feature_names = vectorizer.get_feature_names_out()
            dense = vec.todense().tolist()[0]
            phrase_scores = [pair for pair in zip(feature_names, dense) if pair[1] > 0]
            top_words = sorted(phrase_scores, key=lambda x: x[1], reverse=True)[:3]
            
            pred = model.predict(vec)
            conf = float(max(model.predict_proba(vec)[0])) * 100
            
            latency_container.metric("Latency", f"{(time.time()-start)*1000:.2f} ms")
            
            is_spam = pred[0] == 1 and (conf/100) >= threshold
            save_to_history(user_input, "SPAM" if is_spam else "SAFE", conf)
            
            if is_spam: 
                st.error(f"### 🚨 HIGH RISK: SPAM DETECTED ({conf:.2f}%)")
                st.write("**Key factors identified:**", [word for word, score in top_words])
            else: 
                st.success(f"### ✅ STATUS: SECURE (Confidence: {conf:.2f}%)")

elif page == "History Log":
    st.title("📜 Transaction Log")
    if os.path.exists('data/history.csv'):
        df = pd.read_csv('data/history.csv').sort_index(ascending=False)
        st.dataframe(df, use_container_width=True)
        
        # Export Feature
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button("📥 Download Audit Report (CSV)", data=csv, file_name='spam_report.csv', mime='text/csv')
    else:
        st.info("No activity recorded.")
