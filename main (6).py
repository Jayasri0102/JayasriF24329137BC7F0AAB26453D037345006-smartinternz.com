class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):

  sorted_student = sorted(student_list, key=lambda student: student.cgpa, reverse=True)
  return sorted_student


student = [Student("jaya","A123",7.8), Student ("Saranya","A124",8.9),Student("Sindhu","A125",9.1),Student("gowri","A126",9.9),]

sorted_student= sort_students(student)

for student in sorted_student:
  print ("Name: {}, CGPA: {}".format(student.name,student.roll_number, student.cgpa))