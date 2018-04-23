students = {
    'Popov': ["A", "B", "A-"],
    'Yesmukhanov': ["B-", "D", "C-"],
    'Shamoi': ["A", "A", "A"],
    'Akshabaev': ["B", "B", "B"]
}

for name, l in students.items():
    GPA = 0
    for grade in l:
        if grade == "A":
            GPA = GPA + 4
        elif grade == "A-":
            #continue your code

    GPA = GPA / len(l)
    if GRA > 3:
        print(name)