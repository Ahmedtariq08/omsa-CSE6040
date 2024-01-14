
def cumulative_sum(lst):
    prevSum = 0
    output = []
    for n in lst:
        output.append(n + prevSum)
        prevSum += n

    return output
    # return [sum(lst[:i + 1]) for i in range(len(lst))] - ChatGPT


print(cumulative_sum([1,2,3,4,5]))