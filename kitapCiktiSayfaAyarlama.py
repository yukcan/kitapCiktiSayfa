#yaprak başına 2 sayfa düzeninde önlü arkalı çıktı almak için sayfa sayılarını veren program

sayfaSayisi = int(input("Sayfa sayisi: "))

print("On sayfa:")
sayac = 1
for x in range(1,sayfaSayisi+1):
    if(sayac <= 2):
        print(x, end=",")
        sayac += 1
    elif(sayac > 2 and sayac < 4):
        sayac += 1
    else:
        sayac = 1
print("\nArka sayfa")
sayac = 1
for x in range(3,sayfaSayisi+1):
    if(sayac <= 2):
        print(x, end=",")
        sayac += 1
    elif(sayac > 2 and sayac < 4):
        sayac += 1
    else:
        sayac = 1