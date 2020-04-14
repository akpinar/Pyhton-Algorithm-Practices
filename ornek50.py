
"""Klavyeden 0 ile 900 arasında değerleri olan sayılar girilmektedir. Sayılar gruplara ayrılmıştır.
Her gurubun sonu 999 sayısının girişi ile belirtilmektedir.
 9999 sayısı ise sayı girişinin sonunu ifade etmektedir. Her sayı grubunun ortalamasını hesaplayan bir program yazınız."""
sayiGrubu = 0
a = int()

while a != 9999:

    toplam = 0
    sayac = 0

    while a != 999:

        a = int(input("1 - 900 arası değer: "))
        if a == 9999:
            break
        toplam += a
        sayac += 1

    if a == 9999:
        print('Program sona erdi')
        break

    a = 0
    toplam -= 999
    sayac -= 1
    sayiGrubu += 1

    if toplam == 0 or sayac == 0:
        print('Sayı girilmedi.')
    else:
        print(sayiGrubu, '. grubun ortalaması: ', toplam / sayac)


