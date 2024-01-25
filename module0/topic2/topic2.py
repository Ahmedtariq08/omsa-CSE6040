# === ASSOCIATION RULE MINING ===
import itertools
from collections import defaultdict


# SECTION NOTEBOOK 2
def normalize_string(s):
    assert type(s) is str
    return "".join([c.lower() for c in s if c.isalpha() or c.isspace()])


def get_normalized_words(s):
    assert type(s) is str
    normalizedText = normalize_string(s)
    return normalizedText.split()


def make_itemsets(words):
    return [set(word) for word in words]


def update_pair_counts(pair_counts, itemset):
    assert type(pair_counts) is defaultdict
    for com in list(itertools.permutations(itemset, 2)):
        pair_counts[com] += 1


def update_item_counts(item_counts, itemset):
    for c in itemset:
        item_counts[c] += 1


def filter_rules_by_conf(pair_counts, item_counts, threshold):
    test = {}  # (item_a, item_b) -> conf (item_a => item_b)
    for (key, value) in pair_counts.items():
        t = value / item_counts[key[0]]
        if t >= threshold:
            test[key] = t

    return test


def find_assoc_rules(receipts, threshold):
    pairCounts = defaultdict(int)
    itemCounts = defaultdict(int)
    for set in receipts:
        for com in list(itertools.permutations(set, 2)):
            pairCounts[com] += 1
        for c in set:
            itemCounts[c] += 1

    return filter_rules_by_conf(pairCounts, itemCounts, threshold)


def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    return set(d1.keys()).intersection(d2.keys())


# SECTION ACTUAL ASSOCIATION MINING
def on_vocareum():
    import os
    return os.path.exists('.voc')


def download(file, local_dir="", url_base=None, checksum=None):
    import os, requests, hashlib, io
    local_file = "{}{}".format(local_dir, file)
    if not os.path.exists(local_file):
        if url_base is None:
            url_base = "https://cse6040.gatech.edu/datasets/"
        url = "{}{}".format(url_base, file)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(local_file, 'wb') as f:
            f.write(r.content)
    if checksum is not None:
        with io.open(local_file, 'rb') as f:
            body = f.read()
            body_checksum = hashlib.md5(body).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(
                    local_file,
                    body_checksum,
                    checksum)
    print("'{}' is ready!".format(file))


if on_vocareum():
    DATA_PATH = "./resource/asnlib/publicdata/"
else:
    DATA_PATH = "/home/gosaas/PycharmProjects/pythonProject/module0/topic2/"
datasets = {'groceries.csv': '0a3d21c692be5c8ce55c93e59543dcbe'}

# for filename, checksum in datasets.items():
#     download(filename, local_dir=DATA_PATH, checksum=checksum)

with open('{}{}'.format(DATA_PATH, 'groceries.csv')) as fp:
    groceries_file = fp.read()

# print(groceries_file[0:100])
# print("\n(All data appears to be ready.)")

THRESHOLD = 0.5
MIN_COUNT = 10


def get_basket_rules():
    itemSets = [set(row.split(",")) for row in groceries_file.split("\n")]
    pairCounts = defaultdict(int)
    itemCounts = defaultdict(int)
    for itemSet in itemSets:
        for com in list(itertools.permutations(itemSet, 2)):
            pairCounts[com] += 1
        for item in itemSet:
            itemCounts[item] += 1

    rules = {}
    for (key, value) in pairCounts.items():
        count = itemCounts[key[0]]
        t = value / count
        if t >= THRESHOLD and count >= MIN_COUNT:
            rules[key] = t

    return rules


basket_rules = get_basket_rules()
