# SECTION NOTEBOOK 5
import html
import re

from bs4 import BeautifulSoup

from module0.common import printJson


# Exercise 0
def is_ssn(s):
    pattern = re.compile(r'\d{3}-\d{2}-\d{4}')
    return bool(pattern.search(s))


# Exercise 1
# ValueError wrapper
def eif_wrapper(s, func):
    """
    Returns a (bool, function return) pair where the first element is True when a ValueError is raised
    and False if a Value Error is not raised. The second output is the return value from calling `func(s)`.
    """
    raised_value_error = False
    result = None
    try:
        result = func(s)
    except ValueError:
        raised_value_error = True
    finally:
        return raised_value_error, result


### Define demo inputs
demo_str_ex1_list = ['richie@cc.gatech.edu', 'what-do-you-know+not-much@gmail.com',
                     'x @hpcgarage.org', 'richie@cc.gatech.edu7', '/begged@draw.com2f',
                     'was@quiver3.comK', '_pa3ck@pairs.com', ':ro3om@putting.com',
                     '.simplet4on@right.comc']


### SECTION Exercise 1 solution
def parse_email(s):
    """Parses a string as an email address, returning an (id, domain) pair."""
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.-]+[a-zA-Z]$')
    isValidEmail = bool(pattern.search(s))
    if not isValidEmail:
        raise ValueError("Email not in correct format.")

    index = s.index("@")
    return s[:index], s[index + 1:]


### demo function call
# for demo_str_ex1 in demo_str_ex1_list:
#     print(f"eif_wrapper({demo_str_ex1}, parse_email) -> {eif_wrapper(demo_str_ex1, parse_email)}")

# SECTION Exercise 2
demo_str_ex2_list = ['(404) 121-2121', '404-121-2121']


def parse_phone1(s):
    pattern = re.compile(r'\s*\((\d{3})\)\s*(\d{3})-(\d{4})\s*')
    match = pattern.match(s)
    if not match:
        raise ValueError("Number not in correct format.")

    areaCode, firstThree, lastFour = match.groups()
    return areaCode, firstThree, lastFour


### demo function call
# for demo_str_ex2 in demo_str_ex2_list:
#     print(
#         f"eif_wrapper('{demo_str_ex2}', parse_phone1) -> {eif_wrapper(demo_str_ex2, parse_phone1)}")

# SECTION Exercise 3
### Exercise 3 solution
demo_str_ex3_list = ['404-5551212', '(404-555-1212', '(404) 555-1212', '(404) 5551212',
                     '404-555-1212', '404-5551212', '404555-1212', '4045551212', ' 606078-8556    ']


def parse_phone2(s):
    pattern = re.compile(r'\s*(\(\d{3}\)|\d{3})(\s*|-)(\d{3})(\s*|-)(\d{4})\s*')
    match = pattern.match(s)
    if not match:
        raise ValueError("Number not in correct format.")

    areaCode, h, firstThree, s, lastFour = match.groups()
    areaCode = areaCode.replace("(", "") if areaCode.startswith("(") else areaCode
    areaCode = areaCode.replace(")", "") if areaCode.endswith(")") else areaCode

    return areaCode, firstThree, lastFour


# CHAT GpT Solution
def parse_phone(s):
    pattern = re.compile(r'\s*(?:\((\d{3})\)|(\d{3}))\s*[-\s]*(\d{3})[-\s]*(\d{4})\s*')
    match = pattern.match(s)
    if not match:
        raise ValueError("Number not in correct format.")

    groups = match.groups()
    areaCode = groups[0] or groups[1]  # Use the first non-empty group as areaCode
    firstThree, lastFour = groups[2], groups[3]

    return areaCode, firstThree, lastFour


# ## demo function call for demo_str_ex3 in demo_str_ex3_list: print( f"eif_wrapper('{
# demo_str_ex3}', parse_phone2) -> {eif_wrapper(demo_str_ex3, parse_phone2)}")

# SECTION pART 1

# parsing html file:
# pick <li> with class="regular-search-result"
# pick <span> with class="indexed-biz-name", this will give ranking and name
# pick <span> with class="review-count rating-qualifier" for reviews, convert to numrevs
# pick <span> with class="business-attribute price-range" for price range $$

def parseHtml(yelp_html):
    soup = BeautifulSoup(yelp_html, "html.parser")

    result = []
    allListTags = soup.find_all('li', class_='regular-search-result')
    for tag in allListTags:
        obj = {}

        # finding the name
        anchor = tag.find_next('a', class_='biz-name js-analytics-click')
        if anchor:
            obj['name'] = html.escape(anchor.find_next("span").get_text().strip())

        # finding the stars
        div = tag.find_next('div', class_='biz-rating biz-rating-large clearfix')
        if div:
            obj['stars'] = div.find_next("img").get("alt")[:3]

        result.append(obj)

        # finding numrevs
        revs = div.find_next('span', class_='review-count rating-qualifier')
        if revs:
            text = revs.get_text().strip().split(" ")[0]
            obj['numrevs'] = int(text)

        # finding price
        price = tag.find_next('span', class_='business-attribute price-range')
        if price:
            obj['price'] = price.get_text().strip()

    return result


with open('../../datasets/topic5.html', 'r', encoding='utf-8') as yelp_file:
    yelp_html = yelp_file.read()
    res = parseHtml(yelp_html)
    printJson(res)
