
#Klavyeden A ve B sayıları girilmektedir. Eğer sayıların toplamı C sayısından büyük ise ekranda BÜYÜK mesajı görüntülenecektir;
# büyük değil ise A sayısı 2 ile, B sayısı 3 ile çarpılacak ve hesaplanan çarpımların toplamının C sayısından büyük olup olmadığı denetlenecektir;
# büyük ise ekrana BÜYÜK yazılacaktır;
# eğer büyük değil ise işlem bu biçimde sürdürülecektir. BÜYÜK mesajının ekranda görüntülenmesi ile program sona erecektir. Programı


A = float(input("A:"))
B = float(input("B:"))
C = float(input("C:"))

while A + B < C:
    A  = A * 2
    B  = B * 3
    print("küçük")

print("BÜYÜK")




