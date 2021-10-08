kisiListesi = [["Onur",35],["ali",16],["mehmet",88]]
for kisi in kisiListesi:
    if kisi[1] >= 18 and kisi[1] <= 85:
        print(kisi[0],"Ehliyet alabilir.")
    else:
        print(kisi[0],"Ehliyet alamaz.")
print("------------------------")

for kisi in kisiListesi:
    if kisi[1] > 65 or kisi[1] < 18:
        print(kisi[0],"çalışabilir.")
    else:
        print(kisi[0],"çalışamaz.")