
#F liraya satılan bir ürünün yüzde cinsinden KDV oranı K olduğuna göre ürünün KDV’li satış fiyatını bulan bir program yazınız.

F = float(input("İlk Fiyat:"))
K = float(input("KDV Oranı:"))
faizliFiyat = float()
faizliEklentisi = float()

faizliEklentisi = (F * K) / 100
faizliFiyat = F + faizliEklentisi

print(faizliFiyat)