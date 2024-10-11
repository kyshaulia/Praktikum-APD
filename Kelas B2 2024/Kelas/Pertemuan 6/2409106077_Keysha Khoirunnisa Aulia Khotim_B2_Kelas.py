# daftar_buku = {
#     "Buku1" : "Harry Potter",
#     "Buku2" : "Percy Jackson",
#     "Buku3" : "Twillight"
# }
# print(daftar_buku["Buku1"])
# print(daftar_buku["Buku2"])
# print(daftar_buku["Buku3"])

# daftar_buku = {}

# daftar_buku["novel 1"] = "Senyum pertama di pagi hari Airin"
# daftar_buku[1] = "Matahari"
# print(daftar_buku)

# nama_dict = {
#     "key1" : "value",
#     "key2" : "value",
#     "key3" : "value"

# Biodata = {
#     "Nama" : "Jay",
#     "NIM" : 77, 
#     "Kelas" : "B"
# }

# daftar_buku = dict(Buku1 = "Harry Potter", Buku2 = "Percy Jackson")
# print(daftar_buku["Buku1"])
# #atau pakai fungsi .get
# print(daftar_buku.get("Buku2"))

# Nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
#}

# for i in Nilai :
#     print(i)

# for i, j in Nilai.items() :
#     # print(f"Nilai dari {i} itu valuenya adalah : {j}")
#     print(j)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# nilai["Struktur Data"] = 99

# nilai.update({"Struktur Data" : 99})
# nilai.update({"Matematika" : 95})
# print(nilai)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(nilai)
# print()
# trashbin = nilai.pop("Matematika")

# print(nilai)
# print()
# print(trashbin)

# del nilai["Matematika"]
# print()
# print(nilai)

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# print(f"Jumlah elemen dari data nilai = ", len(nilai))

# nilai = {
#     "Matematika" : 80,
#     "B. Indonesia" : 90,
#     "B. Inggris" : 81,
#     "Kimia" : 78,
#     "Fisika" : 80
# }
# daftar_nilai = nilai.copy()
# print(daftar_nilai)
# import os

# os.system("cls")
# key = "motor", "mobil", "sepeda"
# value = 2
# daftar_kendaraan = dict.fromkeys(key, value)

# print(daftar_kendaraan)

# Musik = {
#     "The Chainsmoker" : ["All We Know", "The Paris"],
#     "Alan Walker" : ["Alone", "Lily"],
#     "Neffex" : ["Best Of Me", "Memories"]
# }
# #Mengakses key dan value dari dictionary
# for i, j in Musik.items():
#     print(f"Musik milik {i} adalah : ")
#     for song in j :
#         print(song)
#         print("")

# mahasiswa ={
#     101 : {"Nama" : "Aldy", "Umur" : 19},
#     111 : {"Nama" : "Abdul", "Umur" : 18, "Hobi" : ["membaca", "menulis", "ngoding"]}
# }
# # for key, value in mahasiswa.items():
# #     print("ID Mahasiswa : ", key)
# #     for key_a, value_a in value.items():
# #         print(key_a, " : ", value_a)
# #         print("")
# print(mahasiswa[111]["Hobi"][-1])

Data_Mahasiswa = {
    "Nama" : "Jay",
    "Umur" : 19,
    "NIM" : 77,
    "Jurusan" : "Informatika",
    "Angkatan" : 2024
}
data_baru = input("Masukkan data yang ingun ditabahkan : ")
isi_data_baru = input("Masukkan isi data yang baru : ")
Data_Mahasiswa.update({{data_baru} : {isi_data_baru}}) 
print(Data_Mahasiswa)
