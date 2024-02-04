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
# def eval_strfrac(s, base=2):
#     # My own algorithm
#     arr = s.split(".")
#     intFloat = float(eval_strint(arr[0], base))
#
#     decFloat = 0.0
#     if len(arr) > 1:
#         decimals = arr[1]
#         decFloat = float(sum([int(decimals[i]) * base ** (-1 - i) for i in range(len(decimals))]))
#
#     return intFloat + decFloat


def eval_strfrac(s, base=2):
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
            digitToFind = digit.lower() if digit.isalpha() else digit
            if digitToFind not in digit_map or digit_map[digitToFind] >= base:
                raise ValueError("Invalid digit in fractional part")
            dec_value += digit_map[digitToFind] * base ** -(i + 1)

    return float(int_value + dec_value)


# Test the function
# print(eval_strfracgt('3.14', base=10))  # Output should be approximately 3.14
# print(eval_strfracgt('100.101', base=2))  # Output should be 4.625
# print(eval_strfracgt('2c', base=16))  # Output should be 44.0


### Exercise 2
def fp_bin(v):
    assert type(v) is float
    hex = v.hex()
    s_sign = '+' if hex[0] == '0' else '-'
    exp = int(hex[hex.index('p') + 1:])

    significand = hex[hex.index('x') + 1: hex.index('p')]
    binary = bin(int(significand.split(".")[1], 16))
    binary = binary.replace("0b", "")
    binary = "0" * (52 - len(binary)) + binary

    formattedBin = significand[0] + "." + binary
    result = (s_sign, formattedBin, exp)
    print(result)
    return result


# v1 = 1280.03125
# fp_bin(v1)
# v2 = 4.2889079630755524e-119
# fp_bin(v2)
# v3 = 0.0
# fp_bin(v3)


def eval_fp(sign, significand, exponent, base=2):
    assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    assert type(exponent) is int
    val = eval_strfrac(significand, base) * base ** exponent
    signedVal = val if sign == '+' else -1 * val
    print(signedVal)
    return signedVal

# eval_fp('-', '1.25000', -1, base=10)  # 0.125
# eval_fp('+', '1.20100202211020211211', 4, 3)  # 138.25708894296503
# eval_fp('+', '1.10101110101100100101001111000101', -5, 2)  # 0.05257526742207119
# eval_fp('-', '2.G0EBPT', -1, 32)  # -0.0781387033930514
# eval_fp('-', '2.5M2M01E', 4, 23)  # -632223.0030410126
