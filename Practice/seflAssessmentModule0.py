from collections import Counter

# SECTION - CONVERT SCORE TO LETTER GRADE
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


# SECTION -FIND COURSE TOTAL
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


# SECTION - BETTER UNDERSTANDING THE SYLLABUS
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


# SECTION - WHAT'S ALLOWED ON THE EXAMS
demo_exam_guidelines = {'Allowed': {'Online Resources': ['Google', 'Practice Exam Solutions'],
                                    'Physical Resources': ['Snacks'],
                                    'Technology': ['One Computer'],
                                    'Environment': ['Cats Making Noise', 'Music With Headphones'],
                                    'Misc': ['Short Breaks']},
                        'Not Allowed': {'Online Resources': ['ChatGPT', 'GitHub Copilot'],
                                        'Technology': ['Multiple Computer Screens'],
                                        'Environment': ['Talking with Friends or Family']}}

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

# print(find_guidelines(demo_exam_guidelines))


# SECTION - LOST IN TRANSLATION
translation_dict = {'cowboy': {'Howdy': 'Hi', 'partners!': 'class!', 'Ah': 'I', 'wanna': 'want to',
                               'extey-nd': 'extend', 'grand': 'very', 'ole': 'warm', 'ta': 'to', 'thuh': 'the',
                               'ya': 'you', 'programmin': 'programming', 'ave': 'have', 'all-fired': 'great',
                               'awf': 'of', 'eend': 'and', 'ahr': 'are', 'hair': 'here'},
                    'gen_z': {'fam!': 'class!', 'no': 'we are so glad', 'cap.': 'to have you.',
                              'hits': 'challenges', 'different,': 'you,', 'total': 'great', 'glow': 'time',
                              'up': 'as', 'from': 'you', 'learning': 'learn', 'periodt.': 'throughout the semester.',
                              "Don't": 'I', '@': 'might be', 'me,': 'biased,', 'slaps': 'are fantastic',
                              'W': 'succeed in'},
                    'shakespearean': {'Good': 'Greetings', 'morrow': 'new', 'class!': 'students!', 'wanteth': 'wanted',
                                      'extendeth': 'extend', 'warmeth': 'warm', 'welcometh': 'welcome',
                                      'desire': 'hope', 'thee': 'you', 'learneth': 'learn', "f'r": 'for',
                                      "has't": 'have', 'most': 'absolute', 'wondrous': 'best', 'Wondrous': 'Best',
                                      "instructeth'rs": 'instructors', 'art': 'are', "h're": 'here',
                                      'holp': 'help', 'succeedeth': 'succeed'}
                    }

distorted_str_3 = '''
Good morrow class! I wanteth to extendeth a warmeth welcometh to CSE 6040!
I desire this course helps thee learneth new programming techniques f'r data analysis.
We has't the most wondrous team of TAs and instructeth'rs who art h're to holp thee learneth and succeedeth
in the course. Wondrous of luck!'''


def translate_msg(distorted_str, msg_style, translation_dict):
    strArr = distorted_str.replace("\n", " ").split(" ")
    return " ".join([translation_dict[msg_style].get(word, word) for word in strArr])


print(translate_msg(distorted_str_3, 'shakespearean', translation_dict))

# SECTION - FAKE COURSE REVIEWS
def count_words(review):
    list_words = review.split()
    word_dictionary = Counter(word.strip() for word in list_words)
    return word_dictionary


print(count_words('This COURSE course changed MY life   it is   so  SO AMAZING amAzing'))
