def hitungKembalian(uang,bayar):
	kembali = uang - bayar
	x = kembali // 50000
	kembali = kembali % 50000
	y = kembali // 20000
	kembali = kembali % 20000
	z = kembali // 10000
	kembali = kembali % 10000
	a = kembali // 5000
	kembali = kembali %5000
	print (x,'x 50000')
	print (y,'x 20000')
	print (z,'x 10000')
	print (a,'x 5000')
	print (kembali,'Disumbangkan')
	
uang = int(input("Masukan jumlah uang (rupiah) : "))
bayar = int(input("Masukan total biaya (rupiah) : "))
hitungKembalian(uang,bayar)
