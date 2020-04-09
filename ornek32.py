
#Girilen M ve N sayılarının her ikisi de pozitif ise ekrana POZİTİF,
# her ikisi de negatif ise ekrana NEGATİF, aksi halde ekrana HİÇBİRİ yazan bir program yazınız.

M = int(input("M:"))
N = int(input("N:"))

if M < 0 and N < 0:
    print("negatif")

elif M > 0 and N > 0:
    print("pozitif")

else:
    print("hiçbiri")