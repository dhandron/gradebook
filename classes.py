
class Student:
    def __init__(self, 
                 andrew_id:str, 
                 first:str, 
                 last:str,
                 college:str,
                 department:str,
                 major:str,
                 section:str,
                 email:str) -> None:
        self.andrew_id = andrew_id
        self.first = first
        self.last = last
        self.college = college
        self.department = department
        self.major = major
        self.section = section
        self.email = email
        self.comment = college + " " + department + " " + major
        self.webwork = None
        self.canvas = None

class AssignmentGroup:
    def __init__(self, weight, average, assignments):
        self.weight = weight
        self.average = average
        self.assignments = assignments

class Course:
    def __init__(self, number, name, semester):
        self.number = number
        self.name = name
        self.semester = semester
        self.roster = None
        self.final = None
        self.midterms = None
        self.quizzes = None
        self.written_hw = None
        self.online_hw = None


