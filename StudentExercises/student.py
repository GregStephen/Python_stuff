class Student:
  def __init__(self, firstName, lastName, slackHandle):
    self.firstName = firstName
    self.lastName = lastName
    self.slackHandle = slackHandle
    self.exercise = list()

  def __str__(self):
    return f"{self.firstName} {self.lastName}"

  def go_to_cohort(self, cohort):
    self.cohort = cohort

  def add_exercise(self, exercise_to_add):
    self.exercise.append(exercise_to_add)
