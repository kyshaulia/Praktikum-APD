import os

no_catatan = ["1", "2", "3", "4"]
tanggal_catatan = ["21/09/24", "22/09/24", "23/09/24", "24/0924"]
isi_catatan = ["Hari ini aku belajar matkul kalkulus materi limit, tetap ngerasa susah sih walaupun background dari SMA, tapi gapapa tetp harus di ngerti-ngertiin buat UTS", 
               "Hari ini aku ngabisin waktu di kamar seharian malas-malasan, karena capek setelah 5 hari berkegiatan, mulai dari tugas ospek, sampai tugas-tugas kuliah",
               "Hari ini aku mulai ngerjain tugas-tugas yang sempat tertunda karena kemarin malas-malasan, walaupun hari ini masih ingin malas-malasan juga sii",
               "Hari ini aku akan mencoba lebih produktif dari kemarin, aku mulai bangun pagi, lalu aku berangkat ke majelis untuk mendatangi acara, ternyata hujan turun tepat setelah acara selesai, mengharuskan aku untuk men1ggunakan almamater asrama sebagai pelindung dari hujan"]
os.system('cls || clear')
print("Program CRUD Catatan Pribadi")
print("Program bersifat pribadi, jika anda gagal login tiga kali maka program akan berhenti.")
usn = "Keysha"
pw = "30"
salah = 0 
while salah < 3:
    username = input("Username : ")
    password = input("Password : ")
    if password == pw and username == usn :
        print("Login Berhasil!")
        break
    else :
        print("Login Gagal!")
        salah += 1
        print(f"Anda Telah Gagal Login {salah} kali")
    if salah == 3 :
        print("Kesempatan login habis. Program berhenti.")
        break
    os.system('cls || clear')
if salah < 3 :
    while True :
        os.system('cls || clear')
        print("="*10)
        print("Catatan Ku")
        print("="*10)
        print("[1] Lihat Daftar Catatan")
        print("[2] Tambah Catatan")
        print("[3] Edit Catatan")
        print("[4] Hapus Catatan")
        print("[5] Keluar Program")
        pilihan = input("Masukkan pilihan : ")

        if pilihan == "1" :
            os.system('cls || clear')
            print("="*15)
            print("Lihat Catatan")
            print("="*15)
            os.system('cls || clear')
            index = 0 
            print(f"Tanggal : {tanggal_catatan [index]}")
            print(f"Catatan : {isi_catatan [index]}")

            index = 1 
            print(f"Tanggal : {tanggal_catatan [index]}")
            print(f"Catatan : {isi_catatan [index]}")

            index = 2 
            print(f"Tanggal : {tanggal_catatan [index]}")
            print(f"Catatan : {isi_catatan [index]}")
            
            index = 3 
            print(f"Tanggal : {tanggal_catatan [index]}")
            print(f"Catatan : {isi_catatan [index]}")
            input("Klik enter untuk memilih menu lagi..")
        
        elif pilihan == "2" :
            os.system('cls || clear')
            print("="*15)
            print("Tambah Catatan")
            print("="*15)
            nomorcatatan = input("Masukkan nomor catatan : ")
            tambahcatatan = input("Masukkan tanggal catatan dengan format dd/mm/yy : ")
            isicatatan = input("Masukkan isi catatan : ")
            no_catatan.append(nomorcatatan)
            tanggal_catatan.append(tambahcatatan)
            isi_catatan.append(isicatatan)
            index = 4 
            print(f"Nomor : {no_catatan[index]}")
            print(f"Tanggal : {tanggal_catatan [index]}")
            print(f"Catatan : {isi_catatan [index]}")
            print(no_catatan)
            print(tanggal_catatan)
            print(isi_catatan)
            print("Catatan {tambahcatatan} berhasil di tambahkan")
            input("Klik enter untuk memilih lagi..")
            
        elif pilihan == "3" :
            os.system ('cls || clear')
            print("="*15)
            print(" Edit Catatan")
            print("="*15)
            index = int(input("Masukkan nomor catatan yang ingin edit : "))
            catatan_baru = input("Masukkan catatan yang baru : ")
            isi_catatan[index] = catatan_baru 
            print(f"Catatan ke {index} berhasil di edit")
            print(isi_catatan)
            input("Klik enter untuk memilih lagi..")

        elif pilihan == "4" :
            os.system ('cls || clear')
            print("="*15)
            print("Hapus Catatan")
            print("="*15)
            index = int(input("Masukkan nomor catatan yang ingin dihapus : "))
            del_catatan = isi_catatan.pop(index)
            print(f"Catatan ke {index} berhasil di hapus")
            print(isi_catatan)
            input("Klik enter untuk memilih lagi..")
        
        elif pilihan == "5" :
            print("Anda Telah keluar dari Program")
            break

        else :
            break 




            

    
