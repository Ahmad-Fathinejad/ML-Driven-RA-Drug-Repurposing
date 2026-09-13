# [EN] Import necessary libraries for web app and visualization
# [FA] فراخوانی کتابخانه‌های مورد نیاز برای داشبورد تحت وب و تصویرسازی
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# [EN] Basic web page configuration and layout setting
# [FA] تنظیمات پایه صفحه وب و تعیین چیدمان عریض
st.set_page_config(page_title="RA Resolution Dashboard", page_icon="🧬", layout="wide")

# [EN] Main title and description
# [FA] عنوان اصلی و توضیحات 
st.title("🧬 ML-Driven Therapeutic Checkpoints in Rheumatoid Arthritis")
st.markdown("""
This interactive dashboard visualizes the results extracted from machine learning algorithms and computational drug repurposing to reverse the pathological signature of Rheumatoid Arthritis (focusing on the **Resolution of Inflammation** pathway).
""")

# [EN] Sidebar navigation setup
# [FA] تنظیمات منوی ناوبری در نوار کناری
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Select Section:", ["1. Hub Genes (Checkpoints)", "2. Drug Candidates (L1000CDS2)"])

@st.cache_data
def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame()

# ==========================================
# [EN] Section 1: Therapeutic Checkpoints (Hubs)
# ==========================================
if menu == "1. Hub Genes (Checkpoints)":
    
    st.subheader("🎯 Top 15 Therapeutic Checkpoints")
    st.write("Identified via **Betweenness Centrality** algorithm and validated by **Random Forest** with 86.96% accuracy in independent external validation.")
    
    hub_df = load_data("top_hub_genes.csv")
    if not hub_df.empty:
        # فیلتر کردن 15 ردیف اول و تنظیم اندیس برای شروع از عدد 1
        top_15_hubs = hub_df.head(15).copy()
        top_15_hubs.index = range(1, len(top_15_hubs) + 1)
        
        st.dataframe(top_15_hubs.style.background_gradient(cmap='Blues'), use_container_width=True)
        
        # رسم نمودار تعاملی
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=top_15_hubs, x='Betweenness_Score', y='Gene', hue='Gene', palette='magma', legend=False, ax=ax)
        ax.set_title("Network Centrality of Checkpoints", fontweight='bold')
        ax.set_xlabel("Betweenness Score")
        ax.set_ylabel("Genes")
        st.pyplot(fig)
    else:
        st.warning("⚠️ File 'top_hub_genes.csv' not found in the repository.")

# ==========================================
# [EN] Section 2: Drug Repurposing Candidates
# ==========================================
elif menu == "2. Drug Candidates (L1000CDS2)":
    
    st.subheader("💊 Resolution-Promoting Agents")
    st.write("Proposed therapeutic agents designed to reverse the inflammatory profile based on the **Pattern Matching / Reverse Signature** approach.")
    
    drug_df = load_data("top_candidate_drugs.csv")
    if not drug_df.empty:
        # تنظیم اندیس برای شروع از عدد 1
        drug_df.index = range(1, len(drug_df) + 1)
        st.dataframe(drug_df.style.highlight_max(subset=['Match Score'], color='#90EE90'), use_container_width=True)
    else:
        st.warning("⚠️ File 'top_candidate_drugs.csv' not found in the repository.")
