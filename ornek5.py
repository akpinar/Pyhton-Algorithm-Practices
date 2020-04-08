
#Kilometre başına B litre benzin harcayan bir otomobilin,
# K kilometre sonra harcadığı benzin miktarını ve benzinin litre fiyatı F olduğuna göre harcanan benzinin parasal tutarını hesaplayan bir program yazınız.

B = float(input("Kilometre başına harcanan benzin:(Litre)"))
K = float(input("Gidilen kilometre:"))
F = float(input("Benzinin litre fiyatı:"))
harcananBenzin =  float()
toplamFiyat = float()

harcananBenzin = B * K
toplamFiyat = harcananBenzin * F

print(toplamFiyat)
