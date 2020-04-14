
#Üç basamaklı bir tamsayının basamakları toplamını bulan bir program yazınız.

sayi = int(input("3 basamaklı sayı:"))
yuzler = int()
onlar = int()
birler = int()
fark = int()

yuzler = sayi // 100
fark = sayi - (yuzler*100)
onlar = fark // 10
birler = fark % 10

print("basamak toplamları:{}".format(yuzler + onlar + birler))