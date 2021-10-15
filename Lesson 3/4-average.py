average=0
grade=0
sum=0
count=0

while count < 2:
    print("Öğrenci notunu giriniz: ")
    grade=int(input())
    sum += grade
    count+=1

average = sum/count
print("Ortalama:",average)
