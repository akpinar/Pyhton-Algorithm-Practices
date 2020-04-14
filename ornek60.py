
#M ve N tamsayıları arasında 5 ile veya 7 ile tam bölünebilen tamsayıların kaç tane olduğunu hesaplayan bir başka program yazınız.

M = int(input("M:"))
N = int(input("N:"))
sayac = 0

for i in range (M,N+1):
    if (i % 5 == 0) or (i % 7 ==0):
        sayac = sayac + 1

print(sayac)