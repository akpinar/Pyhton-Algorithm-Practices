
#İndirimli satış kampanyası yapan bir firma, M liralık alışveriş için yüzde olarak verilen R oranında indirim yapılmaktadır.
# Alışverişin M miktarından daha büyük olan bölümü için ise yüzde olarak verilen P oranında indirim yapılmaktadır.
# N liralık alışveriş yapan bir kişinin indirimler düşülünce ödeyeceği miktarı bulan bir program yazınız.

ind1 = int()
ind2 = int()
toplam = float()
fiyatFarki = float()
P2 = int()
R2 = int()


M = float(input("İlk indirim sınırı:"))
R = int(input("İlk inidirim yüzdesi:"))
P = int(input("İkinci indirim yüzdesi"))
N = float(input("Alışveriş tutarı:"))

R2 = 100 - R
ind1 = (M * R2) / 100

if M > N:
    print("Ödenecek tutar:", N)

elif N > M:
    P2 = 100 - P
    fiyatFarki = N - M
    ind2 = (fiyatFarki * P2) / 100
    toplam = ind2 + ind1
    print("Ödenecek tutar:", toplam)

else:
    print("Ödenecek Tutar:", ind1)