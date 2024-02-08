import re

# REGEX NOTES

# Sample text
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )

coreyms.com

321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

# Matchers
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary (whitespace or nonalphanumeric that separates a word
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)


#### Sample Regex's ####
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+


# Use r before a string to classify it as raw string.
# python will not handle backslashes, new line characters and will treat the string literally
# print(r'\tTab')

# pattern matching which is case and order sensitive
# all the characters that need to be escaped must reseed with backslash

# Different patterns 'abc' string escape special characters '\.' url coreyms\.com [] anything

## SECTION Single character matching with ranges
# withing brackets is the character set to match, matches only one character dash within a
# character set specifies a range such as [1-5] [a-zA-Z] will match all lower and upper case
# letters ^ within a set will negate the set specifiers. [^a-zA-Z] will match everything that is
# not lower or upper case letters
# '[^b]at' will match cat and mat but not bat

## SECTION Quantifiers to match more than one characters at once
# Refer to quantifiers notes above

# matching hone numbers
pattern = re.compile(
    r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')  # matches all numbers with dash and zero as searator

pattern2 = re.compile(
    r'[89]00[-.]\d\d\d[-.]\d\d\d\d')  # matches all numbers that start with 800 or 900

pattern3 = re.compile(
    r'\d{3}[-.]\d{3}[-.]\d{4}')  # uses number to specify how many laces we want to match

# matching mr and mrs
pattern4 = re.compile(
    r'M(r|s|rs)\.?\s[A-Z]\w*')  # ? says that '.' is optional, \s is for space, [A-Z]
# means we want capital letter after space, \w* means that we need to sto before next word break

# matching emails
pattern5 = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

matches = pattern4.finditer(text_to_search)
for match in matches:
    print(match)
