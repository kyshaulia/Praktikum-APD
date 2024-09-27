# ulang = 10 
# for i in range(ulang) :
    # print("Perulangan ke-" +str(i) + " kali")
    # print(f"Perulangan ke--{i} kali")

# for i in range (1, 11):
#     print(f"Perulangan ke-{i} kali")

# simpan = [12, "udin petot", 14.5, True, "A"]
#for i in simpan :
    #print(i)

#print(simpan[2])

# for i in range(1, 4):
#     for j in range(1, 4):
#         print(f"{i} x {j} = {i * j}")
#     print()

# for i in range(1, 6, 2):
#     for j in range(1, 6, 2):
#          print(f"{i} x {j} = {i * j}")
#     print()

# ayam = 10
# ayam -= 1
# for i in range(10, -1, -1):
#     print(f"anak ayam turun {i}")

# ulang = "ya"
# hitung = 1
# while ulang == "ya" or ulang == "Ya":
#     print(f"Perulangan ke-{hitung}")
#     ulang = input("Apakah anda masih ingin mengulang? ")
#     hitung += 1
# print("Perulangan selesai")

# x = 0 
# while x < 5 :
#     print(x)
#     x += 1

# hitung = 1
# while True :
#     print(f"perulangan ke-{hitung}")
#     ulang = input("Apakah anda masih ingin mengulang? ")
#     if ulang == "tidak" :
#         print("Perulangan Berhenti")
#         break
#     hitung += 1
# print(f"Total Perulangan : {hitung}")

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     print(i)

# for i in range(10):
#     if i % 2 == 0:
#         continue
#     if i == 5:
#         break
#     print(i)

usn = "admin"
pw = int(12345678)
salah = 0
while salah < 3 :
    username = input("username :")
    password = int(input("password : "))
    if usn == username and pw == password :
        print("login berhasil")
        break
    else : 
        print("Login gagal")
    salah += 1