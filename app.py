# [EN] Import necessary libraries for web app, data manipulation, and image rendering
# [FA] فراخوانی کتابخانه‌های مورد نیاز برای داشبورد، پردازش داده‌ها و رندر تصاویر
import streamlit as st
import pandas as pd
from PIL import Image
import os

# [EN] Basic web page configuration and layout setting
# [FA] تنظیمات پایه صفحه وب و تعیین چیدمان عریض
st.set_page_config(page_title="RA Resolution Dashboard", page_icon="🧬", layout="wide")

st.title("🧬 ML-Driven Therapeutic Checkpoints in Rheumatoid Arthritis")
st.markdown("""
This interactive dashboard visualizes the computational pipeline to identify therapeutic checkpoints in RA (focusing on the **Resolution of Inflammation** pathway) and proposes novel resolution-promoting agents.
""")

# [EN] Sidebar navigation setup - Structured logically based on research phases
# [FA] تنظیمات منوی ناوبری در نوار کناری - چیدمان منطقی بر اساس فازهای پژوهش
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Select Section:", [
    "1. Exploratory Data Analysis (EDA)", 
    "2. ML Validation & Checkpoints", 
    "3. Drug Candidates (L1000CDS2)"
])

@st.cache_data
def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame()

# ==========================================
# [EN] Section 1: Exploratory Data Analysis
# [FA] بخش اول: تحلیل اکتشافی داده‌ها (PCA, Volcano, Heatmap)
# ==========================================
if menu == "1. Exploratory Data Analysis (EDA)":
    st.subheader("📊 Phase 1: Differential Expression & Data Structure")
    st.write("Visualizing the separation of RA patients from healthy controls and identifying differentially expressed genes (Discovery Dataset: GSE55235).")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("Results/pca_plot.png", caption="PCA: Meaningful separation of RA and Healthy cohorts", use_container_width=True)
    with col2:
        st.image("Results/volcano_plot.png", caption="Volcano Plot: Significant DEGs", use_container_width=True)
        
    st.image("Results/heatmap_plot.png", caption="Clustered Heatmap of Top DEGs", use_container_width=True)

# ==========================================
# [EN] Section 2: Machine Learning & Checkpoints
# [FA] بخش دوم: یادگیری ماشین و نقاط کنترل (Feature Importance, External Validation)
# ==========================================
elif menu == "2. ML Validation & Checkpoints":
    st.subheader("🎯 Phase 2: Therapeutic Checkpoints & Generalizability")
    st.write("Addressing the **Overfitting** research gap: The Random Forest model was trained on the top 15 hub genes and successfully tested on a completely independent external dataset (GSE77298).")
    
    # [EN] Load and display hub genes table
    # [FA] بارگذاری و نمایش جدول ژن‌های هاب
    hub_df = load_data("top_hub_genes.csv")
    if not hub_df.empty:
        st.markdown("**Top 15 Fundamental Bottlenecks (Hubs)**")
        st.dataframe(hub_df.head(15).style.background_gradient(cmap='Blues'), use_container_width=True, hide_index=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("Results/feature_importance.png", caption="Random Forest Feature Importance", use_container_width=True)
    with col2:
        st.image("Results/confusion_matrix.png", caption="External Validation Results (GSE77298)", use_container_width=True)

# ==========================================
# [EN] Section 3: Drug Repurposing Candidates
# [FA] بخش سوم: کاندیداهای بازکاربری دارویی
# ==========================================
elif menu == "3. Drug Candidates (L1000CDS2)":
    st.subheader("💊 Phase 3: Resolution-Promoting Agents")
    st.write("Translating genomic data into pharmacotherapy: Identifying compounds capable of reversing the pathological signature via Reverse Signature Analysis.")
    
    # [EN] Load and display drug candidates table
    # [FA] بارگذاری و نمایش جدول کاندیداهای دارویی
    drug_df = load_data("top_candidate_drugs.csv")
    if not drug_df.empty:
        st.dataframe(drug_df.style.highlight_max(subset=['Match Score'], color='#90EE90'), use_container_width=True, hide_index=True)
    else:
        st.warning("⚠️ File 'top_candidate_drugs.csv' not found.")
