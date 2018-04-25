students = {
    'Popov': ["A", "B", "A-"],
    'Yesmukhanov': ["B", "F", "C"],
    'Shamoi': ["A", "A", "A"],
    'Akshabaev': ["B", "B", "B"],
    'Li': ["A", "A", "A", "A", "A", "A", "F"],
}

for name, l in students.items():
    GPA = 0
    for grade in l:
        if grade == "A":
            GPA = GPA + 4
        elif grade == "A-":
            #continue your code