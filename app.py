# [EN] Import necessary libraries for web app and visualization
# [FA] فراخوانی کتابخانه‌های مورد نیاز برای داشبورد تحت وب و تصویرسازی
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# [EN] Basic web page configuration and layout setting
# [FA] تنظیمات پایه صفحه وب و تعیین چیدمان عریض
st.set_page_config(page_title="RA Resolution Dashboard", page_icon="🧬", layout="wide")

# [EN] Main title and description (UI text restricted to English)
# [FA] عنوان اصلی و توضیحات (متن رابط کاربری منحصراً به زبان انگلیسی)
st.title("🧬 ML-Driven Therapeutic Checkpoints in Rheumatoid Arthritis")
st.markdown("""
This interactive dashboard visualizes the results extracted from machine learning algorithms and computational drug repurposing to reverse the pathological signature of Rheumatoid Arthritis (focusing on the **Resolution of Inflammation** pathway).
""")

# [EN] Sidebar navigation setup
# [FA] تنظیمات منوی ناوبری در نوار کناری
st.sidebar.header("Navigation")
menu = st.sidebar.radio("Select Section:", ["1. Hub Genes (Checkpoints)", "2. Drug Candidates (L1000CDS2)"])

# [EN] Secure data loading with caching to optimize performance
# [FA] بارگذاری ایمن داده‌ها با استفاده از قابلیت کش (Cache) برای بهینه‌سازی سرعت
@st.cache_data
def load_data(filename):
    try:
        return pd.read_csv(filename)
    except FileNotFoundError:
        return pd.DataFrame()

# ==========================================
# [EN] Section 1: Therapeutic Checkpoints (Hubs)
# [FA] بخش ۱: نقاط کنترل درمانی (هاب‌ژن‌ها)
# ==========================================
if menu == "1. Hub Genes (Checkpoints)":
    
    # [EN] Section headers and explanations
    # [FA] عناوین و توضیحات بخش اول
    st.subheader("🎯 Top 15 Therapeutic Checkpoints")
    st.write("Identified via **Betweenness Centrality** algorithm and validated by **Random Forest** with 86.96% accuracy in independent external validation.")
    
    # [EN] Load and display the checkpoints dataframe
    # [FA] بارگذاری و نمایش جدول داده‌های نقاط کنترل
    hub_df = load_data("top_hub_genes.csv")
    if not hub_df.empty:
        st.dataframe(hub_df.style.background_gradient(cmap='Blues'), use_container_width=True)
        
        # [EN] Render interactive network centrality plot
        # [FA] رسم نمودار تعاملی مرکزیت شبکه
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.barplot(data=hub_df.head(15), x='Betweenness_Score', y='Gene', hue='Gene', palette='magma', legend=False, ax=ax)
        ax.set_title("Network Centrality of Checkpoints", fontweight='bold')
        ax.set_xlabel("Betweenness Score")
        ax.set_ylabel("Genes")
        st.pyplot(fig)
    else:
        st.warning("⚠️ File 'top_hub_genes.csv' not found in the repository.")

# ==========================================
# [EN] Section 2: Drug Repurposing Candidates
# [FA] بخش ۲: کاندیداهای بازکاربری دارویی
# ==========================================
elif menu == "2. Drug Candidates (L1000CDS2)":
    
    # [EN] Section headers and explanations
    # [FA] عناوین و توضیحات بخش دوم
    st.subheader("💊 Resolution-Promoting Agents")
    st.write("Proposed therapeutic agents designed to reverse the inflammatory profile based on the **Pattern Matching / Reverse Signature** approach.")
    
    # [EN] Load and display the drug candidates dataframe
    # [FA] بارگذاری و نمایش جدول کاندیداهای دارویی
    drug_df = load_data("top_candidate_drugs.csv")
    if not drug_df.empty:
        # [EN] Highlight the highest match scores
        # [FA] برجسته‌سازی بالاترین نمرات تطابق در جدول
        st.dataframe(drug_df.style.highlight_max(subset=['Match Score'], color='#90EE90'), use_container_width=True)
    else:
        st.warning("⚠️ File 'top_candidate_drugs.csv' not found in the repository.")