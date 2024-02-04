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
    digit_map = {str(i): i for i in range(10)}
    for i, char in enumerate('abcdefghijklmnopqrstuvwxyz', start=10):
        digit_map[char] = i

    integer_part, _, fractional_part = s.partition('.')

    int_value = 0
    for digit in integer_part:
        digitToFind = digit.lower() if digit.isalpha() else digit
        if digitToFind not in digit_map or digit_map[digitToFind] >= base:
            raise ValueError("Invalid digit in integer part")
        int_value = int_value * base + digit_map[digitToFind]

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
    return signedVal


# eval_fp('-', '1.25000', -1, base=10)  # 0.125
# eval_fp('+', '1.20100202211020211211', 4, 3)  # 138.25708894296503
# eval_fp('+', '1.10101110101100100101001111000101', -5, 2)  # 0.05257526742207119
# eval_fp('-', '2.G0EBPT', -1, 32)  # -0.0781387033930514
# eval_fp('-', '2.5M2M01E', 4, 23)  # -632223.0030410126
# eval_fp('-', 'C.DF02BC3', -2, 16)  # -0.0502778729860438


### Exercise
def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    # You may assume normalized inputs at the given precision, `signif_bits`.
    assert u_signif[:2] in {'1.', '0.'} and len(u_signif) == (signif_bits + 1)
    assert v_signif[:2] in {'1.', '0.'} and len(v_signif) == (signif_bits + 1)
    f1 = eval_fp(u[0], u[1], u[2], 2)
    f2 = eval_fp(v[0], v[1], v[2], 2)
    s = f1 + f2
    bs = fp_bin(s)
    nbs = (bs[0], bs[1][:signif_bits + 1], bs[2])
    return nbs


# These calls to `add_fp_bin` will raise an Assertion error if your solution does not
# return the expected result.

# u = ('+', '1.010010', 0)
# v = ('-', '1.000000', -2)
# add_fp_bin(u, v, 7)
# assert add_fp_bin(u, v, 7) == ('+', '1.000010', 0)


# SECTION PART ONE
def alg_sum(x):
    s = 0.
    for x_i in x:
        s += x_i
    return s


# Exercise 0
N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
t = [0.0] * len(N)
for i in range(len(N)):
    x = [.1 * N[i]]
    sums = alg_sum(x)
    t[i] = sums


def alg_sum_accurate(nums):
    assert type(nums) is list
    partials = []  # sorted, non-overlapping partial sums
    for x in nums:
        i = 0
        for y in partials:
            if abs(x) < abs(y):
                x, y = y, x
            hi = x + y
            lo = y - (hi - x)
            if lo:
                partials[i] = lo
                i += 1
            x = hi
        partials[i:] = [x]
    return sum(partials, 0.0)
