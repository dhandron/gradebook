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
GROUPS = [{"name": "Online Homework", "prefix": "WW", "weight": .08},
          {"name": "Written Homework", "prefix": "HW", "weight": .08},
          {"name": "Midterm Exams", "prefix": "Exam", "weight": .52},
          {"name": "Final", "prefix": "Final", "weight": .32}
          ]

CUTOFFS = {"Exam #1": {"A": '90', "B": '80', "C": '70', "D": '50'},
           "Exam #2": {"A": '90', "B": '80', "C": '70', "D": '60'},
           "Final Exam - Part 1": {"A": '90', "B": '80', "C": '70', "D": '60'},
           "Final Exam - Part 2": {"A": '90', "B": '80', "C": '70', "D": '60'},
           "default": {"A": '90', "B": '80', "C": '70', "D": '60'}
           }