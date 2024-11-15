print('Cw1\n')
'''
def pascal(n):
    for i in range(1, n + 1):
        for j in range(0, n - i + 1):
            print(' ', end='')
        C = 1
        for j in range(1, i + 1):
            print(' ', C, sep='', end='')
            C = C * (i - j) // j
        print()
n = int(input("Podaj liczbę wierszy: "))
pascal(n)
'''
print('Cw2\n')
'''
def blizniacze():
    for 
n =1000
'''
print('Cw3\n')
'''
def catalan(n):
    if n <= 1:
        return 1
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
    return res
parzyste=0
nparzyste=0
for i in range(14):
    if catalan(i)%2==0:
        parzyste=parzyste+1
    else:
        nparzyste=nparzyste+1
    print(catalan(i), end=" ")
print('\nLiczba parzystych: ',parzyste)
print('Liczba nieparzystych: ',nparzyste)
'''
print('Cw4\n')
'''
liczba = int(input("Wprowadz liczbe: "))
Sum = 0
for i in range(1, liczba):
    if(liczba % i == 0):
        Sum = Sum + i
if (Sum == liczba):
    print('Liczba jest Liczbą Perfekcyjną.')
else:
    print('Liczba nie jest Liczbą Perfekcyjną.')
'''
print('Cw5\n')


print('Cw6\n')
def poteg(x, n)
    if n = 0:
        return 1
    jeżeli n jest nieparzysta
        zwróć x · (potęga(x, (n - 1)/2))2
    zwróć (potęga(x, n/2))2
