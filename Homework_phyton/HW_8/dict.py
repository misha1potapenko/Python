
with open("subjects.csv", "r", encoding="UTF-8") as f:
    subject_dict = dict.fromkeys(f.readlines())
    print(subject_dict)
subject_dict['Геометрия\n'] = [3, 4, 5]
subject_dict["Алгебра\n"] = [4, 3, 2]

print(subject_dict)
