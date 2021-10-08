print("1. kişinin yaşını girin")
yas1 = int(input())
print("2. kişinin yaşını girin")
yas2 = int(input())
print("3. kişinin yaşını girin")
yas3 = int(input())

enbuyuk = yas1
if yas1 < yas2:
    enbuyuk=yas2
elif yas1 < yas3:
    enbuyuk=yas3
else:
    enbuyuk=yas1
print(enbuyuk,"adam")