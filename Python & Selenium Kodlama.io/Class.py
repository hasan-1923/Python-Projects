class Student():
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
NewStudent=Student("Kaan","18","Male")
NewStudent2=Student("Çağlar","20","Male")
NewStudent3=Student("Çağla","24","Female")


print(f'     {NewStudent.name}--   {NewStudent.age} --  {NewStudent.gender}')
print(f'     {NewStudent2.name} --  {NewStudent2.age}  --{NewStudent2.gender}')
print(f'     {NewStudent3.name}  -- {NewStudent3.age} --  {NewStudent3.gender}')