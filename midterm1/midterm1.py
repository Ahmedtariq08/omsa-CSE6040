from data import poker_info, cards_info, ranks_info

# PART - EXERCISE 1 (1 points)
demo_s_ex_0 = 'ah TH jd qs 9D'

def hand_from_str(s: str) -> int:
    return sum([poker_info['CARDS'][c.upper().strip()] for c in s.split()])


# PART - EXERCISE 2 (2 Points)
demo_d_ex2 = {'x': 1, 'y': 2, 'kangaroo': 'llama'}
demo_d_invalid_ex2 = {'x': 1, 'y': 2, 'kangaroo': 2}

def reverse_dict(d: dict) -> dict:
    result = {}
    for (key, value) in d.items():
        if value not in result:
            result[value] = key
        else:
            raise ValueError("Key already present.")
    return result


# PART - EXERCISE 3 (1 Points)
demo_n_ex3 = 0b11110010101  # equivalent to `demo_n_ex3 = 1941`

def count_bits(n: int) -> int:
    return bin(n).count("1")


# PART - EXERCISE 4 (3 Points)
demo_hands_ex4 = [34084860461056,
                  2252899459547138,
                  3378112070942720,
                  595935302254592,
                  131958575202304,
                  598684148441088,
                  1144044063293440,
                  80815178383360,
                  723616090030080]


### Exercise 4 solution
def get_reductions(hand: int) -> tuple:
    ### Predefined values in starter code

    # W, X, Y, and Z are the four suit groups from the hand
    W, X, Y, Z = [val for val in cards_info(hand)['suit_groups'].values()]
    in_arbitrary_pair = (W & X) | (Y & Z)

    # We are also providing flush and hand_ranks as examples
    flush = (count_bits(W) == 5) | (count_bits(X) == 5) | (count_bits(Y) == 5) | (count_bits(Z) == 5)
    hand_ranks = W | X | Y | Z

    quads = W & X & Y & Z
    odd_ranks = W ^ X ^ Y ^ Z
    trips = odd_ranks & in_arbitrary_pair
    five_high = hand_ranks == poker_info['FIVE_HIGH']
    straight = five_high or count_bits(hand_ranks & (hand_ranks >> 1)) == 4
    rank_count = count_bits(hand_ranks)

    return flush, hand_ranks, quads, odd_ranks, trips, five_high, straight, rank_count


### demo function call
# for hand in demo_hands_ex4:
#     print(f'get_reductions({hand}) -> {get_reductions(hand)}')


# PART - EXERCISE 5 (3 points) ***[NOT ATTEMPTED]***
def identify_from_reductions(flush: bool,
                             hand_ranks: int,
                             quads: int,
                             odd_ranks: int,
                             trips: int,
                             five_high: bool,
                             straight: bool,
                             rank_count: int) -> tuple:
    [type, primaryRanks, secondaryRanks] = [None, None, None]

    print(ranks_info(quads))

    # if rank_count == 2:
    return ()


# demo_reductions_ex5 = [get_reductions(x) for x in demo_hands_ex4]
# for reduction in demo_reductions_ex5:
#     print(identify_from_reductions(*reduction), '\n')

# PART - EXERCISE 6 (2 points)
def score_from_info(hand_type: str, primary: int, secondary: int) -> int:
    bin_hand = bin(poker_info['HAND_TYPES'][hand_type])[2:].zfill(4)
    bin_primary = bin(primary)[2:].zfill(13)
    bin_secondary = bin(secondary)[2:].zfill(13)
    return int((bin_hand + bin_primary + bin_secondary), 2)


# PART - EXERCISE 7 (2 points)
def partition_score(score: int) -> tuple:
    '''Partitions a poker hand score into its type strength, primary ranks, and secondary ranks components
    '''
    FOUR_BITS = 0b1111
    THIRTEEN_BITS = 0b1111111111111

    type_score = FOUR_BITS & score >> 26  # shift right by 26 and keep first 4 bits
    primary_ranks = THIRTEEN_BITS & score >> 13  # shift right by 13 and keep first 13 bits
    secondary_ranks = THIRTEEN_BITS & score  # keep first 13 bits
    return type_score, primary_ranks, secondary_ranks


def translate_score(score: int) -> dict:
    type_score, primary_ranks, secondary_ranks = partition_score(score)

    type_value = None
    primary_set = set()
    secondary_set = set()
    for key, value in poker_info['HAND_TYPES'].items():
        if value == type_score:
            type_value = key

    if primary_ranks != 0:
        str_ranks = ranks_info(primary_ranks)['string_representation'].split()
        primary_set = {c for c in str_ranks}

    if secondary_ranks != 0:
        str_ranks = ranks_info(secondary_ranks)['string_representation'].split()
        secondary_set = {c for c in str_ranks}

    return {'hand_type': type_value, 'primary': primary_set, 'secondary': secondary_set}

