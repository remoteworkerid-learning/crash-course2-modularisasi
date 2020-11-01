#cara 2
import geometri.segitiga
print(f'\ncara 2 hitung luas segitiga {geometri.segitiga.hitung_luas_segitiga(10, 3)}')

#cara 3
import geometri.segitiga as gs
print(f'\ncara 3 hitung luas segitiga {gs.hitung_luas_segitiga(10, 3)}')

#cara 1 - terbaik
#menambah modul info

from geometri.segitiga import hitung_luas_segitiga, info as info_segitiga
from geometri.persegipanjang import hitung_luas_persegi_panjang, info as info_persegipanjang

print(info_segitiga())
print(f'\nhitung luas segitiga {hitung_luas_segitiga(10, 3)}')

print(info_persegipanjang())
print(f'hitung_luas_persegi_panjang {hitung_luas_persegi_panjang(10, 3)}')