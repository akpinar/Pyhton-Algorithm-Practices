
#İki dik kenar (a ve b) ile hipotenüs (c) uzunlukları verilen bir dik üçgende
# hipotenüse ait yüksekliği (h), üçgenin alanını (n) ve dik üçgenin çevresini (v) hesaplayan bir program yazınız.

a = float(input("1. kenar:"))
b = float(input("2. kenar:"))
c = float(input("hipotenüs:"))
yukseklik = float()
alan = float()
cevre = float()

yukseklik = (a * b) / c
alan = (a * b) / 2
cevre = a + b + c

print("Yukseklik: {}\n Alan: {}\n Cevre: {}" .format(yukseklik, alan, cevre))
