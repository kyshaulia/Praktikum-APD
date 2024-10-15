import os

catatan = [
    {
        "Tanggal" : "21/09/24", 
        "Isi Catatan" : "Hari ini aku belajar matkul kalkulus materi limit, tetap ngerasa susah sih walaupun background dari SMA, tapi gapapa tetp harus di ngerti-ngertiin buat UTS"
    },
    {
        "Tanggal" : "22/09/24",  
        "Isi Catatan" : "Hari ini aku ngabisin waktu di kamar seharian malas-malasan, karena capek setelah 5 hari berkegiatan, mulai dari tugas ospek, sampai tugas-tugas kuliah"
    }, 
    {
        "Tanggal" : "23/09/24", 
        "Isi Catatan" : "Hari ini aku mulai ngerjain tugas-tugas yang sempat tertunda karena kemarin malas-malasan, walaupun hari ini masih ingin malas-malasan juga sii"
    }, 
    {
        "Tanggal" : "24/09/24", 
        "Isi Catatan" : "Hari ini aku akan mencoba lebih produktif dari kemarin, aku mulai bangun pagi, lalu aku berangkat ke majelis untuk mendatangi acara, ternyata hujan turun tepat setelah acara selesai, mengharuskan aku untuk men1ggunakan almamater asrama sebagai pelindung dari hujan"
    }
]

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
        os.system('cls || clear')

        if pilihan == "1" :
            print("="*15)
            print("Lihat Catatan")
            print("="*15)
            for i in range(len(catatan)) :
                print(f"Catatan ke {i+1}")
                print(f"Tanggal : {catatan[i]['Tanggal']}")
                print(f"Isi Catatan : {catatan[i]['Isi Catatan']}")
            input("Klik enter untuk memilih lagi..")
            os.system('cls || clear')

        elif pilihan == "2" :
            os.system('cls || clear')
            print("="*15)
            print("Tambah Catatan")
            print("="*15)
            tanggalcatatan = input("Masukkan tanggal catatan dengan format dd/mm/yy : ")
            isicatatan = input("Masukkan isi catatan : ")
            catatan.append({
                "Tanggal" : tanggalcatatan,
                "Isi Catatan" : isicatatan
            })
            print(f"Catatan berhasil di tambahkan")
            input("Klik enter untuk memilih lagi..")
            
        elif pilihan == "3" :
            os.system ('cls || clear')
            print("="*15)
            print(" Edit Catatan")
            print("="*15)
            for i in range(len(catatan)) :
                print(f"Catatan ke {i+1}")
                print(f"Tanggal : {catatan[i]['Tanggal']}")
                print(f"Isi Catatan : {catatan[i]['Isi Catatan']}")
            index = int(input("Masukkan index catatan yang ingin di edit : "))
            if index > len(catatan) or index < 0 :
                print("Index tidak ditemukan")
                input("Klik enter untuk memilih lagi..")
                os.system('cls || clear')
            else :
                catatan_baru = input("Masukkan tanggal catatan yang baru : ")
                isicatatan_baru = input("Masukkan isi catatan yang baru : ")
                catatan[index-1]['Tanggal'] = catatan_baru
                catatan[index-1]['Isi Catatan'] = isicatatan_baru
                print("Catatan berhasil di edit")
                input("Klik enter untuk memilih menu lagi..")
                os.system('cls || clear')

        elif pilihan == "4" :
            os.system ('cls || clear')
            print("="*15)
            print("Hapus Catatan")
            print("="*15)
            for i in range(len(catatan)) :
                print(f"Catatan ke {i+1}")
                print(f"Tanggal : {catatan[i]['Tanggal']}")
                print(f"Isi Catatan : {catatan[i]['Isi Catatan']}")
            index = int(input("Masukkan index catatan yang ingin dihapus : "))
            if index > len(catatan) or index < 0 :
                print("Index tidak ditemukan")
                input("Klik enter untuk memilih lagi..")
                os.system('cls || clear')
            else :
                del_catatan = catatan.pop(index-1)
            print(f"Catatan berhasil di hapus")
            input("Klik enter untuk memilih lagi..")
        
        elif pilihan == "5" :
            print("Anda telah keluar dari program")
            break

        else :
            break 