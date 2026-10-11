COURSE = "21241"

ROSTER_IMPORT_HEADINGS = ["Andrew ID", 
                   "Last Name", 
                   "Preferred/First Name", 
                   "College", 
                   "Department", 
                   "Major", 
                   "Section", 
                   "Email"]

WEBWORK_LST_HEADINGS = ["Andrew ID",
                        "Last Name",
                        "Preferred/First Name",
                        "C",
                        "College", 
                        "Section", 
                        "", 
                        "Email", 
                        "Andrew ID", 
                        "", 
                        "0", 
                        ""]

# GROUPS is a list of dictionaries: {gropu_name: (group_prefix, group_weight)}
GROUPS = [{"name": "Online Homework", "prefix": "WW", "weight": .05},
          {"name": "Written Homework", "prefix": "HW", "weight": .05},
          {"name": "Quizzes", "prefix": "Quiz", "weight": .10},
          {"name": "Midterm Exams", "prefix": "Exam", "weight": .55},
          {"name": "Final", "prefix": "Final", "weight": .25}
          ]

# CUTOFFS = {"Exam #1": {"A": '90', "B": '80', "C": '70', "D": '50'},
#            "Exam #2": {"A": '90', "B": '80', "C": '70', "D": '60'},
#            "Final Exam - Part 1": {"A": '90', "B": '80', "C": '70', "D": '60'},
#            "Final Exam - Part 2": {"A": '90', "B": '80', "C": '70', "D": '60'},
#            "default": {"A": '90', "B": '80', "C": '70', "D": '60'}
#            }

CUTOFFS = {"Exam #1": {"A": '80', "B": '65', "C": '50', "D": '30'},
           "default": {"A": '90', "B": '80', "C": '70', "D": '60'}
           }