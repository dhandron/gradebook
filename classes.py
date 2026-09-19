
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
        self.grades: list[AssignmentGroup] = []
        self.average: float

    def compute_cumulative_average(self):
        total = 0
        for group in self.grades:
            group.compute_average()
            total += group.average * group.weight
        self.average = total


class AssignmentGroup:
    def __init__(self, name, weight):
        self.name:str = name
        self.weight: float = weight
        self.average: float = -1
        self.grades: dict[str:tuple[float]] = {}

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
                print(f"no grade recorded for {assignment}")
            # print(total)
        # print(count)
        if count > 0:
            self.average = total / max_points
        else: 
            self.average = ''


class CourseAssignmentGroup(AssignmentGroup):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.stats: dict[str: float]
        self.cutoffs: dict[str: float]

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

