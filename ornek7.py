
#Haftada G gün çalışan ve haftada N lira kazanan bir işçinin saatlik ücretini (U) bulan bir program yazınız. Günlük çalışma süresi 8 saatti

G = float(input("Çalışılan gün sayısı:"))
N = float(input("haftalık kazanılan para"))
gunlukKazanc = float()
saatlikKazanc = float()

gunlukKazanc = N / G
saatlikKazanc = gunlukKazanc / 8
print(saatlikKazanc)