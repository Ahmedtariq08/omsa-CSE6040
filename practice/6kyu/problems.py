# BANKERS PROBLEM


def fortune(f0, p, c0, n, i):
    gainInterest = p / 100
    finalAmount = f0
    finalExpense = c0
    withdrawInterest = i / 100

    for year in range(n):
        finalAmount = finalAmount + (finalAmount * gainInterest) - finalExpense
        finalExpense = finalExpense + (finalExpense * withdrawInterest)

    return finalAmount > 0


result = fortune(100000, 1, 2000, 15, 1)


def sq_in_rect(lng, wdth):
    if lng == wdth:
        return None

    output = []
    ls = min(lng, wdth)
    bs = max(lng, wdth)
    while ls != bs:
        output.append(ls)
        newSide = bs - ls
        bs = max(newSide, ls)
        ls = min(newSide, ls)
        if ls == bs:
            output.append(ls)

    return output


sqArr = sq_in_rect(20, 14)


# print(sqArr)

# MULTIPLES OF 3 AND 5

def solution(number):
    if number < 0:
        return 0

    index = 0
    totalSum = 0
    while index < number:
        if index % 3 == 0 or index % 5 == 0:
            totalSum += index
        index += 1

    return totalSum


total = solution(10)


# print(total)


# BOUNCING BALLS

def bouncing_ball(h, bounce, window):
    if h > 0 > bounce and bounce > 0 and window < h:
        return -1

    seeingTotal = 1
    while h > window:
        seeingTotal += 1
        h = h * bounce

    return seeingTotal


bounceResult = bouncing_ball(30, 0.75, 1.5)


# print(bounceResult)


# SECTION - FIBONACCI
def fibonacci(num):
    if num < 2:
        return num
    else:
        return fibonacci(num - 1) + fibonacci(num - 2)


def fib(n):
    allFibs = []
    for i in range(1000):
        if i < 2:
            allFibs.append(1)
        else:
            fibSeq = allFibs[i - 1] + allFibs[i - 2]
            if fibSeq < n:
                allFibs.append(fibSeq)
            else:
                break

    return sum([x for x in allFibs if x % 2 == 0])


print(fib(2))
