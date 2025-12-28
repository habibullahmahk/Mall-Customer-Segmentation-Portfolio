# Import Library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans

# Load Data
# Pastikan nama file CSV sesuai dengan yang ada di folder VS Code Anda
df = pd.read_csv('Shopping Mall Customer Segmentation Data.csv')

# Cek 5 baris teratas
print("Data Awal:")
print(df.head()) 

# --- MASUK TAHAP 2: CLEANING & SELECTION (PERBAIKAN) ---
print("\n--- MASUK TAHAP 2: CLEANING & SELECTION ---")

# 1. Cek nama kolom asli (Untuk memastikan)
print("Nama Kolom Asli:", df.columns)

# 2. Ganti nama kolom
# Kita sesuaikan dengan output terminal: 'Annual Income' dan 'Spending Score'
df = df.rename(columns={
    'Annual Income': 'Annual_Income',
    'Spending Score': 'Spending_Score'
})

# 3. Cek apakah penggantian nama berhasil
print("\nNama Kolom Baru:", df.columns)

# 4. Memilih Fitur untuk Clustering
X = df[['Annual_Income', 'Spending_Score']]

print("\nData Siap untuk Clustering (X):")
print(X.head())

# --- BATAS TAHAP 2 (Kode sebelumnya di atas sini) ---

print("\n--- MASUK TAHAP 3: ELBOW METHOD ---")
print("Sedang menghitung inersia untuk 1-10 klaster...")

wcss = [] # List untuk menyimpan nilai error

# Looping mencoba klaster 1 sampai 10
for i in range(1, 11):
    # init='k-means++' adalah trik supaya algoritma lebih cepat menemukan pola
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

print("Selesai menghitung. Menampilkan Grafik...")

# Plotting Grafik Elbow
plt.figure(figsize=(10,5))
plt.plot(range(1, 11), wcss, marker='o', linestyle='--')
plt.title('Metode Elbow (Siku)')
plt.xlabel('Jumlah Klaster')
plt.ylabel('WCSS (Inersia/Error)')
plt.grid(True) # Menambah garis grid supaya mudah dibaca
plt.show() # <--- INI AKAN MEMBUKA JENDELA POP-UP

# --- BATAS TAHAP 3 (Kode sebelumnya di atas sini) ---

print("\n--- MASUK TAHAP 4: CLUSTERING & LABELING ---")

# 1. Melakukan K-Means dengan 5 Klaster (Keputusan Analyst)
kmeans = KMeans(n_clusters=5, init='k-means++', random_state=42)
y_kmeans = kmeans.fit_predict(X)

# 2. Masukkan hasil klaster ke dataframe
df['Cluster_Code'] = y_kmeans

# 3. Cek karakteristik tiap klaster untuk menentukan Label (PENTING!)
# Kita hitung rata-rata Income dan Spending untuk tiap kode (0-4)
summary = df.groupby('Cluster_Code')[['Annual_Income', 'Spending_Score']].mean()
print("\nKarakteristik Tiap Klaster:")
print(summary)

# --- BAGIAN MAPPING OTOMATIS BERDASARKAN LOGIKA ---
# Kode di bawah ini akan otomatis mendeteksi siapa yang "VIP", "Hemat", dll
# berdasarkan nilai rata-rata yang baru saja dihitung.

def get_cluster_name(row):
    # Logika sederhana membandingkan Income dan Spending
    income = row['Annual_Income']
    spending = row['Spending_Score']
    
    # Ambil nilai rata-rata income dan spending score dari seluruh populasi sebagai patokan
    avg_income_population = df['Annual_Income'].mean()
    avg_spending_population = df['Spending_Score'].mean()

    # Logika Penamaan (Rule Based)
    if income > avg_income_population and spending > avg_spending_population:
        return 'VIP (Target)'
    elif income > avg_income_population and spending < avg_spending_population:
        return 'Miser (Berduit tapi Hemat)'
    elif income < avg_income_population and spending > avg_spending_population:
        return 'Careless (Boros)'
    elif income < avg_income_population and spending < avg_spending_population:
        return 'Sensible (Hemat)'
    else:
        return 'Standard (Menengah)'

# Terapkan fungsi penamaan ke setiap baris data
# (Kita pakai apply ke data asli untuk akurasi per individu)
df['Cluster_Name'] = df.apply(get_cluster_name, axis=1)

print("\nContoh Hasil Akhir (Data + Label):")
print(df[['Annual_Income', 'Spending_Score', 'Cluster_Name']].head(10))

# 4. EXPORT DATA (Tahap Terakhir Python)
df.to_csv('Mall_Customers_Segmentation_Final.csv', index=False)
print("\nSUKSES! File 'Mall_Customers_Segmentation_Final.csv' berhasil disimpan.")