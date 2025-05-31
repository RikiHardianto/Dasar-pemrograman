import pandas as pd

# Baca file Excel
data = pd.read_excel('data_penjualan.xlsx')

# Hitung kolom Total Harga
data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']

# Rekap total pendapatan per kategori
rekap = data.groupby('Kategori')['Total Harga'].sum().reset_index()
rekap.columns = ['Kategori', 'Total Pendapatan']

# Simpan ke file Excel baru
rekap.to_excel('rekap_penjualan_per_kategori.xlsx', index=False)