
#Ağırlıkları yüzde olarak Y1, Y2, Y3 ve Y4 olan
# sınavlardan sırasıyla N1, N2, N3 ve N4 notlarını alan öğrencinin ağırlıklı not ortalamasını bulan bir program yazınız.

Y1 = float(input("1. sınav ağırlık yüzdesi:"))
Y2 = float(input("2. sınav ağırlık yüzdesi:"))
Y3 = float(input("3. sınav ağırlık yüzdesi:"))
Y4 = float(input("4. sınav ağırlık yüzdesi:"))
N1 = float(input("1. Sınav notu:"))
N2 = float(input("2. Sınav notu:"))
N3 = float(input("3. Sınav notu:"))
N4 = float(input("4. Sınav notu:"))

ort1 = float()
ort2 = float()
ort3 = float()
ort4 = float()
genelOrt = float()

ort1 = (N1 * Y1) / 100
ort2 = (N2 * Y2) / 100
ort3 = (N3 * Y3) / 100
ort4 = (N4 * Y4) / 100
genelOrt = ort1 + ort2 + ort3 + ort4

print(genelOrt)

