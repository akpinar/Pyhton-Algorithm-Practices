
#A liranın yüzde cinsinden verilen N yıllık faiz oranı ile T yılda kaç lira faiz getireceğini bulan bir program yazınız.

A = float(input("Para miktarını giriniz:"))
N = float(input("Faiz oranını giriniz:"))
T = float(input("Yılı giriniz:"))
faiz = float()
faizFiyati = float()

faiz = (A * N) / 100
faizFiyati = faiz * T
print(faizFiyati)