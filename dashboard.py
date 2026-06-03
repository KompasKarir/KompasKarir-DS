import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# ==================== PAGE CONFIGURATION ====================
st.set_page_config(
    page_title="Kompas Karir - RIASEC Career Guide",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CUSTOM STYLING - KOMPAS KARIR DARK MODE ====================
st.markdown("""
<style>
    /* Main container styling - Pure dark background */
    .main {
        padding-top: 1rem;
        background: #0a0f0d;
    }
    
    /* Hide streamlit default elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* Header styling - Teal accent for main title */
    .header-title {
        text-align: center;
        padding: 2.5rem 2rem;
        background: linear-gradient(135deg, #10a396 0%, #0d7d74 100%);
        color: #ffffff;
        border-radius: 15px;
        margin-bottom: 2rem;
        box-shadow: 0 8px 25px rgba(16, 163, 150, 0.35);
    }
    
    .header-title h1 {
        margin: 0;
        font-size: 2.5em;
        font-weight: 700;
        color: #ffffff;
        letter-spacing: 1px;
    }
    
    .header-title p {
        margin: 0.8rem 0 0 0;
        font-size: 1.05em;
        color: rgba(255, 255, 255, 0.95);
        font-weight: 500;
    }
    
    /* Logo styling */
    .logo-container {
        text-align: center;
        margin-bottom: 1.5rem;
    }
    
    .logo-container img {
        max-width: 150px;
        height: auto;
        filter: drop-shadow(0 0 15px rgba(16, 163, 150, 0.4));
    }
    
    /* Metric card styling - Dark with teal accent border */
    .metric-card {
        background: #141a17;
        padding: 1.5rem;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
        border-left: 5px solid #10a396;
        border-top: 1px solid rgba(16, 163, 150, 0.2);
        transition: transform 0.3s, box-shadow 0.3s;
        color: #e8e8e8;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 20px rgba(16, 163, 150, 0.25);
        border-top: 1px solid rgba(16, 163, 150, 0.4);
    }
    
    /* Section headers - Teal color dengan garis bawah */
    h2 {
        color: #10a396;
        padding-bottom: 1rem;
        border-bottom: 3px solid #10a396;
        font-size: 1.8em;
        font-weight: 700;
        margin-top: 2rem;
        margin-bottom: 1.5rem;
        letter-spacing: 0.5px;
    }
    
    h3 {
        color: #2dd4c0;
        font-size: 1.3em;
        font-weight: 600;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    h4 {
        color: #b0d4d0;
        font-size: 1.1em;
        font-weight: 600;
    }
    
    /* Info card - Subtle teal accent */
    .info-card {
        background: linear-gradient(135deg, #1a2420 0%, #142420 100%);
        padding: 1.2rem;
        border-radius: 10px;
        border-left: 4px solid #10a396;
        border-top: 1px solid rgba(16, 163, 150, 0.15);
        margin: 1rem 0;
        color: #d8d8d8;
    }
    
    /* Tab styling - Teal highlight untuk active tab */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 1.05em;
        font-weight: 600;
        color: #a8a8a8;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #10a396;
        border-bottom-color: #10a396;
        font-weight: 700;
    }
    
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"]::after {
        background-color: #10a396 !important;
    }
    
    /* Dataframe styling */
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
        background: #141a17;
    }
    
    /* Sidebar styling */
    .sidebar-content {
        background: #141a17;
        padding: 1.5rem;
        border-radius: 10px;
        margin-bottom: 1.5rem;
        color: #d8d8d8;
    }
    
    /* Button styling - Teal dengan white text untuk clarity */
    .stButton > button {
        background: linear-gradient(135deg, #10a396 0%, #0d7d74 100%);
        color: #ffffff !important;
        border: none;
        border-radius: 8px;
        font-weight: 700;
        font-size: 1em;
        transition: all 0.3s;
        box-shadow: 0 4px 12px rgba(16, 163, 150, 0.3);
        padding: 0.7rem 1.5rem !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(16, 163, 150, 0.4);
        background: linear-gradient(135deg, #0d7d74 0%, #0a5f5a 100%) !important;
    }
    
    /* Select box, multiselect, radio styling */
    .stSelectbox, .stMultiSelect, .stRadio {
        background: transparent;
    }
    
    .stSelectbox > div > div,
    .stMultiSelect > div > div {
        background: #141a17 !important;
        border: 1px solid rgba(16, 163, 150, 0.3) !important;
        border-radius: 6px !important;
    }
    
    /* Input fields */
    input, textarea, select {
        background-color: #141a17 !important;
        color: #e8e8e8 !important;
        border: 1px solid rgba(16, 163, 150, 0.3) !important;
        border-radius: 6px !important;
        padding: 0.5rem !important;
    }
    
    input::placeholder {
        color: #808080 !important;
    }
    
    /* Success/Error/Info boxes dengan teal accent */
    .stSuccess {
        background-color: #0d2818;
        color: #4cff99;
        border-radius: 8px;
        border-left: 4px solid #10a396;
        border-top: 1px solid rgba(16, 163, 150, 0.2);
    }
    
    .stError {
        background-color: #2d0d0d;
        color: #ff8888;
        border-radius: 8px;
        border-left: 4px solid #ff6b6b;
        border-top: 1px solid rgba(255, 107, 107, 0.2);
    }
    
    .stInfo {
        background-color: #0d1f2d;
        color: #7dd4ff;
        border-radius: 8px;
        border-left: 4px solid #10a396;
        border-top: 1px solid rgba(16, 163, 150, 0.2);
    }
    
    .stWarning {
        background-color: #2d2010;
        color: #ffc266;
        border-radius: 8px;
        border-left: 4px solid #ffa500;
    }
    
    /* Divider styling - Teal gradient */
    hr {
        border: 0;
        height: 2px;
        background: linear-gradient(to right, transparent, rgba(16, 163, 150, 0.5), transparent);
        margin: 2rem 0;
    }
    
    /* Text color untuk readability */
    .stMarkdown, p, label, span {
        color: #d8d8d8;
    }
    
    /* Links styling */
    a {
        color: #10a396 !important;
        text-decoration: underline;
    }
    
    a:hover {
        color: #2dd4c0 !important;
    }
    
    /* Checkbox & radio styling */
    [data-baseweb="checkbox"], [data-baseweb="radio"] {
        color: #d8d8d8;
    }
    
    /* Sidebar header dengan logo */
    .sidebar-header {
        text-align: center;
        padding: 1.5rem 0;
        border-bottom: 2px solid #10a396;
        margin-bottom: 1.5rem;
    }
    
    .sidebar-header img {
        max-width: 120px;
        height: auto;
        margin-bottom: 1rem;
        filter: drop-shadow(0 0 12px rgba(16, 163, 150, 0.4));
    }
    
    .sidebar-header h1 {
        font-size: 1.5em;
        color: #10a396;
        margin: 0;
        font-weight: 700;
        letter-spacing: 1px;
    }
    
    .sidebar-header p {
        font-size: 0.9em;
        color: #a0a0a0;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
    }
    
    /* Metric label styling - Clear teal for section titles */
    .metric-label {
        color: #10a396;
        font-weight: 700;
        font-size: 1.2em;
        margin-bottom: 0.5rem;
    }
    
    .metric-value {
        color: #ffffff;
        font-weight: 700;
        font-size: 1.5em;
        margin-bottom: 0.5rem;
    }
    
    .metric-sublabel {
        color: #a0a0a0;
        font-size: 0.9em;
        margin-top: 0.5rem;
    }
    
    /* Chart styling */
    .stPlotlyChart, .stMatplotlibChart {
        border-radius: 10px;
        background: #141a17;
        padding: 1rem;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }
    
    /* Table styling */
    .stDataFrame, table {
        background: #141a17 !important;
        color: #d8d8d8 !important;
    }
    
    table th {
        background: rgba(16, 163, 150, 0.2) !important;
        color: #10a396 !important;
        font-weight: 700;
    }
    
    table td {
        color: #d8d8d8 !important;
        border-color: rgba(16, 163, 150, 0.1) !important;
    }
    
    table tr:hover {
        background: rgba(16, 163, 150, 0.1) !important;
    }
    
    /* Expander styling */
    .stExpander {
        background: #141a17 !important;
        border: 1px solid rgba(16, 163, 150, 0.2) !important;
        border-radius: 8px !important;
    }
    
    /* Sidebar filter statistics */
    .filter-stats {
        background: linear-gradient(135deg, rgba(16, 163, 150, 0.1) 0%, rgba(13, 125, 116, 0.1) 100%);
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid rgba(16, 163, 150, 0.3);
        margin: 1rem 0;
        color: #d8d8d8;
    }
    
    .filter-stats-title {
        color: #10a396;
        font-weight: 700;
        font-size: 1.1em;
        margin-bottom: 0.5rem;
    }
    
    .filter-stats-value {
        color: #ffffff;
        font-weight: 700;
        font-size: 1.3em;
    }
    
    /* Scrollbar styling untuk matches browser theme */
    ::-webkit-scrollbar {
        width: 8px;
        height: 8px;
    }
    
    ::-webkit-scrollbar-track {
        background: #0a0f0d;
    }
    
    ::-webkit-scrollbar-thumb {
        background: #10a396;
        border-radius: 4px;
    }
    
    ::-webkit-scrollbar-thumb:hover {
        background: #0d7d74;
    }
</style>
""", unsafe_allow_html=True)

# ==================== DATA LOADING & CACHING ====================
@st.cache_data
def load_data():
    """Load and preprocess the RIASEC dataset"""
    # Get the dataset directory path - handle both relative and absolute paths
    try:
        # Try relative path first
        dataset_path = Path("Dataset")
        if not dataset_path.exists():
            # Try absolute path
            dataset_path = Path(__file__).parent / "Dataset"
        if not dataset_path.exists():
            # Try current working directory
            dataset_path = Path.cwd() / "Dataset"
    except:
        dataset_path = Path("Dataset")
    
    # Try loading the processed dataset first
    dataset_file = "riasec_dataset_processed.csv"

    df = None
    riasec_file = dataset_path / dataset_file
    if riasec_file.exists():
        try:
            df = pd.read_csv(riasec_file)
            print(f"✓ Loaded: {dataset_file}")
        except Exception as e:
            st.sidebar.warning(f"⚠ Could not load {dataset_file}: {str(e)}")
    
    if df is None:
        st.error(f"""
        ❌ No RIASEC dataset found!
        
        Expected location: {dataset_path.absolute()}
        
        Please ensure one of these files exists:
        - riasec_ml_ready.csv
        - riasec_dataset_processed.csv
        - riasec_dataset_raw.csv
        """)
        st.stop()
    
    # Ensure required columns exist
    required_cols = ['student_id', 'program_name', 'riasec_primary_type', 
                     'riasec_primary_score', 'academic_overall']
    
    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        # Try to create missing columns if we have raw data
        df = process_riasec_data(df)
    
    return df

def process_riasec_data(df):
    """Process raw RIASEC data to extract key features"""
    # Calculate RIASEC scores if not present
    if 'riasec_r_raw' not in df.columns:
        riasec_types = ['r', 'i', 'a', 's', 'e', 'c']
        for riasec_type in riasec_types:
            cols = [col for col in df.columns if f'riasec_{riasec_type}_item' in col]
            if cols:
                df[f'riasec_{riasec_type}_raw'] = df[cols].sum(axis=1)
    
    # Determine primary RIASEC type
    riasec_raw_cols = ['riasec_r_raw', 'riasec_i_raw', 'riasec_a_raw', 
                       'riasec_s_raw', 'riasec_e_raw', 'riasec_c_raw']
    riasec_raw_cols = [col for col in riasec_raw_cols if col in df.columns]
    
    if riasec_raw_cols:
        df['riasec_primary_type'] = df[riasec_raw_cols].idxmax(axis=1).str.replace('riasec_', '').str.replace('_raw', '').str.upper()
        df['riasec_primary_score'] = df[riasec_raw_cols].max(axis=1)
    
    # Calculate academic performance
    academic_cols = [col for col in df.columns if 'academic_' in col]
    if academic_cols:
        df['academic_overall'] = df[academic_cols].mean(axis=1)
    
    return df

# ==================== LOAD DATA ====================
df = load_data()

# ==================== SIDEBAR CONFIGURATION ====================
with st.sidebar:
    # Logo dan Title Kompas Karir
    try:
        from PIL import Image
        logo = Image.open("logo-kompas-karir.png")
        col1, col2 = st.columns([1, 2])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.markdown("""
            <div style='margin-top: 1rem;'>
                <h3 style='color: #10a396; margin: 0; font-size: 1.3em;'>Kompas Karir</h3>
                <p style='color: #b0b0b0; margin: 0.2rem 0 0 0; font-size: 0.85em;'>RIASEC Career Guide</p>
            </div>
            """, unsafe_allow_html=True)
    except:
        st.markdown("""
        <div style='text-align: center; padding: 1.5rem 0; background: linear-gradient(135deg, #10a396 0%, #0d7d74 100%); 
                    border-radius: 10px; margin-bottom: 2rem;'>
            <h2 style='color: white; margin: 0;'> Kompas Karir</h2>
            <p style='color: rgba(255,255,255,0.8); margin: 0.3rem 0 0 0; font-size: 0.9em;'>RIASEC Career Guide System</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Page selection
    page = st.radio(
        "📍 **Pilih Halaman:**",
        [" Ringkasan", " Tipe Kepribadian", " Performa Akademik", 
         " Distribusi Program Studi", " Profil Siswa"],
        label_visibility="collapsed"
    )
    
    # Filters section
    st.markdown("---")
    st.markdown("#### Filter Data")
    
    riasec_types = sorted(df['riasec_primary_type'].unique())
    riasec_names = {
        'R': ' Realistic (Praktis)',
        'I': ' Investigative (Analitis)',
        'A': ' Artistic (Kreatif)',
        'S': ' Social (Sosial)',
        'E': ' Enterprising (Bisnis)',
        'C': ' Conventional (Teratur)'
    }
    
    selected_riasec = st.multiselect(
        "Tipe Kepribadian RIASEC:",
        riasec_types,
        default=riasec_types,
        format_func=lambda x: riasec_names.get(x, x)
    )
    
    st.markdown("")  # Spacer
    
    # Use all programs (no filter)
    programs = sorted(df['program_name'].unique())
    selected_programs = programs  # Default ke semua program studi
    
    # Apply filters
    filtered_df = df[
        (df['riasec_primary_type'].isin(selected_riasec)) &
        (df['program_name'].isin(selected_programs))
    ]
    
    # Filter stats
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.metric(" Data Terpilih", len(filtered_df), delta=None)
    with col2:
        st.metric(" % dari Total", f"{len(filtered_df)/len(df)*100:.1f}%", delta=None)
    
    # Reset button
    if st.button("Reset Filter", use_container_width=True):
        st.rerun()

# ==================== PAGE: OVERVIEW ====================
if page == " Ringkasan":
    # Header
    st.markdown("""
    <div class='header-title'>
        <h1>Ringkasan Dashboard RIASEC</h1>
        <p>Analisis Kepribadian & Performa Akademik Siswa</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-top: 0;'> Total Siswa</h3>
            <h2 style='margin: 0.5rem 0; color: white;'>{len(filtered_df):,}</h2>
            <p style='color: #999; margin: 0; font-size: 0.9em;'>dari {len(df):,} total</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-top: 0;'> Tipe RIASEC</h3>
            <h2 style='margin: 0.5rem 0; color: white;'>{filtered_df['riasec_primary_type'].nunique()}</h2>
            <p style='color: #999; margin: 0; font-size: 0.9em;'>Macam kepribadian</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-top: 0;'> Program Studi</h3>
            <h2 style='margin: 0.5rem 0; color: white;'>{filtered_df['program_name'].nunique()}</h2>
            <p style='color: #999; margin: 0; font-size: 0.9em;'>Program tersedia</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        avg_score = filtered_df['academic_overall'].mean()
        st.markdown(f"""
        <div class='metric-card'>
            <h3 style='color: #667eea; margin-top: 0;'> Nilai Akademik</h3>
            <h2 style='margin: 0.5rem 0; color: white;'>{avg_score:.1f}</h2>
            <p style='color: #999; margin: 0; font-size: 0.9em;'>Rata-rata dari 100</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main visualizations
    st.markdown("---")
    st.markdown("###  Visualisasi Data")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("####  Distribusi Tipe Kepribadian")
        riasec_counts = filtered_df['riasec_primary_type'].value_counts().sort_index()
        
        # Add names to labels
        riasec_labels = [f"{riasec_names.get(t, t)}\n({t})\n{count} siswa" 
                        for t, count in riasec_counts.items()]
        
        fig, ax = plt.subplots(figsize=(9, 5.5))
        colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
        bars = ax.bar(riasec_counts.index, riasec_counts.values, color=colors[:len(riasec_counts)])
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height,
                   f'{int(height)}',
                   ha='center', va='bottom', fontweight='bold', fontsize=10)
        
        ax.set_xlabel("Tipe Kepribadian", fontsize=11, fontweight='bold')
        ax.set_ylabel("Jumlah Siswa", fontsize=11, fontweight='bold')
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        plt.tight_layout()
        st.pyplot(fig)
    
    with col2:
        st.markdown("####  Distribusi Nilai Akademik")
        fig, ax = plt.subplots(figsize=(9, 5.5))
        
        academic_scores = filtered_df['academic_overall'].dropna()
        n, bins, patches = ax.hist(academic_scores, bins=20, color='#667eea', 
                                    edgecolor='black', alpha=0.7)
        
        # Color gradient for bins
        for i, patch in enumerate(patches):
            patch.set_facecolor(plt.cm.viridis(i / len(patches)))
        
        mean_score = academic_scores.mean()
        median_score = academic_scores.median()
        
        ax.axvline(mean_score, color='red', linestyle='--', linewidth=2.5, 
                  label=f'Mean: {mean_score:.1f}')
        ax.axvline(median_score, color='green', linestyle='--', linewidth=2.5, 
                  label=f'Median: {median_score:.1f}')
        
        ax.set_xlabel("Nilai Akademik", fontsize=11, fontweight='bold')
        ax.set_ylabel("Jumlah Siswa", fontsize=11, fontweight='bold')
        ax.legend(fontsize=10)
        ax.grid(axis='y', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        plt.tight_layout()
        st.pyplot(fig)
    
    # Additional insights
    st.markdown("---")
    st.markdown("###  Wawasan Utama")
    
    col1, col2 = st.columns(2)
    
    with col1:
        top_riasec = filtered_df['riasec_primary_type'].value_counts().idxmax()
        top_count = filtered_df['riasec_primary_type'].value_counts().max()
        st.markdown(f"""
        <div class='info-card'>
            <h4 style='margin-top: 0; color: #667eea;'> Tipe Terbanyak</h4>
            <p style='font-size: 1.3em; margin: 0.5rem 0; font-weight: bold; color: white;'>{riasec_names.get(top_riasec, top_riasec)}</p>
            <p style='color: white; margin: 0; font-size: 0.9em;'>{top_count} siswa ({top_count/len(filtered_df)*100:.1f}%)</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        top_program = filtered_df['program_name'].value_counts().idxmax()
        top_prog_count = filtered_df['program_name'].value_counts().max()
        st.markdown(f"""
        <div class='info-card'>
            <h4 style='margin-top: 0; color: #667eea;'> Program Terpilih</h4>
            <p style='font-size: 1.2em; margin: 0.5rem 0; font-weight: bold; color: white;'>{top_program}</p>
            <p style='color: white; margin: 0; font-size: 0.9em;'>{top_prog_count} siswa ({top_prog_count/len(filtered_df)*100:.1f}%)</p>
        </div>
        """, unsafe_allow_html=True)
    

# ==================== PAGE: RIASEC ANALYSIS ====================
elif page == " Tipe Kepribadian":
    # Header
    st.markdown("""
    <div class='header-title'>
        <h1> Analisis Tipe Kepribadian RIASEC</h1>
        <p>Pahami 6 Dimensi Kepribadian Karir Anda</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class='info-card'>
        <h4 style='margin-top: 0;'> Model RIASEC Adalah:</h4>
        Model kepribadian karir yang terdiri dari 6 tipe utama. Setiap orang memiliki kombinasi unik 
        dari tipe-tipe ini yang menentukan minat dan kecocokan karir mereka.
    </div>
    """, unsafe_allow_html=True)
    
    riasec_descriptions = {
        'R': {
            'name': ' Realistic (Realistis)',
            'desc': 'Praktis, hands-on, technical, suka bekerja dengan benda/mesin',
            'color': '#1f77b4'
        },
        'I': {
            'name': ' Investigative (Investigatif)',
            'desc': 'Analitis, saintifik, suka penelitian dan pemecahan masalah kompleks',
            'color': '#ff7f0e'
        },
        'A': {
            'name': ' Artistic (Artistik)',
            'desc': 'Kreatif, ekspresif, inovatif, suka mengekspresikan diri melalui seni',
            'color': '#2ca02c'
        },
        'S': {
            'name': ' Social (Sosial)',
            'desc': 'People-oriented, komunikatif, suka membantu dan bekerja dengan orang lain',
            'color': '#d62728'
        },
        'E': {
            'name': ' Enterprising (Bisnis)',
            'desc': 'Leadership, ambisius, persuasif, suka memimpin dan berbisnis',
            'color': '#9467bd'
        },
        'C': {
            'name': ' Conventional (Konvensional)',
            'desc': 'Terorganisir, detail-oriented, suka struktur dan tata tertib',
            'color': '#8c564b'
        }
    }
    
    # Create tabs for each RIASEC type
    tabs = st.tabs([riasec_descriptions[t]['name'] for t in ['R', 'I', 'A', 'S', 'E', 'C']])
    
    for tab, riasec_type in zip(tabs, ['R', 'I', 'A', 'S', 'E', 'C']):
        with tab:
            type_data = filtered_df[filtered_df['riasec_primary_type'] == riasec_type]
            desc_info = riasec_descriptions[riasec_type]
            
            # Description card
            st.markdown(f"""
            <div class='info-card' style='border-left-color: {desc_info["color"]};'>
                <p style='margin: 0; font-size: 1.05em; color: white;'>{desc_info["desc"]}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if len(type_data) > 0:
                # Statistics
                st.markdown(f"####  Statistik Tipe {riasec_type}")
                col1, col2, col3, col4 = st.columns(4)
                
                with col1:
                    st.markdown(f"""
                    <div class='metric-card'>
                        <h3 style='color: {desc_info["color"]}; margin-top: 0;'>Jumlah</h3>
                        <h2 style='margin: 0.5rem 0; color: white;'>{len(type_data):,}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col2:
                    pct = (len(type_data)/len(filtered_df)*100) if len(filtered_df) > 0 else 0
                    st.markdown(f"""
                    <div class='metric-card'>
                        <h3 style='color: {desc_info["color"]}; margin-top: 0;'>% Total</h3>
                        <h2 style='margin: 0.5rem 0; color: white;'>{pct:.1f}%</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col3:
                    avg_score = type_data['academic_overall'].mean()
                    st.markdown(f"""
                    <div class='metric-card'>
                        <h3 style='color: {desc_info["color"]}; margin-top: 0;'>Nilai Rata-rata</h3>
                        <h2 style='margin: 0.5rem 0; color: white;'>{avg_score:.1f}</h2>
                    </div>
                    """, unsafe_allow_html=True)
                
                with col4:
                    top_prog = type_data['program_name'].value_counts().index[0] if len(type_data) > 0 else "N/A"
                    top_prog_count = type_data['program_name'].value_counts().values[0] if len(type_data) > 0 else 0
                    st.markdown(f"""
                    <div class='metric-card'>
                        <h3 style='color: {desc_info["color"]}; margin-top: 0;'>Program Top</h3>
                        <p style='font-size: 0.85em; margin: 0.3rem 0; font-weight: bold;'>{top_prog[:20]}...</p>
                        <p style='color: white; margin: 0; font-size: 0.85em;'>{top_prog_count} siswa</p>
                    </div>
                    """, unsafe_allow_html=True)
                
                # Top Programs
                st.markdown("---")
                st.markdown("####  Program Studi Terpopuler")
                
                top_programs = type_data['program_name'].value_counts().head(10)
                
                if len(top_programs) > 0:
                    fig, ax = plt.subplots(figsize=(11, 6))
                    bars = ax.barh(range(len(top_programs)), top_programs.values, 
                                   color=desc_info['color'], alpha=0.8)
                    
                    # Add value labels
                    for i, (bar, value) in enumerate(zip(bars, top_programs.values)):
                        ax.text(value, i, f' {int(value)} siswa', 
                               va='center', fontweight='bold', fontsize=9)
                    
                    ax.set_yticks(range(len(top_programs)))
                    ax.set_yticklabels(top_programs.index, fontsize=9)
                    ax.set_xlabel("Jumlah Siswa", fontsize=10, fontweight='bold')
                    ax.set_title(f"Program Favorit Tipe {riasec_type}", fontsize=11, fontweight='bold')
                    ax.grid(axis='x', alpha=0.3, linestyle='--')
                    ax.set_axisbelow(True)
                    plt.tight_layout()
                    st.pyplot(fig)
            else:
                st.warning(f"❌ Tidak ada siswa dengan tipe {riasec_type} dalam filter saat ini")

# ==================== PAGE: ACADEMIC PERFORMANCE ====================
elif page == " Performa Akademik":
    # Header
    st.markdown("""
    <div class='header-title'>
        <h1> Analisis Performa Akademik</h1>
        <p>Hubungan antara Tipe Kepribadian dan Prestasi Akademik</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Academic performance by RIASEC type
    st.markdown("###  Performa Akademik per Tipe Kepribadian")
    
    col1, col2 = st.columns([1.2, 1])
    
    with col1:
        fig, ax = plt.subplots(figsize=(11, 6))
        riasec_academic = filtered_df.groupby('riasec_primary_type')['academic_overall'].agg(['mean', 'std', 'count'])
        
        if len(riasec_academic) > 0:
            colors_map = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
            riasec_order = ['R', 'I', 'A', 'S', 'E', 'C']
            riasec_academic = riasec_academic.reindex([t for t in riasec_order if t in riasec_academic.index])
            
            bars = ax.bar(range(len(riasec_academic)), riasec_academic['mean'], 
                         color=colors_map[:len(riasec_academic)], alpha=0.8)
            
            # Error bars
            
            # Add value labels
            for i, (idx, row) in enumerate(riasec_academic.iterrows()):
                ax.text(i, row['mean'] + row['std'] + 2, f"{row['mean']:.1f}", 
                       ha='center', fontweight='bold', fontsize=10)
            
            ax.set_xticks(range(len(riasec_academic)))
            ax.set_xticklabels(riasec_academic.index, fontsize=11, fontweight='bold')
            ax.set_ylabel("Nilai Akademik", fontsize=11, fontweight='bold')
            ax.set_xlabel("Tipe Kepribadian", fontsize=11, fontweight='bold')
            ax.set_ylim(0, 100)
            ax.grid(axis='y', alpha=0.3, linestyle='--')
            ax.set_axisbelow(True)
            ax.legend(fontsize=10)
            plt.tight_layout()
            st.pyplot(fig)
    
    with col2:
        st.markdown("####  Tabel Statistik")
        
        summary_stats = filtered_df.groupby('riasec_primary_type')['academic_overall'].agg([
            ('Jumlah', 'count'),
            ('Rata-rata', 'mean'),
            ('Median', 'median'),
            ('Std Dev', 'std'),
            ('Min', 'min'),
            ('Max', 'max')
        ]).round(2)
        
        # Reorder
        summary_stats = summary_stats.reindex([t for t in ['R', 'I', 'A', 'S', 'E', 'C'] 
                                              if t in summary_stats.index])
        
        st.dataframe(summary_stats, use_container_width=True)
    
    # Distribution per type
    st.markdown("---")
    st.markdown("###  Distribusi Nilai per Tipe Kepribadian")
    
    riasec_types_list = sorted(filtered_df['riasec_primary_type'].unique())
    
    if len(riasec_types_list) > 0:
        cols_per_row = 3
        n_rows = (len(riasec_types_list) + cols_per_row - 1) // cols_per_row
        
        colors_map = {'R': '#1f77b4', 'I': '#ff7f0e', 'A': '#2ca02c', 'S': '#d62728', 
                     'E': '#9467bd', 'C': '#8c564b'}
        
        for row_idx in range(n_rows):
            cols = st.columns(cols_per_row)
            
            for col_idx in range(cols_per_row):
                type_idx = row_idx * cols_per_row + col_idx
                
                if type_idx < len(riasec_types_list):
                    riasec_type = riasec_types_list[type_idx]
                    type_data = filtered_df[filtered_df['riasec_primary_type'] == riasec_type]
                    
                    with cols[col_idx]:
                        fig, ax = plt.subplots(figsize=(5, 4))
                        
                        academic_vals = type_data['academic_overall'].dropna()
                        if len(academic_vals) > 0:
                            n, bins, patches = ax.hist(academic_vals, bins=12, 
                                                       color=colors_map.get(riasec_type, '#667eea'),
                                                       edgecolor='black', alpha=0.7)
                            
                            mean_val = academic_vals.mean()
                            ax.axvline(mean_val, color='red', linestyle='--', linewidth=2,
                                     label=f'Mean: {mean_val:.1f}')
                            
                            ax.set_title(f"Tipe {riasec_type}\n({len(type_data)} siswa)", 
                                       fontweight='bold', fontsize=10)
                            ax.set_xlabel("Nilai", fontsize=9)
                            ax.set_ylabel("Frekuensi", fontsize=9)
                            ax.legend(fontsize=8)
                            ax.grid(axis='y', alpha=0.3, linestyle='--')
                            ax.set_axisbelow(True)
                        
                        plt.tight_layout()
                        st.pyplot(fig)

# ==================== PAGE: CAREER PATHWAYS ====================
elif page == " Distribusi Program Studi":
    # Header
    st.markdown("""
    <div class='header-title'>
        <h1> Distribusi Program Studi</h1>
    </div>
    """, unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    
    with col1:
        riasec_options = sorted(filtered_df['riasec_primary_type'].unique())

    
    program_riasec = filtered_df.groupby(['program_name', 'riasec_primary_type']).size().unstack(fill_value=0)
    
    if len(program_riasec) > 0:
        # Show top programs
        col1, col2 = st.columns([1, 1])
        
        with col1:
            top_programs_count = st.slider(
                "Berapa program yang ingin ditampilkan?", 
                3, min(20, len(program_riasec)), 8,
                help="Geser untuk mengubah jumlah program"
            )
        
        with col2:
            st.markdown(f"**Menampilkan: {top_programs_count} program teratas**")
        
        top_programs = program_riasec.sum(axis=1).nlargest(top_programs_count).index
        
        fig, ax = plt.subplots(figsize=(12, top_programs_count * 0.4 + 1))
        program_riasec.loc[top_programs].plot(
            kind='barh', stacked=True, ax=ax, 
            color=['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b'][:len(program_riasec.columns)]
        )
        
        ax.set_xlabel("Jumlah Siswa", fontsize=11, fontweight='bold')
        ax.set_title(f"Distribusi Tipe Kepribadian di {top_programs_count} Program Terpopuler", 
                    fontsize=12, fontweight='bold')
        ax.legend(title="Tipe RIASEC", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=9)
        ax.grid(axis='x', alpha=0.3, linestyle='--')
        ax.set_axisbelow(True)
        plt.tight_layout()
        st.pyplot(fig)

# ==================== PAGE: STUDENT PROFILES ====================
elif page == " Profil Siswa":
    # Header
    st.markdown("""
    <div class='header-title'>
        <h1> Profil & Pencarian Siswa</h1>
        <p>Temukan dan Analisis Data Siswa Secara Detail</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Search options
    st.markdown("###  Pilih Kriteria Pencarian")
    
    search_type = st.radio(
        "Cari Berdasarkan:",
        ["Tipe Kepribadian", "Program Studi", "Performa Akademik"],
        horizontal=True,
        label_visibility="collapsed"
    )
    
    if search_type == "Tipe Kepribadian":
        riasec_options = sorted(filtered_df['riasec_primary_type'].unique())
        riasec_names_short = {
            'R': ' Realistic', 'I': ' Investigative', 'A': ' Artistic',
            'S': ' Social', 'E': ' Enterprising', 'C': ' Conventional'
        }
        search_value = st.selectbox(
            "Pilih Tipe:",
            riasec_options,
            format_func=lambda x: riasec_names_short.get(x, x)
        )
        results = filtered_df[filtered_df['riasec_primary_type'] == search_value]
        search_label = f"Tipe Kepribadian: {riasec_names_short.get(search_value, search_value)}"
        types = results["riasec_primary_type"].unique().tolist()
        
        
    elif search_type == "Program Studi":
        programs = sorted(filtered_df['program_name'].unique())
        search_value = st.selectbox("Pilih Program:", programs)
        results = filtered_df[filtered_df['program_name'] == search_value]
        search_label = f"Program: {search_value}"
        types = results["riasec_primary_type"].unique().tolist()
        
    else:  # Academic Performance
        st.markdown("####  Rentang Nilai Akademik")
        col1, col2 = st.columns(2)
        
        with col1:
            min_score = st.number_input("Nilai Minimum:", 0, 100, 70, step=5)
        with col2:
            max_score = st.number_input("Nilai Maksimum:", 0, 100, 100, step=5)
        
        if min_score > max_score:
            st.error("❌ Nilai minimum tidak boleh lebih besar dari nilai maksimum!")
            results = pd.DataFrame()
        else:
            results = filtered_df[(filtered_df['academic_overall'] >= min_score) & 
                                 (filtered_df['academic_overall'] <= max_score)]
            search_label = f"Performa Akademik: {min_score} - {max_score}"
        types = results["riasec_primary_type"].unique().tolist()
            
    
    st.markdown("---")
    
    # Results header
    if len(results) > 0:
        st.markdown(f"""
        <div class='info-card'>
            <h3 style='margin-top: 0; color: #667eea;'> Hasil Pencarian</h3>
            <p style='margin: 0; font-size: 1.05em; color: white;'><strong>{search_label}</strong></p>
            <p style='margin: 0.5rem 0 0 0; color: white;'>Ditemukan <strong>{len(results):,}</strong> siswa</p>
        </div>
        """, unsafe_allow_html=True)
    
    if len(results) > 0:
        # Summary statistics
        st.markdown("###  Ringkasan Statistik")
        
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin-top: 0;'> Total Siswa</h3>
                <h2 style='margin: 0.5rem 0; color: white;'>{len(results):,}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            avg_score = results['academic_overall'].mean()
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin-top: 0;'> Nilai Rata-rata</h3>
                <h2 style='margin: 0.5rem 0; color: white;'>{avg_score:.1f}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin-top: 0;'> Tipe RIASEC</h3>
                <h2 style='margin: 0.5rem 0; color: white;'>{results['riasec_primary_type'].nunique() } ({", ".join(types)})</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col4:
            st.markdown(f"""
            <div class='metric-card'>
                <h3 style='color: #667eea; margin-top: 0;'> Program Studi</h3>
                <h2 style='margin: 0.5rem 0; color: white;'>{results['program_name'].nunique()}</h2>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Data table with pagination
        st.markdown("###  Data Siswa")
        
        display_cols = ['student_id', 'riasec_primary_type', 'riasec_primary_score', 
                       'program_name', 'academic_overall']
        available_cols = [col for col in display_cols if col in results.columns]
        
        # Pagination
        col1, col2, col3 = st.columns([1, 1, 1])
        
        with col1:
            page_size = st.selectbox("Berapa baris per halaman?", [5, 10, 15, 20, 50], index=1)
        
        total_pages = (len(results) + page_size - 1) // page_size
        
        with col2:
            current_page = st.number_input("Halaman:", 1, max(1, total_pages), 1)
        
        with col3:
            st.markdown(f"<p style='text-align: right; margin-top: 1.5rem;'><strong>{current_page} / {total_pages}</strong></p>", 
                       unsafe_allow_html=True)
        
        start_idx = (current_page - 1) * page_size
        end_idx = start_idx + page_size
        
        display_data = results[available_cols].iloc[start_idx:end_idx].reset_index(drop=True)
        
        # Format display data
        display_data_formatted = display_data.copy()
        display_data_formatted.columns = ['ID Siswa', 'Tipe RIASEC', 'Skor RIASEC', 'Program Studi', 'Nilai Akademik']
        
        st.dataframe(display_data_formatted, use_container_width=True, hide_index=True)
        
        st.markdown("---")
        
        # Statistics visualizations
        st.markdown("###  Visualisasi Detail")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("####  Distribusi Tipe Kepribadian")
            riasec_dist = results['riasec_primary_type'].value_counts().sort_index()
            
            if len(riasec_dist) > 0:
                fig, ax = plt.subplots(figsize=(9, 5))
                colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
                bars = ax.bar(riasec_dist.index, riasec_dist.values, 
                             color=colors[:len(riasec_dist)], alpha=0.8)
                
                # Add value labels
                for bar in bars:
                    height = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2., height,
                           f'{int(height)}',
                           ha='center', va='bottom', fontweight='bold', fontsize=10)
                
                ax.set_ylabel("Jumlah Siswa", fontsize=10, fontweight='bold')
                ax.set_xlabel("Tipe Kepribadian", fontsize=10, fontweight='bold')
                ax.grid(axis='y', alpha=0.3, linestyle='--')
                ax.set_axisbelow(True)
                plt.tight_layout()
                st.pyplot(fig)
        
        with col2:
            st.markdown("####  Distribusi Performa Akademik")
            academic_vals = results['academic_overall'].dropna()
            
            if len(academic_vals) > 0:
                fig, ax = plt.subplots(figsize=(9, 5))
                n, bins, patches = ax.hist(academic_vals, bins=15, color='#764ba2', 
                                          edgecolor='black', alpha=0.7)
                
                # Color gradient
                for i, patch in enumerate(patches):
                    patch.set_facecolor(plt.cm.viridis(i / len(patches)))
                
                mean_val = academic_vals.mean()
                ax.axvline(mean_val, color='red', linestyle='--', linewidth=2,
                          label=f'Mean: {mean_val:.1f}')
                
                ax.set_xlabel("Nilai Akademik", fontsize=10, fontweight='bold')
                ax.set_ylabel("Frekuensi", fontsize=10, fontweight='bold')
                ax.legend(fontsize=9)
                ax.grid(axis='y', alpha=0.3, linestyle='--')
                ax.set_axisbelow(True)
                plt.tight_layout()
                st.pyplot(fig)
    else:
        st.error(f"❌ Tidak ada siswa yang sesuai dengan kriteria pencarian Anda.\n\nCoba ubah filter atau kriteria pencarian.")

# ==================== FOOTER ====================
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem 1rem; background: linear-gradient(135deg, rgba(16, 163, 150, 0.1) 0%, rgba(13, 125, 116, 0.1) 100%); 
            border-radius: 10px; margin-top: 2rem; border: 1px solid rgba(16, 163, 150, 0.3);'>
    <h3 style='margin-top: 0; color: #10a396;'> Kompas Karir - RIASEC Career Guidance</h3>
    <p style='margin: 0.5rem 0; color: #b0b0b0;'><strong>Sistem:</strong> Dashboard Analisis Kepribadian & Rekomendasi Program Studi</p>
    <p style='margin: 0.5rem 0; color: #b0b0b0;'><strong>Tujuan:</strong> Memandu siswa menemukan jalur karir yang sesuai dengan potensi mereka</p>
    <p style='margin: 1rem 0 0 0; color: #808080; font-size: 0.85em;'>
        Menggunakan Framework RIASEC (Holland's Theory) untuk analisis kepribadian<br>
        Mengintegrasikan data akademik & preferensi karir untuk rekomendasi komprehensif<br>
        © 2024 - Universitas Indonesia | Kompas Karir
    </p>
</div>
""", unsafe_allow_html=True)
