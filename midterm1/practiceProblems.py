# 0
# )
# -
# _
# p
# P
# ;
# :
# /
# ?
import math
import re
from collections import Counter

# SECTION PROBLEM 2
dna_seq = "ATGGCAATAACCCCCCGTTTCTACTTCTAGAGGAGAAAAGTATTGACATGAGCGCTCCCGGCACAAGGGCCAAAGAAGTCTCCAATTTCTTATTTCCGAATGACATGCGTCTCCTTGCGGGTAAATCACCGACCGCAATTCATAGAAGCCTGGGGGAACAGATAGGTCTAATTAGCTTAAGAGAGTAAATCCTGGGATCATTCAGTAGTAACCATAAACTTACGCTGGGGCTTCTTCGGCGGATTTTTACAGTTACCAACCAGGAGATTTGAAGTAAATCAGTTGAGGATTTAGCCGCGCTATCCGGTAATCTCCAAATTAAAACATACCGTTCCATGAAGGCTAGAATTACTTACCGGCCTTTTCCATGCCTGCGCTATACCCCCCCACTCTCCCGCTTATCCGTCCGAGCGGAGGCAGTGCGATCCTCCGTTAAGATATTCTTACGTGTGACGTAGCTATGTATTTTGCAGAGCTGGCGAACGCGTTGAACACTTCACAGATGGTAGGGATTCGGGTAAAGGGCGTATAATTGGGGACTAACATAGGCGTAGACTACGATGGCGCCAACTCAATCGCAGCTCGAGCGCCCTGAATAACGTACTCATCTCAACTCATTCTCGGCAATCTACCGAGCGACTCGATTATCAACGGCTGTCTAGCAGTTCTAATCTTTTGCCAGCATCGTAATAGCCTCCAAGAGATTGATGATAGCTATCGGCACAGAACTGAGACGGCGCCGATGGATAGCGGACTTTCGGTCAACCACAATTCCCCACGGGACAGGTCCTGCGGTGCGCATCACTCTGAATGTACAAGCAACCCAAGTGGGCCGAGCCTGGACTCAGCTGGTTCCTGCGTGAGCTCGAGACTCGGGATGACAGCTCTTTAAACATAGAGCGGGGGCGTCGAACGGTCGAGAAAGTCATAGTACCTCGGGTACCAACTTACTCAGGTTATTGCTTGAAGCTGTACTATTTTAGGGGGGGAGCGCTGAAGGTCTCTTCTTCTCATGACTGAACTCGCGAGGGTCGTGAAGTCGGTTCCTTCAATGGTTAAAAAACAAAGGCTTACTGTGCGCAGAGGAACGCCCATCTAGCGGCTGGCGTCTTGAATGCTCGGTCCCCTTTGTCATTCCGGATTAATCCATTTCCCTCATTCACGAGCTTGCGAAGTCTACATTGGTATATGAATGCGACCTAGAAGAGGGCGCTTAAAATTGGCAGTGGTTGATGCTCTAAACTCCATTTGGTTTACTCGTGCATCACCGCGATAGGCTGACAAAGGTTTAACATTGAATAGCAAGGCACTTCCGGTCTCAATGAACGGCCGGGAAAGGTACGCGCGCGGTATGGGAGGATCAAGGGGCCAATAGAGAGGCTCCTCTCTCACTCGCTAGGAGGCAAATGTAAAACAATGGTTACTGCATCGATACATAAAACATGTCCATCGGTTGCCCAAAGTGTTAAGTGTCTATCACCCCTAGGGCCGTTTCCCGCATATAAACGCCAGGTTGTATCCGCATTTGATGCTACCGTGGATGAGTCTGCGTCGAGCGCGCCGCACGAATGTTGCAATGTATTGCATGAGTAGGGTTGACTAAGAGCCGTTAGATGCGTCGCTGTACTAATAGTTGTCGACAGACCGTCGAGATTAGAAAATGGTACCAGCATTTTCGGAGGTTCTCTAACTAGTATGGATTGCGGTGTCTTCACTGTGCTGCGGCTACCCATCGCCTGAAATCCAGCTGGTGTCAAGCCATCCCCTCTCCGGGACGCCGCATGTAGTGAAACATATACGTTGCACGGGTTCACCGCGGTCCGTTCTGAGTCGACCAAGGACACAATCGAGCTCCGATCCGTACCCTCGACAAACTTGTACCCGACCCCCGGAGCTTGCCAGCTCCTCGGGTATCATGGAGCCTGTGGTTCATCGCGTCCGATATCAAACTTCGTCATGATAAAGTCCCCCCCTCGGGAGTACCAGAGAAGATGACTACTGAGTTGTGCGAT"


def count_bases(s):
    assert type(s) is str
    assert all([b in ['A', 'C', 'G', 'T'] for b in s])
    return dict(Counter(s))


def bio_to_regex(pattern_bio):
    mapping = {'R': '[GA]', 'Y': '[TC]', 'K': '[GT]', 'M': '[AC]', 'S': '[GC]', 'W': '[AT]',
               'B': '[GTC]', 'D': '[AGT]', 'H': '[ATC]', 'V': '[GAC]', 'N': '[ACGT]'}

    newStr = "".join([mapping.get(x) or x for x in pattern_bio])
    return re.compile(newStr)


def sim_cuts(site_pattern, s):
    [first, second] = site_pattern.split("|")
    matches = re.finditer(bio_to_regex(first), s)

    startIndex = 0
    result = []
    for match in matches:
        (i1, i2) = match.span()
        nextStr = s[i2: i2 + len(second)]
        nextMatches = bool(re.search(bio_to_regex(second), nextStr))
        if nextMatches:
            result.append(s[startIndex: i2])
            startIndex = i2

    if startIndex != 0:
        result.append(s[startIndex:])
    return result


# SECTION PROBLEM 7
hamlet_text = """

And can you by no drift of circumstance Get from him why he puts on this confusion Grating so harshly all his days of 
quiet With turbulent and dangerous lunacy? He does confess he feels himself distracted. But from what cause he will by 
no means speak. Nor do we find him forward to be sounded But with a crafty madness keeps aloof When we would bring 
him on to some confession Of his true state. Did he receive you well? Most like a gentleman. But with much forcing of 
his disposition. Niggard of question. but of our demands Most free in his reply. Did you assay him? To any pastime? 
Madam it so fell out that certain players We o'er-raught on the way. of these we told him. And there did seem in him a 
kind of joy To hear of it. they are about the court And as I think they have already order This night to play before 
him. 'Tis most true. And he beseech'd me to entreat your majesties To hear and see the matter. With all my heart. and 
it doth much content me To hear him so inclined. Good gentlemen give him a further edge And drive his purpose on to 
these delights. We shall my lord. Sweet Gertrude leave us too. For we have closely sent for Hamlet hither That he as 
'twere by accident may here Affront Ophelia. Her father and myself lawful espials Will so bestow ourselves that seeing 
unseen We may of their encounter frankly judge And gather by him as he is behaved If 't be the affliction of his love 
or no That thus he suffers for. I shall obey you. And for your part Ophelia I do wish That your good beauties be the 
happy cause Of Hamlet's wildness. so shall I hope your virtues Will bring him to his wonted way again To both your 
honours. Madam I wish it may. Ophelia walk you here. Gracious so please you We will bestow ourselves. Read on this 
book. That show of such an exercise may colour Your loneliness. We are oft to blame in this 'Tis too much proved that 
with devotion's visage And pious action we do sugar o'er The devil himself. O 'tis too true! How smart a lash that 
speech doth give my conscience! The harlot's cheek beautied with plastering art Is not more ugly to the thing that 
helps it Than is my deed to my most painted word. O heavy burthen! I hear him coming. let's withdraw my lord. To be 
or not to be. that is the question. Whether 'tis nobler in the mind to suffer The slings and arrows of outrageous 
fortune Or to take arms against a sea of troubles And by opposing end them? To die. to sleep. No more. and by a sleep 
to say we end The heart-ache and the thousand natural shocks That flesh is heir to 'tis a consummation Devoutly to be 
wish'd. To die to sleep. To sleep. perchance to dream. ay there's the rub. For in that sleep of death what dreams may 
come When we have shuffled off this mortal coil Must give us pause. there's the respect That makes calamity of so long 
life. For who would bear the whips and scorns of time The oppressor's wrong the proud man's contumely The pangs of 
despised love the law's delay The insolence of office and the spurns That patient merit of the unworthy takes When he 
himself might his quietus make With a bare bodkin? who would fardels bear To grunt and sweat under a weary life But 
that the dread of something after death The undiscover'd country from whose bourn No traveller returns puzzles the 
will And makes us rather bear those ills we have Than fly to others that we know not of? Thus conscience does make 
cowards of us all. And thus the native hue of resolution Is sicklied o'er with the pale cast of thought And 
enterprises of great pith and moment With this regard their currents turn awry And lose the name of action. Soft you 
now! The fair Ophelia! Nymph in thy orisons Be all my sins remember'd. Good my lord How does your honour for this 
many a day? I humbly thank you. well well well. My lord I have remembrances of yours That I have longed long to 
re-deliver. I pray you now receive them. No not I. I never gave you aught. My honour'd lord you know right well you 
did. And with them words of so sweet breath composed As made the things more rich. their perfume lost Take these 
again. for to the noble mind Rich gifts wax poor when givers prove unkind. There my lord. Ha ha! are you honest? My 
lord? Are you fair? What means your lordship? That if you be honest and fair your honesty should admit no discourse 
to your beauty. Could beauty my lord have better commerce than with honesty? Ay truly. for the power of beauty will 
sooner transform honesty from what it is to a bawd than the force of honesty can translate beauty into his likeness. 
this was sometime a paradox but now the time gives it proof. I did love you once. Indeed my lord you made me believe 
so. You should not have believed me. for virtue cannot so inoculate our old stock but we shall relish of it. I loved 
you not. I was the more deceived. Get thee to a nunnery. why wouldst thou be a breeder of sinners? I am myself 
indifferent honest. but yet I could accuse me of such things that it were better my mother had not borne me. I am 
very proud revengeful ambitious with more offences at my beck than I have thoughts to put them in imagination to give 
them shape or time to act them in. What should such fellows as I do crawling between earth and heaven? We are arrant 
knaves all. believe none of us. Go thy ways to a nunnery. Where's your father? At home my lord. Let the doors be shut 
upon him that he may play the fool no where but in's own house. Farewell. O help him you sweet heavens! If thou dost 
marry I'll give thee this plague for thy dowry. be thou as chaste as ice as pure as snow thou shalt not escape 
calumny. Get thee to a nunnery go. farewell. Or if thou wilt needs marry marry a fool. for wise men know well enough 
what monsters you make of them. To a nunnery go and quickly too. Farewell. O heavenly powers restore him! I have 
heard of your paintings too well enough. God has given you one face and you make yourselves another. you jig you 
amble and you lisp and nick-name God's creatures and make your wantonness your ignorance. Go to I'll no more on't. 
it hath made me mad. I say we will have no more marriages. those that are married already all but one shall live. the 
rest shall keep as they are. To a nunnery go. O what a noble mind is here o'erthrown! The courtier's soldier's 
scholar's eye tongue sword. The expectancy and rose of the fair state The glass of fashion and the mould of form The 
observed of all observers quite quite down! And I of ladies most deject and wretched That suck'd the honey of his 
music vows Now see that noble and most sovereign reason Like sweet bells jangled out of tune and harsh. That 
unmatch'd form and feature of blown youth Blasted with ecstasy. O woe is me To have seen what I have seen see what I 
see! Love! his affections do not that way tend. Nor what he spake though it lack'd form a little Was not like madness. 
There's something in his soul O'er which his melancholy sits on brood. And I do doubt the hatch and the disclose Will 
be some danger. which for to prevent I have in quick determination Thus set it down. he shall with speed to England 
For the demand of our neglected tribute Haply the seas and countries different With variable objects shall expel 
This something-settled matter in his heart Whereon his brains still beating puts him thus From fashion of himself. 
What think you on't? It shall do well. but yet do I believe The origin and commencement of his grief Sprung from 
neglected love. How now Ophelia! You need not tell us what Lord Hamlet said. We heard it all. My lord do as you 
please. But if you hold it fit after the play Let his queen mother all alone entreat him To show his grief. let her 
be round with him. And I'll be placed so please you in the ear Of all their conference. If she find him not To England 
send him or confine him where Your wisdom best shall think. It shall be so. Madness in great ones must not unwatch'd 
go.

"""

hamsplits = []


def splitHamletText(text):
    pattern = re.compile(r'[\w\s\']*[.?!]')
    matches = re.finditer(pattern, text)
    result = []
    for match in matches:
        (start, end) = match.span()
        formattedSentence = ["".join([c for c in x.lower() if c.isalnum()]) for x in
                             text[start: end].strip().split()]
        result.append(formattedSentence)

    return result


# We now want to make a sequential pairs dictionary.
def getHamDict(hamsplits):
    hamdict = {}
    for sentence in hamsplits:
        for index in range(len(sentence) - 1):
            word = sentence[index]
            value = sentence[index + 1]
            if word in hamdict:
                hamdict[word].append(value)
            else:
                hamdict[word] = [value]

    return hamdict


def wordsNotInDict(hamdict, hamsplits):
    result = []
    for sentence in hamsplits:
        for index, word in enumerate(sentence):
            if word not in hamdict:
                result.append(word)

    return result


# SECTION PROBLEM 29

def enum_filter(fun, iterable):
    return [(value, index) for index, value in enumerate(iterable) if fun(value) is True]


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


### Define demo inputs ###
demo_dictionary_ex1_okay = {1: 7, 'cat': 9, 3: False}
demo_dictionary_ex1_bad = {1: 7, 'cat': 9, 3: 7}


### Exercise 1 solution
def invert_dict(dictionary):
    result = {}
    for (key, value) in dictionary.items():
        if value not in result:
            result[value] = key
        else:
            raise ValueError("Key already there.")
    return result


### Exercise 3 solution
toString = '''bdarter@coral-energy.com, onvacation@pdq.net, kimberly.s.olinger@enron.com,
	scott.hendrickson@enron.com, cnmfree@hrb.de, ddarter@webtv.net,
	vdaniels@imsday.com'''

newString = '''ben.glisan@enron.com,
 	and(rew.fastow@enron.com,
 richard.causey@enron.com,
 rick.buy@enron.com,
 greg.whalley@enron.com'''

fromString = 'rew.fastow@enron.com'


def gather_addresses_from_field(email, field):
    pattern = r'''((?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\]))'''
    compiled = re.compile(pattern)
    string = email.get(field)
    resultSet = set()
    if string:
        for str in string.split(","):
            match = compiled.search(str)
            if match:
                (start, end) = match.span()
                emailFound = str[start: end]
                resultSet.add(emailFound)

    return resultSet


### Define demo inputs ###

demo_addresses_ex4 = {
    'grampus@sunbeach.net',
    'petersm@energystore.net',
    'knowak@wpo.org',
    'lhgas@hoegh.no',
    'llightfoot@coral-energy.com',
    'sjohnsto@wutc.wa.gov',
    'amitava.dhar@enron.com',
    'jennifer.blay@enron.com',
    'lburns@hotmail.com',
    'steve.schneider@enron.com',
    'amy.fitzpatrick@enron.com'
}


### Exercise 4 solution
def get_enron_addresses(addresses):
    result = set()
    for email in addresses:
        pattern = re.compile(r'[\w.\s]*@enron.com')
        isValidEmail = bool(pattern.search(email))
        if isValidEmail:
            result.add(email)

    return result


### Define demo inputs ###

demo_address_map_ex5 = [
    {'From': {'jeffery.fawcett@enron.com'},
     'To': {'drew.fossum@enron.com'},
     'Cc': set(),
     'Bcc': set()},
    {'From': {'lloyd.will@enron.com'},
     'To': {'smith.day@enron.com'},
     'Cc': {'clint.dean@enron.com',
            'jeffrey.miller@enron.com',
            'jim.homco@enron.com',
            'smith.day@enron.com',
            'tom.may@enron.com'},
     'Bcc': {'clint.dean@enron.com',
             'jeffrey.miller@enron.com',
             'jim.homco@enron.com',
             'smith.day@enron.com',
             'tom.may@enron.com'}}
]


### Exercise 5 solution
def remove_duplicates(address_map):
    output = []
    for address in address_map:
        output.append({
            'From': address['From'],
            'To': {x for x in address['To'] if x not in address['From']},
            'Cc': {x for x in address['Cc'] if x not in address['From'].union(address['To'])},
            'Bcc': {x for x in address['Bcc'] if
                    x not in address['From'].union(address['To']).union(address['Cc'])},
        })
    return output


### demo function call ###
demo_your_solution_ex5 = remove_duplicates(demo_address_map_ex5)
print(demo_your_solution_ex5)

### Define demo inputs ###

demo_address_map_ex6 = [
    # Message 0:
    {'From': {'a@enron.com'}, 'To': {'b@enron.com', 'c@enron.com'}, 'Cc': set(),
     'Bcc': {'d@enron.com'}},
    # Message 1:
    {'From': {'b@enron.com'}, 'To': set(), 'Cc': set(), 'Bcc': {'d@enron.com'}},
    # Message 2:
    {'From': {'d@enron.com'}, 'To': {'a@enron.com'}, 'Cc': set(), 'Bcc': {'e@enron.com'}},
]


### Exercise 6 solution
def count_addresses(address_map):
    counts = {}
    for address in address_map:
        for key, value in address.items():
            for email in value:
                if email in counts:
                    counts[email] += 1
                else:
                    counts[email] = 1

    return counts


# Exercise 7 solution
def gen_coords(address_map, address_to_id, address_counts):
    result = {}
    b_weight = {'From': 1.0, 'To': 0.5, 'Cc': 0.25, 'Bcc': 0.75}

    for index, address in enumerate(address_map):
        for key, value in address.items():
            for email in value:
                addressId = address_to_id[email]
                messageId = index

                # calculate score
                M = len(address_map)
                na = address_counts[email]
                b = b_weight[key]
                score = 1 / math.log((M + 1) / b * na)
                result[(messageId, addressId)] = score
    return result
