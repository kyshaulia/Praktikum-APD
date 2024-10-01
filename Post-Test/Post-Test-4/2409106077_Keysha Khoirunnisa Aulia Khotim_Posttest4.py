print("Kalkulator (Body Mass Index)")
print("Silahkan login terlebih dahulu. Kesempatan login hanya 3 kali, jika kesempatan habis program akan berakhir.")

usn = "Keysha"
pw = "77"
salah = 0
while salah < 3 :
    username = input("Masukkan username anda : ")
    password= input("Masukkan password anda : ")
    if pw == password and usn == username :
        print("Login Berhasil")
        break
    else :
        print("Login Gagal")       
        salah += 1 
        print(f"Anda Telah Gagal Login {salah} kali")
    if salah == 3 :
        print("Kesempatan Login Habis. Program Berhenti")
if salah < 3 :
        while True : 
            beratbadan = float(input("Masukkan Berat Badan Anda dalam Satuan Mg : "))
            tinggibadan = float(input("Masukkan Tinggi Badan Anda dalam Satuan Km : "))
            beratbadankg = float(beratbadan/1000000)
            tinggibadanm = float(tinggibadan*1000)
            BMI = float(beratbadankg/tinggibadanm**2) 

            if BMI < 18.5 : 
                print("Berat Badan Kurang (Underweight)")
            elif (BMI < 24.9) :
                print("Berat Badan Normal")
            elif (BMI < 29.9) :
                print("Berat Badan Berlebih (Overweight)")
            else :
                print("Obesitas")
            jawaban = input("Apakah anda ingin menghitung BMI kembali? (ya atau tidak) : ") 
            if jawaban == "ya" :
                continue
            else :
                break
        print("Program Telah Berakhir. Terima Kasih")

    