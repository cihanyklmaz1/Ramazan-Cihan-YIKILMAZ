kisiListesi = [["Onur",35],["ali",16],["mehmet",88]]

for kisi in kisiListesi:
    if kisi[1] <= 18:
        print("indirimli")
    elif kisi[1] <=60:
        print("normal")