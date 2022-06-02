# from Classes.student import Student
# from Classes.staff import Staff
from Classes.student import Student
from Classes.staff import Staff


class School:
      def __init__(self, name):
        self.name = name
        self.staff = Staff.all_staff()
        self.students = Student.all_students()




    

