class Cohort:
  def __init__(self, name):
    self.name = name
    self.instructors = list()
    self.students = list()

  def add_instructor(self, instructor_to_add):
    if instructor_to_add not in self.instructors:
      self.instructors.append(instructor_to_add)
      instructor_to_add.teach_class(self.name)
    else:
      print('Instructor already teaching class')

  def add_student(self, student_to_add):
    if student_to_add not in self.students:
      self.students.append(student_to_add)
      student_to_add.go_to_cohort(self.name)
    else:
      print('Student alredy enrolled')