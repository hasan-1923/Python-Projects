#öğrencilerin isimlerini tutulduğu liste oluşturulması

studenst=["Oğuzhan Türk","Kaan ERTUĞRUL","Alper ÇAĞLAR"]
#Kullanıcıdan listeye öğrenci ekleme 
NewStudent=input("Lütfen Öğrenci ad ve soyad giriniz:") 
studenst.append(NewStudent)
print(studenst)
print("**********************************************")
#Kullanıcıdan listeden öğrenci bilgisi silme işlemi yaptırma
DeleteStudent=input("Silinecek öğrenci ad ve soyad giriniz:")
studenst.remove(DeleteStudent)
print(studenst)
print("**********************************************")

#listemize kullanıcının 2 öğrenciyi fonskiyon ile listeye eklemesi
def NewStudenst2():
    NewStudenst3=input("Lütfen Öğrenci ad ve soyad giriniz:")
    NewStudenst4=input("Lütfen Öğrenci ad ve soyad giriniz:")
    studenst.extend([NewStudenst3,NewStudenst4])
    return studenst
NewStudenst2()
print(studenst)

print("**********************************************")

# listeden öğrencileri tek tek gösteren fonskiyon
def studentsLoop():
    for i in range(len(studenst)):
        print(studenst[i])

studentsLoop()
print("***********************************************")
def StudentsNumberLoop():
    i=0
    while i<len(studenst):
        print(f"{(studenst[i]),studenst.index(studenst[i])}")
        i +=1
StudentsNumberLoop()        