from student import Student
from StudentMba import StudentMba


std1 = Student("othman","Business", 3.1 , False)
std2 = Student("Jim","Account", 2.1 , False)
std3 = Student("Mark","Technology", 4.1 , True)
std4 = StudentMba("Jack", "Mba Affaire" , 3.01 , True)

print(std3.name)
print(std3.on_honor_roll())


print(std4.name)
print(std4.on_honor_roll())


