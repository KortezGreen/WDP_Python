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
#a
def parz_str(a):
    return a[0::2]
ciag = 'abra kadabra'
print(parz_str(ciag))

#b
def last_str(a):
    return a[-1]
print(last_str(ciag))

#c
def rev_str():
    a = str(input("Podaj string: "))
    return a[::-1]
print(rev_str())

#d
def palindrom_str():
    a = str(input("Podaj string: "))
    b = a[::-1]
    if a==b:
        return "To palindrom!"
    else:
        return "To NIE palindrom!"
print(palindrom_str())

#e


#f


#g
