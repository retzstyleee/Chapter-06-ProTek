def faktorial(n):
	if n == 0:
		return 1
	else:
		return n * faktorial(n-1)

m = 5
n = 3
print('a. C(', m, ', ', n, ') = ', faktorial(m) / (faktorial(m - n) * faktorial(n)))

m = 10
n = 7
print('b. P(', m, ',', n, ') = ', faktorial(m) / faktorial(m-n))