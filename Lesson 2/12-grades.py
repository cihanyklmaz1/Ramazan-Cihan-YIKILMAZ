print("Sınav sonuç bilgisini giriniz")
grade = int(input())
if grade>=90:
    print("a")
elif grade>=80:
    print("b")
elif grade>=70:
    print("c")
elif grade>=60:
    print("d")
elif grade>60:
    print("e")
else:
    print("f")