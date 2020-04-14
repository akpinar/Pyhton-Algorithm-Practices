
#1’den 10’a kadar olan tamsayılar için bir çarpım tablosu hazırlayan bir program yazınız.

carpim = int()

for i in range(1,11):
    for j in range(1,11):
        #carpim = i * j
        print("{} x {} = {}".format(i,j,(i*j)))