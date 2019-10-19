def hitungParkir(jam):
	if 0 < jam <= 3:
		print ('biaya:',jam*2000)
	elif 3 < jam <= 7:
		print ('biaya:',3*2000+(jam-3)*1000)
	elif 7 < jam:
		print ('biaya: 10000')
	else:
		print ('ERROR - Masukan angka positif')

jam = int(input("Lama waktu parkir: "))
hitungParkir(jam)

