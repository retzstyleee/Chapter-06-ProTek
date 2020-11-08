def starFormation1(n):
	baris = n

	i = 0
	while (i < baris):
		j = 0
		while (j <= i):
			print('* ', end='')
			j += 1
		print('')
		i += 1

n = 4
starFormation1(n)