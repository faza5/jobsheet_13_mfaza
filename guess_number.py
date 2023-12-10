def guess_number():
    angka_rahasia = 3888
    batas = 99999999
    penghitung = 0

    while penghitung < batas :
        user = int(input("masukkan angka: "))
        if user == angka_rahasia :
            print("selamat, tebakan anda benar")
            break   
        else :
            print ("maaf, tebakan anda salah")
            penghitung +=1
            print("sisa kesempatan anda", batas - penghitung)

    else : 
        print("gagal, angka yang benar adalah {angka_rahasia}")     
 