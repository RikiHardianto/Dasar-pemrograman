import pandas as pd 
import matplotlib.pyplot as plt

file_path = "Data_Penduduk.xlsx"
data = pd.read_excel(file_path)

count_data = data.groupby(["Pendidikan_Terakhir","Jenis_Kelamin"]).size().unstack()

count_data.plot(kind="bar", stacked=True)

plt.title('Jumlah harga Bedasarkan Pendidikan Terakhir dan jenis kelamin')
plt.xlabel("Pendidikan Terakhir ")
plt.ylabel("Jumlah Warga ")
plt.xticks(rotation=45)
plt.legend(title="jenis kelamin")

plt.tight_layout()
plt.show()