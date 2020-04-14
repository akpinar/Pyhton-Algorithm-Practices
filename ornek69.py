
#M tane satır ve N tane sütundan (* karakteri kullanılarak) oluşturulmuş bir dikdörtgeni ekranın ortasında görüntüleyen bir program yazınız.

M = int(input("M:(satır sayısı)"))
N = int(input("N:(sütun sayısı)"))
i = int()
j = int()

for i in range(0,M):
    print(" ")
    for j in range(0,N):
        print("*" , end= " ")
