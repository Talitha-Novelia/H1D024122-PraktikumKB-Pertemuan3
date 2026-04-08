import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt
from skfuzzy import control as ctrl

barang_terjual = ctrl.Antecedent(np.arange(0,101,1),'barang_terjual')
permintaan = ctrl.Antecedent(np.arange(0,301,1),'permintaan')
harga = ctrl.Antecedent(np.arange(0,100001,1),'harga')
profit = ctrl.Antecedent(np.arange(0,4000001,1),'profit')
stok = ctrl.Consequent(np.arange(0,1001,1),'stok')

barang_terjual['rendah'] = fuzz.trimf(barang_terjual.universe,[0,0,50])
barang_terjual['sedang'] = fuzz.trimf(barang_terjual.universe,[25,50,75])
barang_terjual['tinggi'] = fuzz.trimf(barang_terjual.universe,[50,100,100])

permintaan['rendah'] = fuzz.trimf(permintaan.universe,[0,0,150])
permintaan['sedang'] = fuzz.trimf(permintaan.universe,[75,150,225])
permintaan['tinggi'] = fuzz.trimf(permintaan.universe,[150,300,300])

harga['murah'] = fuzz.trimf(harga.universe,[0,0,50000])
harga['sedang'] = fuzz.trimf(harga.universe,[25000,50000,75000])
harga['mahal'] = fuzz.trimf(harga.universe,[50000,100000,100000])

profit['rendah'] = fuzz.trimf(profit.universe,[0,0,2000000])
profit['sedang'] = fuzz.trimf(profit.universe,[1000000,2000000,3000000])
profit['tinggi'] = fuzz.trimf(profit.universe,[2000000,4000000,4000000])

stok['sedang'] = fuzz.trimf(stok.universe,[0,500,1000])
stok['banyak'] = fuzz.trimf(stok.universe,[500,1000,1000])

rule1 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule2 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule3 = ctrl.Rule(barang_terjual['tinggi'] & permintaan['sedang'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule4 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['sedang'], stok['sedang'])
rule5 = ctrl.Rule(barang_terjual['sedang'] & permintaan['tinggi'] & harga['murah'] & profit['tinggi'], stok['banyak'])
rule6 = ctrl.Rule(barang_terjual['rendah'] & permintaan['rendah'] & harga['sedang'] & profit['sedang'], stok['sedang'])

stok_ctrl = ctrl.ControlSystem([rule1,rule2,rule3,rule4,rule5,rule6])
stok_simulasi = ctrl.ControlSystemSimulation(stok_ctrl)

stok_simulasi.input['barang_terjual'] = 80
stok_simulasi.input['permintaan'] = 255
stok_simulasi.input['harga'] = 25000
stok_simulasi.input['profit'] = 3500000
stok_simulasi.compute()

print("Jumlah Stok Optimal = %.2f unit" % stok_simulasi.output['stok'])
input("Tekan ENTER untuk menampilkan semua grafik...")

barang_terjual.view()
permintaan.view()
harga.view()
profit.view()
stok.view(sim=stok_simulasi)
plt.show()

input("Tekan ENTER untuk keluar...")







