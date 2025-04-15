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


while len(unmatched) > 0:
    
    for student in unmatched:
        
        preference = students[student][0]
        
        # matches[preference] = student
        
        if preference not in matches.keys():
            
            matches[preference] = student
            students[student].pop(0)

        else:
            
            current_student_match = matches[preference]
            preference_list = internships[preference]

            if preference_list.index(student) < preference_list.index(current_student_match):
                matches[preference] = student
                unmatched.append(current_student_match)
            else:
                unmatched.append(student)

            students[student].pop(0)

        unmatched.remove(student)


print(matches)

# step one: select the first preference of the first student
# 2:    check if already in the final matches
# 3:    if yes, see if the index is 'lower' than the existing match (find the index of set in dict)
#            if yes, update the match
#            if no, don,t change the match
#                repeat the process for the next preference
#       if no, add the matches to the final matches

# either go over all preference for a person, or per person over preferences
# and then it would all go in a loop set to the amount of of preferences there are