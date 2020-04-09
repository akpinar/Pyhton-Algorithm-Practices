
#X^K değerini üs alma operatörü (veya eşdeğerlerini) kullanmadan hesaplayan bir program yazınız. Burada X gerçel, K tamsayı değerlerdir.

x = float(input("x:"))
k = int(input("k:"))
i = int()
a = int()

a = x
for i in range(0,k-1):
    x = x * a
    print(x)

