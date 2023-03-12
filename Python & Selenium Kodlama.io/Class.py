#class oluşturma 
class Student():
    def __init__(self,name,age,gender): # öğrencilerin tutulması ve oluşturulması
        self.name=name
        self.age=age
        self.gender=gender
NewStudent=Student("Kaan","18","Male")
NewStudent2=Student("Çağlar","20","Male")
NewStudent3=Student("Çağla","24","Female")
NewStudentA=input("name")
#Kullanıcıdan veri alıp class eklenmesi
NewStudentB=input("age")
NewStudentC=input("gender")
NewStudent4=Student(NewStudentA,NewStudentB,NewStudentC)

#ekrana öğrencilerin bilgilerinin yazdırılması
print(f'     {NewStudent.name}--   {NewStudent.age} --  {NewStudent.gender}')
print(f'     {NewStudent2.name} --  {NewStudent2.age}  --{NewStudent2.gender}')
print(f'     {NewStudent3.name}  -- {NewStudent3.age} --  {NewStudent3.gender}')
print(f'     {NewStudent4.name}  -- {NewStudent4.age} --  {NewStudent4.gender}')