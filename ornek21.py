
#1 mil = 1.6093 km olduğuna göre M1 mil (tamsayı) değerinden M2 (tamsayı) değerine kadar birer birer artırarak mil-km tablosu hazırlayan bir program yazınız.

km = float()
i = int()
mil = 1.6093

M1 = int(input("M1:"))
M2 = int(input("M2:"))

for i in range(M1, M2+1):
    km = i * mil
    print("{} mil = {} km" .format(i, km))
