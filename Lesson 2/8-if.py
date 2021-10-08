arabalar = ["ford","mercedes","audi","honda","nissan","bmw"]

for araba in arabalar:
    if araba == "bmw":
        print(araba.upper())
    else:
        print(araba.title())

for araba in arabalar:
    if araba in arabalar:
        if araba != "bmw":
            print(araba.title)
        else:
            print(araba.upper)