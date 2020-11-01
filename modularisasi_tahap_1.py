"""
Program menghitung luas segitiga
"""
print('Menghitung luas segitiga 1')
alas = 10
tinggi = 6
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}')

print('\nMenghitung luas segitiga 2 dengan Copy paste')
alas = 20
tinggi = 2
luas_segitiga = alas * tinggi / 2
print(f'Luas segitiga dengan alas {alas} dan tinggi {tinggi} adalah {luas_segitiga}')

print('\nMempersiapkan fungsi hitug_luas_segitiga')
def hitung_luas_segitiga(alas, tinggi):
    luas_segitiga = alas * tinggi / 2
    return  luas_segitiga

alas = 10
tinggi = 6
print (f'Dengan fungsi, Luas segitiga dengan alas {alas} dan tinggi {tinggi} = {hitung_luas_segitiga(10, 6)}')
print (f'Menghitung luas segitiga dengan fungsi {hitung_luas_segitiga(20, 2)}')