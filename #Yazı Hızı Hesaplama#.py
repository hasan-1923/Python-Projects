#Yazma Hızı Hesaplama#

import time
import datetime

print("Yazmaya 3 saniye sonra başlayabilirsiniz..:")

print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("Başlayınız..")
time.sleep(0.3)
before=datetime.datetime.now()

text=input("yazınız..")
after=datetime.datetime.now()

speed=after-before
seconds=round(speed.total_seconds(),2)
speed_per_letter=round(len(text)/seconds,1)

print("Metni yazma hızınız :{}" .format(seconds))
print("Bir saniyelik yazma hızınız:{}" .format(speed_per_letter))