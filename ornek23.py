
#Verilen a ve d değerleri için N elemanlı aritmetik diziyi hesaplayıp görüntüleyen bir program yazınız. Aritmetik dizi: a, a+d, a+2d, a+3d, a+4d, ... , a+(N-1)d

eleman = int()
i = int()

a = int(input("a:"))
d = int(input("d:"))
N = int(input("N:"))

for i in range(0 , N):
    eleman = a + (i * d)
    print(eleman)