hedefSayi = 31
print("0 ile 100 arasında bir sayı yazınız")
grade=int(input())

while grade != hedefSayi:
    if grade <= hedefSayi:
        print("Büyüt")
    elif grade >= hedefSayi:
        print("Küçült")
    else:
        print("Tebrikler")
        