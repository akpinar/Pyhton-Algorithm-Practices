
#Santigrat olarak verilen sıcaklığı (C) Fahrenhayt’a (F) çeviren bir program yazınız.  Yardımcı açıklama: C / 100 = (F-32) / 180

santigrad = float(input("Santigrad:"))
fahrenhayt = float()

fahrenhayt = ((santigrad/100) * 180) + 32
print(fahrenhayt)