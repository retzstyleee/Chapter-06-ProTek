def starFormation1(n):
	baris = n

	i = 0
	while (i < baris):
		j = 0
		while (j <= i):
			print('* ', end='')
			j += 2
		print('')
		i += 2

def starFormation2(n):
	baris = 0\

	i = n
	while (i >= baris):
		j = 1
		while (j < i):
			print('* ', end='')
			j += 2
		print('')
		i -= 2

n = 7
starFormation1(n)
starFormation2(n)