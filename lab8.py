print('Cw1\n')
napis = 'Bezpłatny kalkulator znaków informujący precyzyjnie o objętości tekstu zawsze pod ręką nie musisz liczyć liter ręcznie'
#a
print (len(napis))
#b
print(napis[12])
print(napis[7])
print(napis[-4])
napis2 = napis[12]+napis[7]+napis[-4]
print(napis2)
#c
print(napis+napis2)
#d
print(napis.lower())
#e
print(napis.upper())

print('Cw2\n')
napis = 'Kieplin Kacper'
#a
kk = napis.split()
print(kk)
#b
zamiana = kk[1] + ' ' + kk[0]
print(zamiana)
#c
anagram = napis[4] + napis[5] + napis[13] + napis[9]
print(anagram)
#d
inicjaly = napis[0] + napis[8]
print(inicjaly)
#e
zamiana2 = napis[8] + napis[1:7] + ' ' + napis[0] + napis[9:]
print(zamiana2)

print('Cw3\n')

