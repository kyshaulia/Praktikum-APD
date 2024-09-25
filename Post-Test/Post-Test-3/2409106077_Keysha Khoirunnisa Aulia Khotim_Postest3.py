print("Kalkulator (Body Mass Index)")

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