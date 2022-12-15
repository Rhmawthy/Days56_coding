#program deret bintang secara terbalik dan tidak, jika angka yg di masukkan ganjil deret bintangnya terbalik dan jika angka yg di masukkan genap deretnys normal

x = int(input("masukkan angka : "))

if x %2 == 0 :
	for i in range (1,x+1):
		print(i*"*")
	
elif x %2 != 0 :
	for i in range (x+1,0,-1):
		print(i*"*")
