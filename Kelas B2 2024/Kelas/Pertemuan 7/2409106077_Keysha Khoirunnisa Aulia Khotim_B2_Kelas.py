# def aku_fungsi () :
#     print("hello world")
# aku_fungsi()

# def tambah(a,b):
#     hasil = a + b 
#     print(hasil)

# tambah(10, 2)

# def tambah(a,b):
#     hasil = a + b 
#     return hasil

# tambahan = tambah(2,4) + tambah(4,6)
# print(tambahan)

# def tambah(a,b):
#     hasil = a + b 
#     return 2

# tambahan = tambah(2,4) + tambah(4,6)
# print(tambahan)

# def pilihan (opsi):
#     opsi = input("Masukkan pilihan : ")
#     match opsi :
#         case 1 :
#             print(1)
#             # return
#         case 2 :
#             print(2)
#             # return
#     print(3)
# pilihan(2)

# def cetak(nama, nim, **matkul):
#     print(nama, nim, matkul)

# cetak("jay", 41, kalkulus = 75, fisikadasar = 38)

# def cetak(nama, nim, matkul):
#     print(nama, nim, matkul)

# cetak("jay", 41, "kalkulus")


# var = 2, 4, 5
# var1, var2, var3 = var
# print(var)
# print(var1)
# print(var2)
# print(var3)

# yang ada didalam def bisa mengakses variabel diluar
# tetapi yang diluar tidak bisa mengakses yang ada didalam def
# Nama = "Informatika"
# Mata_Kuliah = "Algoritma dan Pemrograman Dasar"
# kelas = "b"
# def info():
#     Nama = "Teknik Elektro"
#     Mata_Kuliah = "Pengantar Teknik ELektro"
#     print("Nama :", Nama)
#     print("Mata Kuliah :", Mata_Kuliah)
#     print("Kelas :", kelas)
# info()
# print("Prodi:", Nama)
# print("Mata Kuliah:", Mata_Kuliah)

def cetak(nama, nim, umur = 18):
    print(nama, nim, umur)
cetak("jay", 77, 22)