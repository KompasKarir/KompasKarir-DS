# 🧭 Kompas Karir - RIASEC Career & Academic Performance Dashboard

**Sistem rekomendasi jurusan berbasis analisis kepribadian RIASEC dengan integrasi data akademik siswa SMA.**

Repositori ini berisi **Notebook untuk eksplorasi data**, **Dataset RIASEC yang telah diproses**, dan **Dashboard Interaktif** untuk visualisasi dan analisis hasil.

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
│   ├── Riasec_item.xlsx                            (Item RIASEC)
│   ├── program_studi_aggregated.csv                (Data 70 program studi)
│   └── data_prodi_ukt_universitas_indonesia.xlsx   (Data 22 kampus Indonesia)
│
├── 💻 dashboard.py                                 (Aplikasi Streamlit utama)
├── 📋 requirements.txt                             (Python dependencies)
├── 🎨 logo-kompas-karir.png                        (Logo branding)
└── 📖 README.md                                    (File ini)

```

---

## 📓 Notebook - Analisis Data

### File: `Notebook/riasec_analisis_data_preparation_for_ML.ipynb`

**Tujuan**: Eksplorasi data mendalam, pembersihan data (data wrangling), analisis statistik, dan persiapan data untuk machine learning.

### Isi Notebook:

#### **Bagian 1: Persiapan & Data Wrangling**
#### **Bagian 2: Analisis RIASEC**
#### **Bagian 3: Analisis Program Studi**
#### **Bagian 4: Analisis Kinerja Akademik**
#### **Bagian 5: Insights & Recommendations**

### Cara Menggunakan Notebook:
1. Buka di Jupyter Notebook atau Google Colab
2. Update path data (sesuaikan dengan lokasi file di sistem Anda)
3. Jalankan setiap cell secara berurutan
4. Lihat output untuk insights dan visualisasi

---

## 📊 Dataset - Data & Kegunaannya

---
> ⚠️ **DISCLAIMER**
>
> Data RIASEC pada repository ini merupakan data sintetis dan digunakan hanya untuk keperluan proyek kelompok dan demonstrasi. Hasil prediksi tidak boleh digunakan sebagai dasar pengambilan keputusan akademik atau profesional tanpa validasi lebih lanjut.

Dataset yang digunakan adalah data siswa SMA dengan informasi kepribadian RIASEC dan performa akademik mata pelajaran tertentu.

### File Dataset & Penjelasan:

#### **1. RIASEC Data**

| File | Deskripsi | Kegunaan |
|------|-----------|----------|
| `riasec_dataset_raw.csv` | Data mentah RIASEC dan nilai akademik | Input untuk notebook analisis |
| `riasec_dataset_processed.csv` | Data RIASEC yang sudah dibersihkan & diproses | Input utama untuk dashboard |
| `riasec_ml_ready.csv` | Data siap untuk machine learning | Input untuk modeling & predictive analytics |
| `Riasec_item.xlsx` | Item-item pertanyaan RIASEC  | Referensi pertanyaan (12 item per tipe × 6 = 72 items) |
| `riasec_data_dictionary.xlsx` | Kamus data (penjelasan kolom) | Memahami struktur data |

#### **2. Program Studi Data**

| File | Deskripsi | Kegunaan |
|------|-----------|----------|
| `program_studi_aggregated.csv` | Data program studi dalam bentuk agregat | Referensi program studi |
| `data_prodi_ukt_universitas_indonesia.xlsx` | Data program studi, lokasi, ukt 22 kampus di Indonesia | Rekomendasi perguruan tinggi berdasarkan rekomendasi Prodi |


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
### 5 Halaman Dashboard:

#### **1. 📊 Ringkasan (Overview)**
Halaman pertama yang menampilkan statistik keseluruhan:
- Total siswa terpilih
- Jumlah tipe RIASEC
- Jumlah program studi
- Rata-rata nilai akademik
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
- Distribusi nilai akademik
- Perbandingan performa antar tipe RIASEC

#### **4. 🏫 Distribusi Program Studi (Program Distribution)**
Pemetaan RIASEC dengan program studi:
- Top programs per tipe RIASEC
- Distribusi siswa per program
- Insights program mana yang paling populer

#### **5. 👥 Profil Siswa (Student Profiles)**
Pencarian dan filter siswa individual:
- Search by student ID
- Tampilkan detail siswa lengkap
- Tipe kepribadian & score
- Program studi
- Nilai akademik semua mata pelajaran
- Pagination untuk browsing data

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


## 🚀 Cara Menjalankan

### Menjalankan Dashboard:

```powershell
# Run dashboard
streamlit run dashboard.py
```

Dashboard akan:
- Compile & load data
- Open di browser default (http://localhost:8501)
- Display "Ringkasan" page sebagai default

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
