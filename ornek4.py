
#Haftanın H sayıda gününde çalışan ve saatlik ücreti U olan bir kısmi zamanlı işçinin haftalık kazancını bulan bir program yazınız.
# Günlük çalışma süresi 8 saattir.

H = int(input("Haftalık çalışma gününü giriniz:"))
U = float(input("Saatlik ücreti giriniz:"))
gunluk = float()
haftalik = float()

gunluk = 8 * U
haftalik = gunluk *  H
print(haftalik)