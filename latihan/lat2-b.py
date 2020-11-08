def starFormation2(n):
	baris = 0\

	i = n
	while (i >= baris):
		j = 0
		while (j < i):
			print('* ', end='')
			j += 1
		print('')
		i -= 1

n = 4
starFormation2(n)