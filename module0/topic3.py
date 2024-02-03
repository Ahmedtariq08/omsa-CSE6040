# === SECTION MATHEMATICAL EXERCISES ===
from math import comb


# Probability that sum of two die is even
def odd_one_out():
    return len([x + j for x in range(1, 7) for j in range(1, 7) if (x + j) % 2 == 0]) / 36


print(4 * comb(13, 3))

# SECTION - ANSWERS

# Exercise 0 -> 0.5
# Exercise 1a -> 2598960
