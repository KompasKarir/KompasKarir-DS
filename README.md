# 🧭 Kompas Karir - RIASEC Career & Academic Performance Dashboard

**Sistem rekomendasi jurusan berbasis analisis kepribadian RIASEC dengan integrasi data akademik siswa SMA.**

Repositori ini berisi **Notebook untuk eksplorasi data**, **Dataset RIASEC yang telah diproses**, dan **Dashboard Interaktif** untuk visualisasi dan analisis hasil.

---
> ⚠️ **DISCLAIMER**
>
> Dataset dan hasil analisis pada repository ini merupakan data sintetis dan digunakan hanya untuk tujuan edukasi dan demonstrasi. Hasil prediksi tidak boleh digunakan sebagai dasar pengambilan keputusan akademik atau profesional tanpa validasi lebih lanjut.

## 🎯 Tentang Proyek

**Kompas Karir** adalah sistem rekomendasi karir yang menganalisis kepribadian siswa menggunakan **model RIASEC (Realistic, Investigative, Artistic, Social, Enterprising, Conventional)** yang dikombinasikan dengan **data hasil akademik**.

### Tujuan Proyek:
- 📊 **Analisis Kepribadian**: Memetakan distribusi siswa ke dalam 6 tipe kepribadian RIASEC
- 🎓 **Rekomendasi Program Studi**: Menghubungkan tipe kepribadian dengan program studi yang sesuai
- 📈 **Korelasi Akademik**: Menentukan hubungan antara tipe kepribadian, pilihan program, dan performa akademik
- 💡 **Insights Karir**: Memberikan panduan karir berdasarkan data dan analisis statistik

### Pertanyaan Bisnis:
1. **Bagaimana distribusi siswa pada setiap tipe kepribadian RIASEC?** Program studi mana yang paling sesuai dengan setiap tipe?
2. **Apakah ada korelasi signifikan antara tipe kepribadian dan kinerja akademik?** Apakah siswa dengan keselarasan personality-program memiliki performa yang lebih baik?

---

## 📁 Struktur Repository

```
KompasKarir_DS/
│
├── 📓 Notebook/
│   └── riasec_analisis_data_preparation_for_ML.ipynb
│       └─ Notebook Jupyter untuk eksplorasi, analisis, dan persiapan data
│
├── 📊 Dataset/
│   ├── riasec_dataset_raw.csv                      (Data mentah RIASEC)
│   ├── riasec_dataset_processed.csv                (Data terproses untuk dashboard)
│   ├── riasec_ml_ready.csv                         (Data siap ML)
│   ├── riasec_data_dictionary.xlsx                 (Kamus data)
│   ├── Riasec_item.xlsx                            (Item RIASEC questionnaire)
│   ├── program_studi_aggregated.csv                (Data program studi agregat)
│   ├── data_prodi_ukt_universitas_indonesia.xlsx   (Data program UI)
│   ├── data_prodi_ukt_universitas_indonesia 1.xlsx (Data program UI - Part 1)
│   └── data_prodi_ukt_universitas_indonesia 2.xlsx (Data program UI - Part 2)
│
├── 💻 dashboard.py                                 (Aplikasi Streamlit utama)
├── 📋 requirements.txt                             (Python dependencies)
├── 🎨 logo-kompas-karir.png                        (Logo branding)
├── 📖 README.md                                    (File ini)
├── 🚀 GETTING_STARTED.md                           (Quick start guide)
└── 📚 REPOSITORY_STRUCTURE.md                      (Penjelasan struktur repository)
```

---

## 📓 Notebook - Analisis Data

### File: `Notebook/riasec_analisis_data_preparation_for_ML.ipynb`

**Tujuan**: Eksplorasi data mendalam, pembersihan data (data wrangling), analisis statistik, dan persiapan data untuk machine learning.

### Isi Notebook:

#### **Bagian 1: Persiapan & Data Wrangling**
- 📥 **Gathering Data**: Memuat dataset RIASEC dari Google Drive
- 🔍 **Data Exploration**: Melihat struktur data, tipe kolom, missing values
- 🧹 **Data Cleaning**: Menangani duplikat, nilai hilang, dan outliers
- 📊 **Data Overview**: Statistik deskriptif, distribusi data

#### **Bagian 2: Analisis RIASEC**
- 🧭 **RIASEC Scoring**: Menghitung skor untuk masing-masing 6 tipe kepribadian
- 🔝 **Primary Type Determination**: Menentukan tipe kepribadian utama setiap siswa
- 📈 **Distribution Analysis**: Melihat persentase distribusi siswa per tipe
- 🎯 **Type Characteristics**: Analisis karakteristik unik setiap tipe

#### **Bagian 3: Analisis Program Studi**
- 🏫 **Program Distribution**: Distribusi siswa per program studi
- 🔗 **RIASEC-Program Mapping**: Hubungan antara tipe kepribadian dan pilihan program
- 📊 **Cross-tabulation Analysis**: Tabel silang untuk melihat pola

#### **Bagian 4: Analisis Kinerja Akademik**
- 🎓 **Academic Subjects**: Analisis nilai per mata pelajaran (Math, Bahasa, IPA, IPS, Informatika, Praktik)
- 📉 **Performance Metrics**: Rata-rata, median, std dev per tipe kepribadian
- 🔗 **Correlation Analysis**: Korelasi Pearson & Spearman antara RIASEC score dan nilai akademik
- 📊 **Heatmap Visualization**: Visualisasi korelasi dalam bentuk heatmap

#### **Bagian 5: Insights & Recommendations**
- 💡 **Key Findings**: Temuan penting dari analisis
- ✅ **Recommendations**: Rekomendasi untuk sistem karir
- 🎯 **Data Preparation for ML**: Persiapan data untuk modeling

### Cara Menggunakan Notebook:
1. Buka di Jupyter Notebook atau Google Colab
2. Update path data (sesuaikan dengan lokasi file di sistem Anda)
3. Jalankan setiap cell secara berurutan
4. Lihat output untuk insights dan visualisasi

---

## 📊 Dataset - Data & Kegunaannya

### Sumber Data: Universitas Indonesia

Dataset yang digunakan adalah data siswa Universitas Indonesia dengan informasi kepribadian RIASEC dan performa akademik.

### File Dataset & Penjelasan:

#### **1. RIASEC Data**

| File | Deskripsi | Kegunaan |
|------|-----------|----------|
| `riasec_dataset_raw.csv` | Data mentah RIASEC dari questionnaire | Input untuk notebook analisis |
| `riasec_dataset_processed.csv` | Data RIASEC yang sudah dibersihkan & diproses | Input utama untuk dashboard |
| `riasec_ml_ready.csv` | Data siap untuk machine learning | Input untuk modeling & predictive analytics |
| `Riasec_item.xlsx` | Item-item pertanyaan RIASEC questionnaire | Referensi pertanyaan (12 item per tipe × 6 = 72 items) |
| `riasec_data_dictionary.xlsx` | Kamus data (penjelasan kolom) | Memahami struktur data |

#### **2. Program Studi Data**

| File | Deskripsi | Kegunaan |
|------|-----------|----------|
| `program_studi_aggregated.csv` | Data program studi dalam bentuk agregat | Referensi program studi |
| `data_prodi_ukt_universitas_indonesia.xlsx` | Data lengkap program UI | Mapping program dengan RIASEC |
| `data_prodi_ukt_universitas_indonesia 1.xlsx` | Data program UI (part 1) | Backup & detail tambahan |
| `data_prodi_ukt_universitas_indonesia 2.xlsx` | Data program UI (part 2) | Backup & detail tambahan |

### Struktur Data RIASEC:

```
Kolom Utama:
├── student_id              (ID unik siswa)
├── program_name            (Nama program studi)
├── riasec_r_item_1...12    (12 item untuk tipe Realistic)
├── riasec_i_item_1...12    (12 item untuk tipe Investigative)
├── riasec_a_item_1...12    (12 item untuk tipe Artistic)
├── riasec_s_item_1...12    (12 item untuk tipe Social)
├── riasec_e_item_1...12    (12 item untuk tipe Enterprising)
├── riasec_c_item_1...12    (12 item untuk tipe Conventional)
├── academic_math           (Nilai Matematika)
├── academic_language       (Nilai Bahasa)
├── academic_ipa            (Nilai IPA/Science)
├── academic_ips            (Nilai IPS/Social)
├── academic_informatika    (Nilai Informatika)
├── academic_praktik        (Nilai Praktik)
└── [Kolom lain]            (Demografi, dll)
```

### 6 Tipe Kepribadian RIASEC:

| Tipe | Deskripsi | Ciri-Ciri | Program yang Cocok |
|------|-----------|----------|-------------------|
| **R** - Realistic | Praktis & Konkret | Suka kerja manual, problem-solving praktis, teknis | Teknik, Pertanian, Kelautan |
| **I** - Investigative | Analitis & Peneliti | Suka riset, data, logika, thinking & analyzing | Sains, Teknologi, Riset |
| **A** - Artistic | Kreatif & Imajinatif | Suka seni, design, ekspresi, unstructured | Seni, Design, Komunikasi |
| **S** - Social | Sosial & Membantu | Suka interaksi, mentoring, helping people | Pendidikan, Psikologi, Sosial |
| **E** - Enterprising | Bisnis & Kepemimpinan | Suka leadership, persuasi, bisnis, risk-taking | Bisnis, Manajemen, Ekonomi |
| **C** - Conventional | Teratur & Sistematis | Suka organisasi, detail, rules, data processing | Akuntansi, Administrasi |

### Kegunaan Data dalam Proyek:

1. **Dashboard Visualisasi**: Data digunakan untuk membuat visualisasi interaktif
2. **Filtering & Segmentation**: Memfilter data berdasarkan tipe kepribadian
3. **Correlation Analysis**: Menganalisis hubungan RIASEC dengan performa akademik
4. **Recommendation Engine**: Basis untuk merekomendasikan program studi
5. **Predictive Modeling**: Persiapan untuk machine learning model

---

## 💻 Dashboard - Visualisasi Interaktif

### File: `dashboard.py`

**Framework**: Streamlit v1.28.1  
**Theme**: Dark mode dengan aksen teal (#10a396) - warna Kompas Karir  
**Accessibility**: WCAG AAA compliant

### Arsitektur Dashboard:

```
┌─────────────────────────────────────────────────┐
│  🧭 Kompas Karir - Dashboard                    │
│  Dark Mode with Strategic Teal Accents          │
└─────────────────────────────────────────────────┘
│                                                 │
│ SIDEBAR                    │  MAIN CONTENT      │
│ ─────────────────          │  ──────────────    │
│ 🧭 Logo & Branding         │  5 Pages:          │
│ 📍 Navigation Pages        │  ✓ Ringkasan       │
│ 🔍 Filter RIASEC Types     │  ✓ Tipe Kepribadian│
│ 📊 Filter Statistics       │  ✓ Performa        │
│ 🔄 Reset Filters           │  ✓ Program Studi   │
│                            │  ✓ Profil Siswa    │
└────────────────────────────────────────────────┘
```

### 5 Halaman Dashboard:

#### **1. 📊 Ringkasan (Overview)**
Halaman pertama yang menampilkan statistik keseluruhan:
- Total siswa terpilih
- Jumlah tipe RIASEC
- Jumlah program studi
- Rata-rata nilai akademik
- Visualisasi distribusi RIASEC dengan pie chart
- Grafik performa akademik per tipe kepribadian

#### **2. 🧭 Tipe Kepribadian (RIASEC Analysis)**
Analisis mendalam untuk setiap tipe kepribadian:
- Tab untuk setiap tipe (R, I, A, S, E, C)
- Deskripsi karakteristik tipe
- Jumlah & persentase siswa per tipe
- Distribusi program studi per tipe
- Performa akademik per tipe
- Visualisasi grafik yang detail

#### **3. 📈 Performa Akademik (Academic Performance)**
Analisis kinerja siswa berdasarkan mata pelajaran:
- Statistik per mata pelajaran (Mean, Min, Max, Std Dev)
- Box plot untuk setiap mata pelajaran
- Distribusi nilai akademik
- Perbandingan performa antar tipe RIASEC
- Heatmap korelasi RIASEC score vs nilai akademik

#### **4. 🏫 Distribusi Program Studi (Program Distribution)**
Pemetaan RIASEC dengan program studi:
- Top programs per tipe RIASEC
- Distribusi siswa per program
- Cross-tabulation RIASEC vs Program
- Visualisasi hubungan dalam bentuk sunburst chart
- Insights program mana yang paling populer

#### **5. 👥 Profil Siswa (Student Profiles)**
Pencarian dan filter siswa individual:
- Search by student ID
- Tampilkan detail siswa lengkap
- Tipe kepribadian & score
- Program studi
- Nilai akademik semua mata pelajaran
- Pagination untuk browsing data

### Fitur Interaktif:

✨ **Sidebar Filter**:
- Filter berdasarkan tipe kepribadian RIASEC
- Real-time filtering
- Statistics tentang data terpilih
- Reset filter button

🎨 **Modern Design**:
- Dark mode (#0a0f0d) untuk kenyamanan mata
- Teal accent (#10a396) untuk brand consistency
- High contrast text (#d8d8d8, #ffffff) untuk readability
- Responsive layout untuk berbagai ukuran layar

📊 **Interactive Visualizations**:
- Pie charts untuk distribusi
- Bar charts untuk komparasi
- Line charts untuk trends
- Heatmaps untuk korelasi
- Hover tooltips untuk detail

🚀 **Performance Optimized**:
- @st.cache_data untuk mempercepat loading
- Lazy loading untuk visualisasi besar
- Efficient data filtering

---

## 🔄 Langkah-langkah Replikasi

### Persiapan Awal:

#### **Langkah 1: Clone Repository**
```bash
git clone https://github.com/KompasKarir/KompasKarir_DS.git
cd KompasKarir_DS
```

#### **Langkah 2: Setup Python Environment**
```bash
# Windows PowerShell
python -m venv venv
venv\Scripts\Activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

#### **Langkah 3: Install Dependencies**
```bash
pip install -r requirements.txt
```

### Workflow Lengkap:

#### **Phase 1: Data Preparation**
1. **Pastikan Dataset Ada**
   ```
   Dataset/
   ├── riasec_dataset_raw.csv
   ├── riasec_dataset_processed.csv
   └── [file lainnya]
   ```
   
2. **Buka Notebook** (Opsional - untuk analisis mendalam)
   - Buka: `Notebook/riasec_analisis_data_preparation_for_ML.ipynb`
   - Jalankan cells untuk eksplorasi data
   - Generate visualisasi dan insights

3. **Validate Data**
   ```python
   import pandas as pd
   df = pd.read_csv('Dataset/riasec_dataset_processed.csv')
   print(df.head())
   print(df.info())
   print(df.describe())
   ```

#### **Phase 2: Run Dashboard**
```bash
streamlit run dashboard.py
```
Dashboard akan buka di `http://localhost:8501`

#### **Phase 3: Explore & Analyze**
- Gunakan sidebar filter untuk eksplorasi data
- Klik tab berbeda untuk lihat berbagai perspektif
- Interact dengan chart untuk detail lebih

#### **Phase 4: Customize (Opsional)**
- Edit `dashboard.py` untuk custom styling
- Add kolom baru ke dataset
- Tambah halaman baru dengan analisis khusus

---

## 📋 Persyaratan & Instalasi

### Sistem Requirement:

- **Operating System**: Windows, macOS, atau Linux
- **Python**: 3.8 atau lebih tinggi
- **RAM**: Minimal 4GB (recommended 8GB)
- **Storage**: Minimal 500MB

### Step-by-Step Installation:

#### **1. Install Python** (jika belum)
Download dari: https://www.python.org/downloads/

Pastikan centang "Add Python to PATH" saat install.

#### **2. Navigate ke Project Directory**
```powershell
cd "path\to\KompasKarir_DS"
```

#### **3. Create Virtual Environment**
```powershell
# Windows
python -m venv venv
venv\Scripts\Activate

# atau jika Python 3 command
python3 -m venv venv
venv\Scripts\Activate
```

Atau gunakan Anaconda:
```bash
conda create -n kompas-karir python=3.9
conda activate kompas-karir
```

#### **4. Install Dependencies**
```powershell
pip install --upgrade pip
pip install -r requirements.txt
```

Atau install manual:
```powershell
pip install streamlit==1.28.1 pandas==2.0.3 numpy==1.24.3 matplotlib==3.7.2 seaborn==0.12.2 scipy==1.11.2 scikit-learn==1.3.0 openpyxl==3.1.2 Pillow==10.0.0
```

#### **5. Verify Installation**
```powershell
python -c "import streamlit; print(streamlit.__version__)"
```

---

## 🚀 Cara Menjalankan

### Menjalankan Dashboard:

```powershell
# Navigate ke project directory
cd "c:\Users\carli\Documents\Kuliah\Coding Camp DBS\Capstone\Data Scientist"

# Activate virtual environment
venv\Scripts\Activate

# Run dashboard
streamlit run dashboard.py
```

Dashboard akan:
- Compile & load data
- Open di browser default (http://localhost:8501)
- Display "Ringkasan" page sebagai default

### Command Line Options:

```powershell
# Run dengan custom config
streamlit run dashboard.py -- --logger.level=warning

# Run dengan custom port
streamlit run --server.port 8502 dashboard.py

# Run dari terminal lain untuk debugging
streamlit run dashboard.py --logger.level=debug
```

### Troubleshooting:

❌ **"streamlit: command not found"**
```powershell
# Pastikan virtual environment aktif
venv\Scripts\Activate

# Atau install streamlit
pip install streamlit
```

❌ **"ModuleNotFoundError: No module named 'pandas'"**
```powershell
pip install -r requirements.txt
```

❌ **"riasec_dataset_processed.csv not found"**
- Pastikan file ada di folder `Dataset/`
- Check path di dashboard.py line 400-410

---

## ✨ Fitur Dashboard

### Design & UX:
- ✅ **Dark Mode**: Background #0a0f0d untuk kenyamanan mata
- ✅ **Brand Colors**: Teal #10a396 sesuai logo Kompas Karir
- ✅ **High Contrast**: Font colors #d8d8d8 & #ffffff untuk readability
- ✅ **Responsive**: Adapts ke berbagai ukuran layar
- ✅ **WCAG AAA**: Accessible untuk semua pengguna
- ✅ **Logo Integration**: Logo Kompas Karir di sidebar

### Interactivity:
- ✅ **RIASEC Filter**: Multi-select untuk tipe kepribadian
- ✅ **Real-time Updates**: Data update saat filter berubah
- ✅ **Student Search**: Cari siswa by ID
- ✅ **Interactive Charts**: Hover untuk tooltips
- ✅ **Pagination**: Browsing data dengan pagination

### Data Visualization:
- ✅ **Pie Charts**: Distribusi RIASEC types
- ✅ **Bar Charts**: Komparasi akademik
- ✅ **Box Plots**: Distribution analysis
- ✅ **Heatmaps**: Correlation matrix
- ✅ **Line Charts**: Trends analysis

### Performance:
- ✅ **Data Caching**: @st.cache_data untuk fast loading
- ✅ **Lazy Loading**: Efficient rendering
- ✅ **Optimized**: Smooth performance dengan 5000+ records
- ✅ **Responsive**: No lag pada filtering

---

## 🛠 Teknologi & Library

### Backend & Frontend:

| Library | Versi | Fungsi |
|---------|-------|--------|
| **Streamlit** | 1.28.1 | Web framework untuk interactive dashboard |
| **Pandas** | 2.0.3 | Data manipulation & analysis |
| **NumPy** | 1.24.3 | Numerical computations |
| **Matplotlib** | 3.7.2 | Static data visualization |
| **Seaborn** | 0.12.2 | Statistical data visualization |
| **SciPy** | 1.11.2 | Scientific computing & statistics |
| **scikit-learn** | 1.3.0 | Machine learning algorithms |
| **openpyxl** | 3.1.2 | Excel file handling |
| **Pillow** | 10.0.0 | Image processing (logo display) |

### Tools & Environment:

- **Version Control**: Git & GitHub
- **IDE**: VS Code, PyCharm, atau Jupyter Notebook
- **Package Manager**: pip
- **Virtual Environment**: venv (built-in Python)
- **Data Format**: CSV, XLSX, JSON (supported)

---

## 📧 Support & Contact

- 📝 **Issues**: Report bugs via GitHub Issues
- 💬 **Discussions**: Join GitHub Discussions untuk Q&A
- 🔗 **GitHub**: [KompasKarir/KompasKarir_DS](https://github.com/KompasKarir/KompasKarir_DS)

---

## 📄 Lisensi

Proyek ini adalah bagian dari **Capstone Project** di **DBS Coding Camp** dan merupakan **research project** untuk **Universitas Indonesia**.

---

## 🎓 Tim Pengembang

**Data Scientist**: [Nama Anda]  
**Institusi**: DBS Coding Camp x Universitas Indonesia  
**Tahun**: 2024-2025

---

## 📚 Dokumentasi Tambahan

- 🚀 **GETTING_STARTED.md**: Quick start guide
- 📖 **INSTALLATION_GUIDE.md**: Panduan instalasi detail
- 🏗️ **REPOSITORY_STRUCTURE.md**: Penjelasan struktur folder
- 🎨 **VISUAL_SUMMARY.md**: Visual reference untuk design system
- 📊 **COLOR_PALETTE_REFERENCE.md**: Color system documentation
- ✅ **FINAL_VERIFICATION_CHECKLIST.md**: Checklist verifikasi
- 📈 **UPDATE_ENHANCED_DARK_MODE.md**: Dark mode documentation

---

**Last Updated**: Juni 2025  
**Dashboard Version**: 3.2 (Enhanced Dark Mode)  
**Status**: ✅ Production Ready  

🧭 **Kompas Karir Dashboard - Siap Digunakan!**
streamlit run dashboard.py
```

Dashboard akan otomatis membuka di browser pada `http://localhost:8501` ✨

Dashboard akan membuka otomatis di browser (biasanya http://localhost:8501)

### Alternatif:

```powershell
python -m streamlit run dashboard.py
```

## 📁 Struktur Folder

```
Capstone/Data Scientist/
├── dashboard.py                              # Main dashboard file
├── requirements.txt                          # Python dependencies
├── README.md                                 # Dokumentasi ini
├── Dataset/
│   ├── riasec_dataset_raw.csv               # Raw dataset
│   ├── riasec_dataset_processed.csv         # Processed dataset
│   ├── riasec_ml_ready.csv                  # ML-ready dataset
│   ├── program_studi_aggregated.csv
│   ├── data_prodi_ukt_universitas_indonesia.xlsx
│   └── ... (file dataset lainnya)
├── Notebook/
│   └── riasec_analisis_data_preparation_for_ML.ipynb
```

## 🎯 Fitur Dashboard (5 Halaman Interaktif)

### 1. 📊 Ringkasan (Overview)

- **Statistik Utama:** Total siswa, tipe RIASEC, program studi, nilai rata-rata
- **Visualisasi:** Distribusi tipe kepribadian & nilai akademik
- **Insights:** Tipe terbanyak, program terpilih, siswa berprestasi

### 2. 🧭 Tipe Kepribadian (RIASEC Analysis)

- **6 Tabs** untuk analisis mendalam setiap tipe (R, I, A, S, E, C)
- **Per Tipe:** Deskripsi lengkap, statistik, program favorit
- **Visualisasi:** Horizontal bar charts dengan value labels
- **Interaktif:** Hover effects dan color-coding

### 3. 📈 Performa Akademik (Academic Performance)

- **Chart:** Performa akademik per tipe RIASEC dengan error bars
- **Tabel:** Statistik lengkap (mean, median, std dev, min, max)
- **Histograms:** Distribusi nilai untuk setiap tipe (grid 3x2)
- **Analisis:** Mean & median lines, grid styling

### 4. 🎓 Rekomendasi Karir (Career Pathways)

- **Pilih Tipe:** Selectbox dengan format intuitif
- **Rekomendasi:** 6 karir suggestions dalam grid layout
- **Mapping:** Distribusi RIASEC dalam program studi (stacked bar)
- **Slider:** Customizable number of programs to display

### 5. 👥 Profil Siswa (Student Profiles)

- **Search:** Berdasarkan tipe kepribadian, program, atau performa akademik
- **Results:** Statistics cards dengan summary data
- **Table:** Pagination dengan customizable page size
- **Visualisasi:** Distribution charts untuk hasil pencarian

### 4. 🎓 Career Pathways

- Rekomendasi karir berdasarkan tipe RIASEC
- Mapping program studi ke tipe kepribadian
- Visualisasi distribusi RIASEC dalam program

## 🎨 UI/UX Design Improvements ✨

Dashboard telah diperbarui dengan design yang **lebih intuitif, modern, dan profesional**:

### 🎯 Design Highlights

- ✅ **Header Gradient** - Modern purple gradient (#667eea → #764ba2)
- ✅ **Metric Cards** - Custom styled dengan hover effects
- ✅ **Color Coding** - RIASEC types punya warna unik & konsisten
- ✅ **Bahasa Indonesia** - Semua konten dalam Bahasa Indonesia
- ✅ **Value Labels** - Semua chart menampilkan nilai (no guessing)
- ✅ **Icons & Emojis** - Visual cues untuk setiap fitur
- ✅ **Responsive Layout** - Fleksibel di berbagai ukuran layar
- ✅ **Professional Typography** - Bold headers, clear hierarchy

### 🔍 Sidebar Improvements

- **Logo/Branding** - Header dengan gradient background
- **Clear Navigation** - 5 halaman dengan deskripsi
- **Better Filters** - Format display untuk RIASEC types
- **Filter Stats** - Menampilkan data yang terfilter
- **Reset Button** - Tombol untuk reset filter

### 📊 Chart Enhancements

- Value labels pada semua bar & histogram
- Color gradient untuk better aesthetics
- Grid lines untuk readability
- Error bars untuk uncertainty visualization
- Legend positioning yang optimal

## 🔧 Sidebar Filters

- **Tipe Kepribadian RIASEC**: Pilih satu atau lebih tipe untuk dianalisis
- **Program Studi**: Pilih program yang ingin ditampilkan
- **Filter Statistics**: Melihat data yang terfilter secara real-time
- **Reset Filter Button**: Kembalikan ke default settings

## 📊 Dataset Support

Dashboard mendukung file dataset berikut (dalam urutan preferensi):

1. `riasec_ml_ready.csv` - Dataset siap untuk machine learning
2. `riasec_dataset_processed.csv` - Dataset yang sudah diproses
3. `riasec_dataset_raw.csv` - Raw dataset (akan diproses otomatis)

**Kolom yang diperlukan dalam dataset:**

- `student_id` - ID siswa
- `program_name` - Nama program studi
- `riasec_primary_type` - Tipe kepribadian utama (R, I, A, S, E, C)
- `riasec_primary_score` - Skor kepribadian utama
- `academic_overall` - Skor akademik keseluruhan

## 🎨 Color Scheme

Dashboard menggunakan palette yang konsisten & profesional:

- **Primary:** #667eea (Blue-Purple)
- **Secondary:** #764ba2 (Purple)
- **RIASEC Types:**
  - R: #1f77b4 (Blue)
  - I: #ff7f0e (Orange)
  - A: #2ca02c (Green)
  - S: #d62728 (Red)
  - E: #9467bd (Purple)
  - C: #8c564b (Brown)

## 📱 Responsive Design

- Flexible column-based layouts
- Adaptive figure sizes
- Dynamic grid arrangements
- Mobile-friendly responsive design

## ⚙️ Troubleshooting

### Streamlit tidak terdeteksi

```powershell
# Install ulang streamlit
pip install --upgrade streamlit
```

### Data tidak ditemukan

- Pastikan folder `Dataset` ada di lokasi yang sama dengan `dashboard.py`
- Pastikan minimal satu file dataset ada (lihat section Dataset Support)

### Port sudah digunakan

```powershell
streamlit run dashboard.py --server.port 8502
```

### Virtual Environment issue

```powershell
# Buat virtual environment baru
python -m venv venv_new
venv_new\Scripts\Activate
pip install -r requirements.txt
```

## 📚 Dataset Information

**RIASEC Model:**

- **R**ealistic (Realistis) - Praktis, hands-on, teknis
- **I**nvestigative (Investigatif) - Analitis, saintifik, pemecahan masalah
- **A**rtistic (Artistik) - Kreatif, ekspresif, inovatif
- **S**ocial (Sosial) - Berorientasi orang, komunikasi, teamwork
- **E**nterprising (Enterprising) - Kepemimpinan, ambisius, persuasif
- **C**onventional (Konvensional) - Terorganisir, detail-oriented, administratif

## 📖 Dokumentasi Lengkap

Lihat file dokumentasi lainnya untuk informasi lebih detail:

- `FITUR_DASHBOARD.md` - Panduan lengkap fitur & UI
- `UI_UX_IMPROVEMENTS.md` - Detail perubahan UI/UX
- `START_HERE.md` - Quick start guide
- `QUICK_START.md` - Quick reference
- `DATA_STRUCTURE_GUIDE.md` - Data format specification

## 🔗 Resources

- [Streamlit Documentation](https://docs.streamlit.io)
- [RIASEC Model](https://en.wikipedia.org/wiki/Strong_Interest_Inventory)
- [Pandas Documentation](https://pandas.pydata.org)
- [Matplotlib Documentation](https://matplotlib.org)

## 📝 Catatan

- Dashboard menggunakan caching untuk performa optimal
- Data difilter secara real-time berdasarkan sidebar selections
- Semua grafik dihasilkan menggunakan Matplotlib dan Seaborn
- Kompatibel dengan Windows, macOS, dan Linux
- **BARU:** Semua konten dalam Bahasa Indonesia untuk accessibility

## 🤝 Support

Untuk masalah atau pertanyaan, silakan:

1. Periksa bagian Troubleshooting di atas
2. Verifikasi struktur folder dan file dataset
3. Pastikan semua dependensi terinstall dengan benar

---

**Happy Analyzing! 🎉**
