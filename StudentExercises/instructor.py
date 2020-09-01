class Instructor:
  def __init__(self, firstName, lastName, slackHandle, specialty):
    self.firstName = firstName
    self.lastName = lastName
    self.slackHandle = slackHandle
    self.specialty = specialty

  def assign_exercise(self, exercise_to_assign, student_to_assign):
    student_to_assign.add_exercise(exercise_to_assign)

  def teach_class(self, cohort_to_teach):
    self.cohort = cohort_to_teach
