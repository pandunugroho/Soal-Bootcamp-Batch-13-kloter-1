dataKey = ['a','e','i','o','u']
word = str(input("Masukan kata untuk memeriksa huruf vokal: "))

def check(dataKey,word):
	for i in dataKey:
		if i in word:
			print (i,"==>",True)
		else:
			print (i,"==>",False)			 

check(dataKey,word)
