student_name = "sonia" 
student_major = "CSCI"

if student_major == "BIOL":
    major = "Bilogy"
    location = "Science Bldg, Room 310"
elif student_major == "CSCI":
    major = "computer science"
    location = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major = "English"
    location = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major = "History"
    location = "Kerr Hall, Room 114"
elif student_major == "MKT":
    major = "Marketing"
    location = "Westly Hall, Room 310"
else:
    major = "<unknown>"
    location = ""

print("Student:", student_name)
print("Major:", major)
print("Office:", location)