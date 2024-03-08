class Student:
    def __init__(self, s_name):
        self.s_name = s_name
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        print(f"{self.s_name} has enrolled in the {course} course.")

    def list_courses(self):
        print(f"{self.s_name}'s enrolled courses: {', '.join(self.courses)}")



student1 = Student("Alice")
student2 = Student("Bob")

student1.enroll("Mathematics 101")
student1.enroll("Physics 202")
student2.enroll("Mathematics 101")
student1.list_courses()
