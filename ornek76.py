
#Bir kız voleybol takımındaki öğrencilerin isimleri klavyeden girilmiştir. Daha sonra girilen bir ismin takımda olup olmadığını belirten bir program yazınız.


aranacak_isim = input("aranacak isim:")
while True:
    takim = [input("isim:")]

    for i in range(0,len(takim)):
        if aranacak_isim == takim[i]:
            print("isim bulundu:",aranacak_isim)
    break