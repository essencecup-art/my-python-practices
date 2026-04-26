class Student:
    def __init__(self,name,grade_list):
        self.name = name
        self.grade_list = grade_list
    def add_grade(self,grade):
        self.grade_list.append(grade)
    def avg_score(self):
        try:
            avg = sum(self.grade_list) / len(self.grade_list)
        except ZeroDivisionError:
            avg = 0
            print("cannot find average of student with no score and and negative score")
        return avg
    def find_highest(self):
        return max(self.grade_list)
    def find_lowest(self):
        return min(self.grade_list)
    def pass_or_fail(self):
        if self.avg_score() >= 50:
            return "pass"
        else:
            return "fail"

class ClassRoom:
    def __init__(self,class_name):
        self.name = class_name
        self.students = []
    def add_student(self,student):
        self.students.append(student)
        return self.students
    def show_top(self):
        if not self.students:
            return "No student in this class"
        top_student = self.students[0]
        for student in self.students:
            if student.avg_score() > top_student.avg_score():
                top_student = student
            return f"Top Performer: {top_student.name} with an average of {top_student.avg_score()}"
