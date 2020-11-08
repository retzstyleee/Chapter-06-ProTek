def luasSegitiga(a, t=0):
	luas = a * t / 2
	return luas
def totalLuas(luas1, luas2):
	total = luas1 + luas2
	return total

alas1 = 10
tinggi1 = 20
print('Luas segitiga dg alas', alas1, 'dan tinggi', tinggi1, 'adalah', luasSegitiga(alas1, tinggi1))

alas2 = 15
tinggi2 = 45
print('Luas segitiga dg alas', alas2, 'dan tinggi', tinggi2, 'adalah', luasSegitiga(alas2, tinggi2))

print('Total luas kedua segitiga adalah', totalLuas(luasSegitiga(alas1, tinggi1), luasSegitiga(alas2, tinggi2)))