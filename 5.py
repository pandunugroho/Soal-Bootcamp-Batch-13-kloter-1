def nilaiTotal(nama,nim,hadir,tugas,uts,uas):
	print ('Nama :',nama)
	print ('NIM :',nim)
	if hadir == 0 or tugas == 0 or uts == 0 or uas == 0:
		print ('Nilai : E')
	else:
		total = hadir/14*100*1/10+tugas*2/10+uts*3/10+uas*4/10
		if 80 < total <=100:
			grade = 'A'
		elif 70 < total <= 80:
			grade = 'B'
		elif 60 < total <= 70:
			grade = 'C'
		elif 50 <= total <= 60:
			grade = 'D'
		elif 0 <= total < 50:
			grade = 'E'
		print ('Nilai :',grade)

nama = str(input('Nama : '))
nim = str(input('NIM : '))
hadir = int(input('Jumlah Hadir : '))
tugas = int(input('Tugas : '))
uts = int(input('UTS : '))
uas = int(input('UAS : '))

nilaiTotal(nama,nim,hadir,tugas,uts,uas)



