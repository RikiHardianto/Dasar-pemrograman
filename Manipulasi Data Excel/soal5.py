import pandas as pd
data = pd.read_excel('data_penjualan.xlsx')
data['Total Harga'] = data['Jumlah'] * data['Harga Satuan']
data_sorted = data.sort_values(by='Total Harga', ascending=False)
data_sorted.to_excel('penjualan_terurut.xlsx',index=False)