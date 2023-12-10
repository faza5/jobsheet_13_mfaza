berat = int(input("Masukkan berat anda > "))
satuan = input("satuan apa yang anda masukka ? (K untuk KG, L untuk LBS) > ")
  
if satuan.lower() == 'l':
  print(f"Berat anda dikonversi menjadi kilogram adalah {round(berat * 0.453592)} kg")
elif satuan.lower() ==  'k':
  print(f"Berat anda dikonversi  menjaddi pons adalah {round(berat * 2.20462)} lbs ")
else : 
  print("tidak ada")
