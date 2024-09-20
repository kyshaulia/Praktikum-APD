# cuaca = "Cerah"
# if cuaca == "Cerah"
#   print("Kamu pergi keluar rumah")

#jika operator perbandingan harus pakai dua tanda (=) karna kalau satu tidak terbaca

#cuaca = input("Masukkan cuaca hari ini : ")
#if cuaca == "cerah":
#   print("kamu keluar rumah")
 
#cuaca = input("Masukkan cuaca hari ini : ")
#if cuaca == "cerah":
 #  print("kamu keluar rumah")
#else :
 #   print("kamu tetap dirumah")

#cuaca = input("Masukkan cuaca hari ini : ")
#if cuaca == "cerah" :
#   print("Kamu keluar rumah")
#elif cuaca == "mendung" :
#    print("Baca komik dirumah")
#else : 
#    print("Kamu tidur di rumah")

#opsi = input("""Pilih menu:
#1. kondisi 1
#2. kondisi 2
#3. kondisi 3\n""")
#f opsi == "1" :
#elif opsi == "2":
#    print("kondisi 2")
#elif opsi == "3" :
#    print("kondisi 3")
#else :
#    print("input tidak valid")

#umur = int(input("Masukkan umur : "))
#if umur < 0 :
#    print("input tidak valid")
#elif (umur <= 10) and (umur > 0) :
#    print("Bocil")
#elif (umur <= 18) and (umur > 10) :
#    print("Remaja")
#elif (umur <= 36) and (umur > 18) :
#    print ("Dewasa")
#elif (umur <= 66) and (umur > 36) :
#    print ("Parubaya")
#else :
#    print("lansia")

#angka = int(input("Masukkan angka: "))
#result = "genap" if angka % 2 == 0 else "ganjil"

#print(angka, "adalah angka", result)

#a = 10
#b = 20
#print("a lebih besar dari b") if a > b else print("a lebih kecil dari b")

#if a < b :
#    print("a lebih kecil dari b")
#else :
#    print("a lebih besar dari b")

#string = ""
#int = 0
#print(bool(string))
#print(bool(int))

#string = "ab"
#int = 2
#print(bool(string))
#print(bool(int))

#penggunaan and, or, not
#a = 10
#b = 20
# a = 33
# b = 20
# if a < b and a % 2 == 0 :
#     print("a lebih kecil dari b dan a bilangan genap")
# elif a > b or a % 2 == 0 :
#     print("a lebih besar dari b atau a bilangan genap")
# else :
#     print("a lebih besar dari b dan a bilangan ganjil")


print("""Pilih menu:
# 1. kondisi 1
# 2. kondisi 2
# 3. kondisi 3""")
opsi = input("pilih menu: ")
match opsi:
    case "1":
        print("kondisi 1")
    case "2":
        print("kondisi 2")
    case "3":
        print("kondisi 3")
    case _:
        print("input tidak valid")