
#İnç olarak verilen değeri (I) santimetreye (C) ve milimetreye (M) çeviren bir program yazınız. Açıklama: 1 inç = 2.54 cm

I = float(input("inç değeri yazınız:"))
C = float()
M = float()

C = (I * 2.54)
M = C * 100

print("cm: {} \nmm: {}" .format(C,M))