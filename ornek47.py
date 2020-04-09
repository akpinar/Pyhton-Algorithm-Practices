
#Klavyeden pozitif ve negatif sayılar girilmektedir.
# Bilgi girişi, sıfır girilmesi ile sona ermektedir.
# Pozitif ve negatif sayıların ortalamalarını ayrı ayrı hesaplayan bir program yazınız.

pozOrt = float()
negOrt= float()
pozToplam = int()
negToplam = int()
pozSayac = 0
negSayac = 0

while True:
    a = int(input("sayi:"))

    if a == 0:
        break

    elif a > 0:
        pozToplam = pozToplam + a
        pozSayac = pozSayac + 1

    else:
        negToplam = negToplam + a
        negSayac = negSayac + 1

pozOrt = pozToplam / pozSayac
negOrt = negToplam / negSayac

print("Pozitif Toplam: {}\n Pozitif Ortalama: {}\n Negatif Toplam: {}\n Negatif Ortalama: {}" .format(pozToplam,pozOrt,negToplam,negOrt))
