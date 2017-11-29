def perkalian(a, b, c):
    hasil = a*b*c
    return hasil

def pertambahan(a, b, c=None, d=None):
    hasil = a + b
    if c:
        hasil += c
    if d:
        hasil+= d*100
    return hasil

def pertambahan_koleksi(koleksi):
    hasil = sum(koleksi)
    return hasil

def ganti(mutable):
    if len(mutable) > 0:
        mutable[0] = 'ini udah ganti'

def bintang_satu(*args):
    print(args)

def bintang_dua(**kwargs):
    print(kwargs)

if __name__ == '__main__':
    kali = perkalian(1, 2, 3)
    print(kali)

if __name__ == '__main__':
    kali_lagi = perkalian(1, 2, perkalian(1, 2, 3))
    print(kali_lagi)

if __name__ == '__main__':
    tambah_aja = pertambahan(1, 2)
    print(tambah_aja)
    
if __name__ == '__main__':
    tambah_c = pertambahan(1, 2, 3)
    print(tambah_c)

if __name__ == '__main__':
    tambah_koleksi = pertambahan_koleksi([1,2,3])
    print(tambah_koleksi)

if __name__ == '__main__':
    koleksi = [1,2,3]
    ganti(koleksi)
    print(koleksi)

if __name__ == '__main__':
    tambah_d = pertambahan(1,2, d=9)
    print(tambah_d)

if __name__ == '__main__':
    bintang_satu(1,2,3,4)

if __name__ == '__main__':
    bintang_dua(h=1, b=2, c=4)
