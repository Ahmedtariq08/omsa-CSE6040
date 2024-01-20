import statistics
from itertools import accumulate


def cumulative_sum(lst):
    prevSum = 0
    output = []
    for n in lst:
        output.append(n + prevSum)
        prevSum += n

    return output
    # return [sum(lst[:i + 1]) for i in range(len(lst))] - ChatGPT


# print(cumulative_sum([1,2,3,4,5]))


# SECTION === NOTEBOOK1 ===
def report_exam_avg(a, b, c):
    avg = (a + b + c) / 3
    return 'Your average score: {}'.format(round(avg, 1))


# print(report_exam_avg(100, 95, 80))

def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    return [len(x) for x in s.split(" ") if len(x) != 0]


# print(count_word_lengths('the quick  brown   fox jumped over     the lazy  dog'))

def minmax(L):
    assert hasattr(L, "__iter__")
    return min(L), max(L)


# print(minmax([8, 7, 2, 5, 1]))

def compress_vector(x):
    assert type(x) is list
    d = {'inds': [], 'vals': []}
    for index, value in enumerate(x):
        if value != 0:
            d['inds'].append(index)
            d['vals'].append(value)

    dict = {'inds': [j for j in range(len(x)) if x[j] != 0], 'vals': [i for i in x if i != 0]}
    return dict


x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]

print(compress_vector(x))


def decompress_vector(d, n=None):
    # Checks the input
    assert type(
        d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"

    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    if n is None:
        n = i_max + 1
    else:
        assert n > i_max, "Bad value for full vector length"

    output = []
    for i in range(n):
        indices = [index for index, value in enumerate(d['inds']) if value == i]
        values = [d['vals'][ind] for ind in indices]
        output.append(float(sum(values)))

    return output


d = {'inds': [0, 3, 7, 3, 3, 5, 1], 'vals': [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]}


# print(decompress_vector(d, None))


def find_common_inds(d1, d2):
    assert type(d1) is dict and 'inds' in d1 and 'vals' in d1
    assert type(d2) is dict and 'inds' in d2 and 'vals' in d2
    return list(set(d1['inds']).intersection(d2['inds']))


d1 = {'inds': [9, 9, 1, 9, 8, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
d2 = {'inds': [0, 9, 9, 1, 3, 3, 9],
      'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}

# print(find_common_inds(d1, d2))

# SECTION - PART2
grades = [['Student', 'Exam 1', 'Exam 2', 'Exam 3', 'Exam 4', 'Exam 5', 'Exam 6'],
          ['Gregar Typho', '96', '76', '77', '86', '101', '82'],
          ['Luminara Unduli', '68', '61', '81', '73', '69', '92'],
          ['Cliegg Lars', '82', '69', '84', '86', '100', '77'],
          ['Ackbar', '95', '78', '88', '101', '92', '59'],
          ['Yoda', '101', '81', '94', '62', '83', '101'],
          ['Jek Tono Porkins', '88', '101', '85', '60', '71', '94'],
          ['R5-D4', '78', '62', '90', '74', '67', '101'],
          ['Raymus Antilles', '66', '67', '57', '57', '93', '96'],
          ['Dexter Jettster', '75', '57', '53', '98', '63', '71']]


def get_students(grades):
    # return [str[0] for str in grades[1:]]
    return grades


def get_assignments(grades):
    return grades[0][1:]


def build_grade_lists(grades):
    return {row[0]: [int(x) for x in row[1:]] for row in grades[1:]}


def build_grade_dicts(grades):
    return {
        studentRow[0]: {header: int(studentRow[index + 1]) for index, header in
                        enumerate(grades[0][1:])}
        for studentRow in grades[1:]}


def build_avg_by_student(grades):
    return {row[0]: statistics.mean([int(x) for x in row[1:]]) for row in grades[1:]}


def build_grade_by_asn(grades):
    return {
        header: [int(val) for row in grades[1:] for i, val in enumerate(row[1:]) if i == index]
        for index, header in enumerate(grades[0][1:])
    }


def build_avg_by_asn(grades):
    return {
        header: statistics.mean(
            [int(val) for row in grades[1:] for i, val in enumerate(row[1:]) if i == index])
        for index, header in enumerate(grades[0][1:])
    }


def get_ranked_students(grades):
    studentAvgDict = {row[0]: statistics.mean([int(x) for x in row[1:]]) for row in grades[1:]}
    return list(dict(sorted(studentAvgDict.items(), key=lambda x: x[1], reverse=True)).keys())


# print(get_ranked_students(grades))


# SECTION === TOPIC 1 ===

def maxStockProfit(prices):
    minPrices = list(accumulate(prices, func=min))
    return max([sell - bestBuy for sell, bestBuy in zip(prices, minPrices)])


testArray = [13, 11, 10, 8, 5, 9, 6, 7, 7, 10, 4, 3]
# print(maxStockProfit(testArray))

# SECTION === MORE EXERCISES ===

A = [2, 16, 26, 32, 52, 71, 80, 88]


def ordered_contains(S, x):
    firstNum = S[0]
    lastNum = S[-1]
    if x < firstNum or x > lastNum:
        return False

    if (abs(lastNum - x) > abs(x - firstNum)):
        return x in S
    else:
        return x in S[::-1]
