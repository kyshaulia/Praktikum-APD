# list = ["a", 2, True, [1,2,3]]

# print(list[3][2])

# list1 = ["a"
#         2,
#         True,]

# print(list[list1])

tas = ["buku", 32, True, 3.14, ["IF", 24]]
for i in tas :
    print(i)

# for i in range (len(tas)) :
#     print(tas[i])

#manipulasi list
# matkul = ["kalkulus", "fisdas", "pti"]
# print(matkul)

# matkul.append("Sastra Mesin")
# print(matkul)
#cara sisipkan list baru
# matkul.insert(1, "Sastra Mesin")
# print(matkul)

# matkul.insert(1, "Sastra Mesin")
# print(matkul)

# matkul[1] = "Fisika Quantum"
# print(matkul)

# del matkul [1]
# print(matkul)

# buang = matkul.pop(1)
# print(matkul)
# print(f"variable buang = {buang} ")

# prodi = ["Informatika", "Sistem Informasi", "Teknik Arsitektur", "Teknik Lingkungan", 
#          "Teknik Pertambangan", "Teknik Pertambangan", "TeknikElektro", 
#          "Teknik Industri", "Teknik Sipil", "Teknik Geologi", "Teknik Kimia"]
# print(prodi[::2],"\n", prodi)

# pyrochar = ["hu tao", "klee"]
# hydrocar = ["lapu lapu"]

# party = pyrochar + hydrocar 
# print(party)

# print(pyrochar*3)

# barang = [["Sepatu", "tas", "baju"], 
#           ["pulpen", "pensil", "laptop"]]
# print(barang[1][1])
# print(barang[-2][-1])
# print(barang)
# for i in barang :
#     for j in i :
#         print(j)
# for baris in barang :
#     for kolom in baris :
#         print(kolom)

# perabotan = []
# print(perabotan)
# perabotan.append("Meja")
# print(perabotan)

# nama = ("aldi", "daffa", "jay")
# print(nama)

# barang1 = ("Sepatu", "tas", "baju")
# barang2 = ("pulpen", "pensil", "laptop")
# barangtotal = (barang1, barang2)
# print(barangtotal)

# mahasiswa = (69, "Informatika", "24345678", "Jay")
#lalu kita unpacking
# absen, prodi, nim, nama = mahasiswa
# maka ketiga variabel tersebut akan berisi data dari tuple mahasiswa
# menampilkan variabel
# print(absen)
# print(prodi)
# print(nim)
# print(nama)

# mahasiswa = (69, "Informatika", "24345678", "Jay")
# print(mahasiswa)

# mahasiswa = list(mahasiswa)
# mahasiswa[2] = "2409106077"

# mahasiswa = tuple(mahasiswa)
# print(mahasiswa)