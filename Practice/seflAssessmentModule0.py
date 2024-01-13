# CONVERT SCORE TO LETTER GRADE
demo_course_score = 90.6


def convert_score_to_letter(course_score):
    if course_score >= 90:
        return "A"
    elif course_score >= 80:
        return "B"
    elif course_score >= 70:
        return "C"
    elif course_score >= 60:
        return "D"
    else:
        return "F"


# print(convert_score_to_letter(demo_course_score))


# FIND COURSE TOTAL
demo_grades = {'NB0': 100, 'NB1': 87.5, 'NB2': 100, 'NB4': 75, 'NB5': 70, 'NB7': 100, 'NB9': 50, 'NB10': 100,
               'NB11': 77.5,
               'NB12': 56.25, 'NB13': 100, 'NB14': 100, 'NB15': 100, 'MT1': 75, 'MT2': 85, 'Final': 85,
               'Extra Credit': 66.667}

demo_weights = [('NB0', 2), ('NB1', 4), ('NB2', 4), ('NB4', 4), ('NB5', 4), ('NB7', 4), ('NB9', 4), ('NB10', 4),
                ('NB11', 4),
                ('NB12', 4), ('NB13', 4), ('NB14', 4), ('NB15', 4), ('MT1', 10), ('MT2', 15), ('Final', 25),
                ('Extra Credit', 3)]

def find_course_total(grades, weights):
    total = 0
    for w in weights:
        name = w[0]
        weight = w[1]
        grade = grades[name]
        total += (weight * grade) / 100

    return round(total, 2)

# print(find_course_total(demo_grades, demo_weights))



# BETTER UNDERSTANDING THE SYLLABUS
demo_syllabus_words = ['the', 'a', 'utc', 'it', 'frequently', 'piazza', 'is', 'for', 'notebook', 'vocareum']
demo_important_words = {'utc', 'autograder', 'vocareum', 'notebook', '48-hour extension', 'proctored exams', 'piazza'}

def syllabus_words_importance(syllabus_words, important_words):
    words = []
    for sylWord in syllabus_words:
        if sylWord in important_words and sylWord not in words:
            words.append(sylWord)

    words.sort()
    return words[:3]

# print(syllabus_words_importance(demo_syllabus_words, demo_important_words))


# WHAT'S ALLOWED ON THE EXAMS

def find_guidelines(exam_guidelines):
    output = {}
    for permission in exam_guidelines:
        permissionCategories = exam_guidelines[permission]
        for category in permissionCategories:
            arr = permissionCategories[category]
            newArr = list(map(lambda value: {value: permission}, arr))
            if category in output:
                output[category] = output[category] + newArr
            else:
                output[category] = newArr

    return output


print(find_guidelines(demo_exam_guidelines))
