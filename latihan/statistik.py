def sum(*myData):
	jumlah = 0
	i = 0

	for data in myData:
		jumlah += data
		i += 1
	print('Jumlah bilangan dari', myData, 'adalah', jumlah)

def average(*myData):
	sum = 0
	i = 0

	for data in myData:
		sum += data
		i += 1

	rata2 = sum / i
	print('Rata-rata bilangan dari', myData, 'adalah', rata2)

def maks(*myData):
	terbesar = ()
	print('Nilai maksimum dari bilangan', myData, 'adalah', max(myData))

def minimum(*myData):
	terkecil = ()
	print('Nilai minimum dari bilangan', myData, 'adalah', min(myData))