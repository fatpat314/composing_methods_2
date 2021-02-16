# By Kamran Bigdely Nov. 2020
# Replace temp variable with query
# TODO: Use 'extract method' refactoring technique to improve this code. If required, use
#       'replace temp variable with query' technique to make it easier to extract methods.
class Employer:    
    def __init__(self, name):
        self.name = name
    def send(self, students):
        print("Students' contact info were sent to", self.name + '.')

class Student:
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name
    def get_gpa(self):
        return self.gpa
    def send_congrat_email(self):
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    def __init__(self, students) -> None:
        self.students = students

    def process_graduation(self):
        self.get_grad_list()
        self.print_student_name_who_graduated()
        self.send_congrat_emails()
        self.find_the_top()

    def get_grad_list(self):
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for s in self.students:
            if s.get_gpa() > min_gpa:
                passed_students.append(s)
        return passed_students

    def print_student_name_who_graduated(self):
        print('*** Student who graduated *** ')
        for s in self.get_grad_list():
            print(s.name)
        print('****************************')

    def send_congrat_emails(self):
        for s in self.get_grad_list():
            s.send_congrat_email()

    def find_the_top(self):
        self.get_grad_list().sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(self.get_grad_list()))
        top_10_percent = self.get_grad_list()[index:]
        top_employers = [Employer('Microsoft'), Employer('Free Software Foundation'), Employer('Google')]
        for e in top_employers:
            e.send(top_10_percent)

students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'), 
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(students)
school.process_graduation()
"""
I don't remember being taught "memoization"
Looks like something that would be good to go over.
"""

