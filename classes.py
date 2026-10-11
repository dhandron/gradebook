from constants import COURSE

class AssignmentGroup:
    def __init__(self, name, weight):
        self.name:str = name
        self.weight: float = weight
        self.average: float = -1
        self.grades: dict[str:str] = {} # {assignment: grade}

    def add_grade(self, assignment_name, grade):
        self.assignments[assignment_name] = grade

    def compute_average(self):
        total = 0
        max_points = 0
        count = 0
        for assignment in self.grades:
            # print(f"self.grades[{assignment}] is {self.grades[assignment]}")
            try:                 
                total = total + float(self.grades[assignment][0]) 
                max_points = max_points + float(self.grades[assignment][1])
                count += 1
            except Exception as e:
                pass
                #print(f"no grade recorded for {assignment}")
        if count > 0:
            self.average = total / max_points
        else: 
            self.average = ''


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
        self.course = COURSE

        self.canvas_name: str
        self.canvas_id: str
        self.sisuserid:str
        self.sisloginid:str
        self.rootaccount: str
        self.canvas_section = "foo"

        self.grades: list[AssignmentGroup] = []
        self.average: float
        self.letter_grade: str
        self.webwork: AssignmentGroup

    def compute_cumulative_average(self):
        total_score = 0
        total_weight = 0
        for group in self.grades:
            group.compute_average()
            if isinstance(group.average, float):
                total_score += group.average * group.weight
                total_weight += group.weight
        self.average = total_score / total_weight



class CutoffData(AssignmentGroup):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.cutoffs: list[AssignmentGroup] = []



