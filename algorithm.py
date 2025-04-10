students = {
    'Trillian': ['Physics', 'Sociology', 'Philosophy'],
    'Ford': ['Physics', 'Philosophy', 'Sociology'],
    'Zaphod': ['Philosophy', 'Sociology', 'Physics']
}
internships = {
    'Physics': ['Trillian', 'Ford', 'Zaphod'],
    'Sociology': ['Ford', 'Trillian', 'Zaphod'],
    'Philosophy': ['Ford', 'Trillian', 'Zaphod']
}

unmatched : list = list(students.keys())
matches : dict = dict()


# while unmatched:
for student1 in students:
    preference = students[student1][0]
    matches[preference] = student1
    students[student1].pop(0)
    if preference in matches.keys():
        student2 = matches[preference]
        # current_position = next((v for v in internships.values() if v == student), None)
        if internships[preference].index(student1) < internships[preference].index(student2):
            matches[preference] = student2
    else:
        matches[preference] = student1

print(matches)
