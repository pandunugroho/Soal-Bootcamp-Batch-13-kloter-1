def drawImage(n):
	for i in range((n+1)//2):
		print ('='*((n-(i*2+1))//2)+'@'*(i*2+1)+'='*((n-(i*2+1))//2))
	j = 1
	for i in range((n+1)//2,n):
		print ('='*j+'@'*(n-j*2)+'='*j)
		j = j+1

n = int(input("Masukan Angka ganjil: "))
drawImage(n)
