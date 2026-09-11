
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
    def __init__(self, name, weight):
        self.name:str = name
        self.weight: float = weight
        self.average: float
        self.assignments = dict[str:float]

    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

class CourseAssignmentGroup(AssignmentGroup):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.stats: dict[str: float]

class Course:
    def __init__(self, number, name, semester):
        self.number = number
        self.name = name
        self.semester = semester
        self.roster = None
        self.final: CourseAssignmentGroup
        self.midterms: CourseAssignmentGroup
        self.quizzes: CourseAssignmentGroup
        self.written_hw: CourseAssignmentGroup
        self.online_hw: CourseAssignmentGroup
        self.cutoffs: dict[str: float]

