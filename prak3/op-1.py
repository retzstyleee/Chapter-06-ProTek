from operation import *

a = 2
b = 4
c = 6
print('a. ', a, '+', b, 'x', c, '-', b, '=', kurang(jumlah(a, kali(b, c)), b))

a = 4
b = 6
c = 7
d = 9
print('b. (', a, '+', c, ') x (', b, '-', d, ') =', kali(jumlah(a, c), kurang(b, d)))

a = 2
b = 5
c = 7
d = 10
e = 12
f = 34
print('c. (', d, '+', a, ') / (', c, '+', b, ') / (', e, '-', f, ') =',bagi(bagi(jumlah(d, a), jumlah(c, b)),kurang(e,f)))