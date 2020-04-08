
#X, Y ve Z sayıları verilmiştir.
# Bu sayıları kullanarak X-Y, X-Z ve Y-Z farkları ile bu farkların ortalamasını hesaplayıp görüntüleyen bir program yazınız.

X = float(input("X:"))
Y =float(input("Y:"))
Z = float(input("Z:"))
fark1 = float()
fark2 = float()
fark3 = float()
ortalama = float()

fark1 = X - Y
fark2 = X - Z
fark3 = Y - Z
ortalama = (fark1 + fark2 + fark3) / 3

print("X - Y = {}\n X - Z = {}\n Y - Z = {}\n Ortalama = {}" .format(fark1, fark2, fark3, ortalama))