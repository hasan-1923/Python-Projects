#Hesap Makinesi#

sayi_1=int(input("sayi Giriniz.."))

sayi_2=int(input("sayi Giriniz"))

islem=input("islem Giriniz") 

toplama=(sayi_1)+(sayi_2) 

cikarma=(sayi_1)-(sayi_2)

carpma=(sayi_1)*(sayi_2)


if islem =="+":
    print("sonuc:", toplama)
elif islem=="-":
    print("sonuc:",cikarma)
elif islem=="*":
    print("sonuc:",carpma)
elif islem=="/":
    if sayi_2==0:
        print("2.sayi sıfır olamaz...")
    else:
        bolme=(sayi_1)/(sayi_2)
        
        print("sonuc:",bolme)
else:
    print("Hatali islem") 

print(sayi_1,sayi_2)







