
#Bir memur, ATM adı verilen otomatik banka makinasından maaşını (M) almıştır. Makine ancak 5, 10 ve 20 milyonluk banknotlar verebilmektedir.
# Büyük kupürlü banknotların sayısı maksimum olacak biçimde ayarlandığına göre
# maaşın kaç tane 20, kaç tane 10 ve kaç tane 5 milyonluk banknottan oluştuğunu bulan bir program yazınız.

banknot20 = int()
banknot10 =int()
banknot5 = int()
kalan1 = int()
kalan2 = int()

M = int(input("Maaşı giriniz:"))

banknot20 = M // 20 #sadece tam kısmı almak için iki // bölme işareti kullanılır
kalan1 = M % 20
banknot10 = kalan1 // 10
kalan2 = kalan1 % 10
banknot5 = kalan2 // 5

print("20'lik: {} tane\n 10'luk: {} tane\n 5'lik: {} tane" .format(banknot20,banknot10,banknot5))
