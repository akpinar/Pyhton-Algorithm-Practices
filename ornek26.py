
#F(x) = 5x3 – 7*x2 + 4x – 1 + 8x^-1 fonksiyonunun aldığı değerleri x’in 3’ten 8’e kadar olan değerleri için 0.25’lik adımlarla hesaplayıp tablo halinde görüntüleyen bir program yazınız.

x = float()
f = float()

for x in numpy.arange(3,9,0.25)

    f = (5 * x * x * x) - (7 * x * x) + (4 * x) + (8 / x) - 1
    print("{} değeri için sonuç = {}".format(x,f))