# === SECTION FLOATING POINT - NOTEBOOK 4 ===

### Exercise 0
def eval_strint(s, base=2):
    assert type(s) is str
    assert 2 <= base <= 36
    # My own algorithm for strings with digits only
    # return sum([int(s[i]) * base ** (len(s) - i - 1) for i in range(len(s))])

    return int(s, base)


# print(f"eval_strint('6040', 8) -> {eval_strint('6040', 8)}")
# print(f"eval_strint('deadbeef', 16) -> {eval_strint('deadbeef', 16)}")
# print(f"eval_strint('4321', 5) -> {eval_strint('4321', 5)}")


### Exercise 1
def eval_strfrac(s, base=2):
    # My own algorithm
    arr = s.split(".")
    intFloat = float(eval_strint(arr[0], base))

    decFloat = 0.0
    if len(arr) > 1:
        decimals = arr[1]
        decFloat = float(sum([int(decimals[i]) * base ** (-1 - i) for i in range(len(decimals))]))

    return intFloat + decFloat


def eval_strfracgt(s, base=2):
    digit_map = {str(i): i for i in range(10)}
    for i, char in enumerate('abcdefghijklmnopqrstuvwxyz', start=10):
        digit_map[char] = i

    integer_part, _, fractional_part = s.partition('.')

    int_value = 0
    for digit in integer_part:
        if digit not in digit_map or digit_map[digit] >= base:
            raise ValueError("Invalid digit in integer part")
        int_value = int_value * base + digit_map[digit]

    dec_value = 0
    if fractional_part:
        for i, digit in enumerate(fractional_part):
            if digit not in digit_map or digit_map[digit] >= base:
                raise ValueError("Invalid digit in fractional part")
            dec_value += digit_map[digit] * base ** -(i + 1)

    return float(int_value + dec_value)


# Test the function
print(eval_strfracgt('3.14', base=10))  # Output should be approximately 3.14
print(eval_strfracgt('100.101', base=2))  # Output should be 4.625
print(eval_strfracgt('2c', base=16))  # Output should be 44.0
