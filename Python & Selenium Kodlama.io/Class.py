#class oluşturma 
class Student():
    def __init__(self,name,age,gender): # öğrencilerin tutulması ve oluşturulması
        self.name=name
        self.age=age
        self.gender=gender
NewStudent1=Student("Kaan","18","Male")
NewStudent2=Student("Çağlar","20","Male")
NewStudent3=Student("Çağla","24","Female")
#Kullanıcıdan veri alıp class eklenmesi
NewStudentA=input("name:").capitalize() # ismin ilk harfi büyütülür
NewStudentB=input("age:")
NewStudentC=input("gender:").capitalize() #ilk harf büyütülür
NewStudent4=Student(NewStudentA,NewStudentB,NewStudentC)

#ekrana öğrencilerin bilgilerinin yazdırılması
print(f'     {NewStudent1.name}--   {NewStudent1.age} --  {NewStudent1.gender}')
print(f'     {NewStudent2.name} --  {NewStudent2.age}  -- {NewStudent2.gender}')
print(f'     {NewStudent3.name}  -- {NewStudent3.age} --  {NewStudent3.gender}')
print(f'     {NewStudent4.name}  -- {NewStudent4.age} --  {NewStudent4.gender}')

print("***************************************************************************")
#öğrencinin bilgilerini değiştirilmesi
NewStudent1.age=24
NewStudent2.age=34
NewStudent3.age=25
print(f'     {NewStudent1.name}--   {NewStudent1.age} --  {NewStudent1.gender}')
print(f'     {NewStudent2.name} --  {NewStudent2.age}  -- {NewStudent2.gender}')
print(f'     {NewStudent3.name}  -- {NewStudent3.age} --  {NewStudent3.gender}')
print(f'     {NewStudent4.name}  -- {NewStudent4.age} --  {NewStudent4.gender}')




