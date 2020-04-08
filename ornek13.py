
#A, B ve C sayıları verilmiştir.
# Bu sayıları kullanarak A+B, A+C ve B+C toplamları ile bu toplamların ortalamasını hesaplayıp görüntüleyen bir program yazınız.

A =float(input("A:"))
B = float(input("B:"))
C = float(input("C:"))
top1 = float()
top2 = float()
top3 = float()
ortalama = float()

top1 = A + B
top2 = A + C
top3 = B + C
ortalama = (top1 + top2 + top3) / 3

print("A + B = {}\n A + C = {}\n B + C = {}\n Ortalam = {}" .format(top1, top2, top3, ortalama))