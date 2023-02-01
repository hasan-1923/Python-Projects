#Taş Kağıt Makas oyunu#

import random 

seçenek=["Taş","Kağıt","Makas","q"]
Taş=seçenek[0]
Kağıt=seçenek[1]
Makas=seçenek[2]
q=seçenek[3]
print("Taş Kağıt Makas oyununa hoşgeldiniz...")
while True:
    seçim=input("Seçiminizi yapınız..: Taş-Kağıt-Makas ")
    computer_choice =random.choice(seçenek)
    if seçim==Taş:
        if computer_choice==Taş:
            print("Bilgisayarın Seçimi:Taş , Sonuç=Berabere...")
        elif computer_choice== Kağıt:
            print("Bilgisayarın Seçimi:Kağıt , Sonuç=Kaybettiniz...")
        else:
            print("Bilgisayarın Seçimi:Makas ,Sonuç=Kazandınız...")
    if seçim==Kağıt:
        if computer_choice==Taş:
                print("Bilgisayarın Seçimi:Taş , Sonuç=Kazandınız...")
        elif computer_choice==Kağıt:
                print("Bilgisayarın Seçimi:Kağıt , Sonuç=Berabere...")
        else:
                print("Bilgisayarın Seçimi:Makas , Sonuç=Kaybettiniz...")
    if seçim==Makas:
        if computer_choice==Taş:
                print("Bilgisayarın Seçimi:Taş , Sonuç=Kaybettiniz...")
        elif computer_choice==Kağıt:
                print("Bilgisayarın Seçimi:Kağıt , Sonuç=Kazandınız...")
        else:
                print("Bilgisayarın Seçimi:Makas , Sonuç=Berabere...")     
    if seçim==q:
            print("Oyun Sonlandırıldı....\n Çıkış yapılıyor.")
            break




        

