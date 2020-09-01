from cohort import Cohort
from exercise import Exercise
from instructor import Instructor
from student import Student

exercise1 = Exercise('Hello World JS', 'Javascript')
exercise2 = Exercise('Hello World RoR', 'Ruby on Rails')
exercise3 = Exercise('Hello World C', 'C#')
exercise4 = Exercise('Hello World J', 'Java')

cohort32 = Cohort('Day 32')
cohort9 = Cohort('Evening 9')
cohort33 = Cohort('Day 33')

Jim = Student('Jim', 'Bloom', 'JimBloom')
John = Student('John', 'Johner', 'Johnnnyyy')
Janger = Student('Jang', 'Er', 'JangerMan')
James = Student('James', 'Smith', 'Fauhs')

cohort32.add_student(Jim)
cohort33.add_student(John)
cohort9.add_student(Janger)
cohort33.add_student(James)

Sally = Instructor('Sally', 'Flemming', 'SalFlem', 'Farting')
Larry = Instructor('Larry', 'Yrral', 'Larrrr', 'Fencing')
Lu = Instructor('Lu', 'LJ', 'Plre', 'Swimming')

cohort32.add_instructor(Sally)
cohort33.add_instructor(Larry)
cohort9.add_instructor(Lu)

Sally.assign_exercise(exercise1, Jim)
Sally.assign_exercise(exercise2, John)
Larry.assign_exercise(exercise3, Janger)
Larry.assign_exercise(exercise4, James)
Lu.assign_exercise(exercise1, James)
Lu.assign_exercise(exercise2, Janger)
Lu.assign_exercise(exercise3, John)
Larry.assign_exercise(exercise4, Jim)


students = list()
students.append(Jim)
students.append(John)
students.append(Janger)
students.append(James)

exercises = list()
exercises.append(exercise1)
exercises.append(exercise2)
exercises.append(exercise3)
exercises.append(exercise4)

for student in students:
  report = f"{student} is working on "
  length = len(student.exercise)
  for i in range(length -1):
    report += f"{student.exercise[i]}, "
  report += f"and {student.exercise[length -1]}"
  print(report)