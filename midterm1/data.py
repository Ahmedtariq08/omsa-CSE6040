poker_info = {
    "RANKS": {
        "2": 0,
        "3": 1,
        "4": 2,
        "5": 3,
        "6": 4,
        "7": 5,
        "8": 6,
        "9": 7,
        "T": 8,
        "J": 9,
        "Q": 10,
        "K": 11,
        "A": 12
    },
    "SUITS": {
        "H": {
            "index": 0,
            "symbol": "â™¥",
            "start_pos": 0,
            "end_pos": 13,
            "full_block": 8191
        },
        "D": {
            "index": 3,
            "symbol": "â™¦",
            "start_pos": 39,
            "end_pos": 52,
            "full_block": 4503049871556608
        },
        "C": {
            "index": 2,
            "symbol": "â™£",
            "start_pos": 26,
            "end_pos": 39,
            "full_block": 549688705024
        },
        "S": {
            "index": 1,
            "symbol": "â™ ",
            "start_pos": 13,
            "end_pos": 26,
            "full_block": 67100672
        }
    },
    "CARDS": {
        "2H": 1,
        "3H": 2,
        "4H": 4,
        "5H": 8,
        "6H": 16,
        "7H": 32,
        "8H": 64,
        "9H": 128,
        "TH": 256,
        "JH": 512,
        "QH": 1024,
        "KH": 2048,
        "AH": 4096,
        "2S": 8192,
        "3S": 16384,
        "4S": 32768,
        "5S": 65536,
        "6S": 131072,
        "7S": 262144,
        "8S": 524288,
        "9S": 1048576,
        "TS": 2097152,
        "JS": 4194304,
        "QS": 8388608,
        "KS": 16777216,
        "AS": 33554432,
        "2C": 67108864,
        "3C": 134217728,
        "4C": 268435456,
        "5C": 536870912,
        "6C": 1073741824,
        "7C": 2147483648,
        "8C": 4294967296,
        "9C": 8589934592,
        "TC": 17179869184,
        "JC": 34359738368,
        "QC": 68719476736,
        "KC": 137438953472,
        "AC": 274877906944,
        "2D": 549755813888,
        "3D": 1099511627776,
        "4D": 2199023255552,
        "5D": 4398046511104,
        "6D": 8796093022208,
        "7D": 17592186044416,
        "8D": 35184372088832,
        "9D": 70368744177664,
        "TD": 140737488355328,
        "JD": 281474976710656,
        "QD": 562949953421312,
        "KD": 1125899906842624,
        "AD": 2251799813685248
    },
    "HAND_TYPES": {
        "STRAIGHT_FLUSH": 9,
        "FOUR_OF_A_KIND": 8,
        "FULL_HOUSE": 7,
        "FLUSH": 6,
        "STRAIGHT": 5,
        "THREE_OF_A_KIND": 4,
        "TWO_PAIR": 3,
        "PAIR": 2,
        "HIGH_CARD": 1
    },
    "FIVE_HIGH": 4111
}


def cards_info(cards: int) -> dict:
    return {
        'int_value': cards,
        'binary_representation': f'0b{cards:052b}',
        'string_representation': ' '.join(k for k, v in poker_info['CARDS'].items() if cards & v),
        'suit_groups': {suit_str: (cards & suit_info['full_block']) >> suit_info['start_pos'] for suit_str, suit_info in
                        poker_info['SUITS'].items()}
    }


def pprint_cards(cards: int) -> None:
    pretty_binary = f'''SUIT: DDDDDDDDDDDDD CCCCCCCCCCCCC SSSSSSSSSSSSS HHHHHHHHHHHHH
RANK: AKQJT98765432 AKQJT98765432 AKQJT98765432 AKQJT98765432
BITS: {(cards >> 39) & 0b1111111111111:013b} {(cards >> 26) & 0b1111111111111:013b} {(cards >> 13) & 0b1111111111111:013b} {(cards) & 0b1111111111111:013b}'''
    print(pretty_binary)


def ranks_info(ranks: int) -> dict:
    return {
        'int_value': ranks,
        'binary_representation': f'0b{ranks:013b}',
        'string_representation': ' '.join(k for k, v in poker_info['RANKS'].items() if ranks & 1 << v)
    }


def pprint_ranks(ranks: int) -> None:
    pretty_binary = f'''RANK: AKQJT98765432
BITS: {ranks & 0b1111111111111:013b}'''
    print(pretty_binary)
