# SECTION NOTEBOOK 5
import re


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


### Exercise 1 solution
def parse_email(s):
    """Parses a string as an email address, returning an (id, domain) pair."""
    pattern = re.compile(r'^[a-zA-Z][a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.-]+[a-zA-Z]$')
    isValidEmail = bool(pattern.search(s))
    if not isValidEmail:
        raise ValueError("Email not in correct format.")

    index = s.index("@")
    return s[:index], s[index + 1:]


### demo function call
for demo_str_ex1 in demo_str_ex1_list:
    print(f"eif_wrapper({demo_str_ex1}, parse_email) -> {eif_wrapper(demo_str_ex1, parse_email)}")
