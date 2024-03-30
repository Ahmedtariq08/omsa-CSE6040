### Global Imports

###
### AUTOGRADER TEST - DO NOT REMOVE
###

# Import required modules
# Feel free to import anything else you find useful
import pandas as pd
#import dill as pickle
from io import StringIO
# from matplotlib import pyplot as plt
import numpy as np
from scipy.stats import norm

# from football_utils import *

# loading the raw data
# with open('datasets\midterm2\\all_events_df.pkl', 'rb') as f:
#     all_events_df = pickle.load(f)

arr = np.array([1, 2, 3])


def convert_string_to_dataframe(data_str):
    data_str = data_str.strip()
    lines = data_str.split('\n')
    column_names = lines[0].split()
    df = pd.DataFrame(columns=column_names)

    for line in lines[1:]:
        values = [x.strip() for x in line.split('\t')[1:]]
        if len(values) == len(column_names):
            df.loc[len(df)] = values

    return df


# Exercise 0 (2 p0ints)
data = {
    'play_id': [99, 154, 27, 83, 26],
    'drive_id': [4008746382403, 4008745353875, 401030721707, 4011279702090, 400791570689],
    'event_id': [40087463814, 40087453524, 4010307216, 40112797010, 4007915705],
    'sequenceNumber': [240300, 387500, 70700, 209000, 68900],
    'type': ['Rush', 'Rush', 'Rush', 'Field Goal Missed', 'Pass Reception'],
    'poss_team_id': [6, 29, 26, 34, 34],
    'scoringPlay': [False, False, False, False, False],
    'awayScore': [10, 20, 7, 7, 7],
    'homeScore': [10, 31, 7, 17, 0],
    'period': [3, 4, 1, 2, 1],
    'clock': ['9:48', '9:48', '5:29', '0:02', '4:13'],
    'homeTeamPoss': [True, True, False, False, True],
    'down': [2, 1, 2, 1, 2],
    'distance': [2, 10, 8, 10, 11],
    'yardsToEndzone': [53, 15, 66, 38, 26]
}

all_events_df = pd.DataFrame(data)


def calc_time_left(all_events_df: pd.DataFrame) -> pd.DataFrame:
    newDf = all_events_df.copy()

    def performCalculation(row):
        clock = row['clock'].split(":")
        value = (15 * 60) * (4 - row['period']) + (60 * int(clock[0])) + int(clock[1])
        print(value)
        return value

    newDf['timeLeft'] = newDf.apply(performCalculation, axis=1)
    return newDf


# print(calc_time_left(all_events_df))

# Exercise 1 (2 points)
data2 = {
    'type': ['Punt', 'Two Point Rush', 'Two-minute warning', 'Rush', 'Timeout', 'Rush', 'End Period',
             'Rushing Touchdown', 'Timeout', 'Timeout', 'Pass Reception', 'Pass Reception', 'Extra Point Good', 'Rush',
             'Pass Reception', 'Timeout', 'Two-minute warning', 'Pass Reception'],
    'timeLeft': [-830, 0, 1920, 976, 332, 3533, 900, 3165, 1533, 51, -473, -317, 3214, 792, -235, -894, 1920, 926],
    'event_id': [401127999, 400874631, 401437889, 401220231, 400951744, 401127999, 401220213, 400554399, 401249063,
                 401437866, 400951562, 400874555, 401326418, 400874553, 400874621, 401030770, 401220292, 401437633]
}

demo_df_ex1 = pd.DataFrame(data2)


def filter_non_plays_and_ot(df: pd.DataFrame) -> pd.DataFrame:
    non_play_types = ['Penalty', 'End Period', 'Two-minute warning', 'Timeout', 'End of Half',
                      'End of Game', 'Official Timeout', 'Defensive 2pt Conversion',
                      'Two Point Rush', 'Extra Point Good']

    ot_event_ids = df[df['timeLeft'] < 0]['event_id']
    newDf = df[(~df['type'].isin(non_play_types)) & (~df['event_id'].isin(ot_event_ids.values))]
    return newDf


# Exercise 2 (2 points)
data3 = {
    'drive_id': [4014356414, 4014356414, 4014356414, 4014356414, 4014356414, 4014356414,
                 4014356418, 4014356418, 4014356418, 4014356418, 4014356418, 4014356418,
                 4014356411, 4014356411, 4014356411, 4014356411, 4014356411],
    'type': ['Pass Reception', 'Rush', 'Rush', 'Rush', 'Pass Reception', 'Passing Touchdown',
             'Pass Incompletion', 'Rush', 'Rush', 'Pass Incompletion', 'Pass Reception', 'Field Goal Good',
             'Kickoff Return (Offense)', 'Pass Incompletion', 'Rush', 'Sack', 'Punt'],
    'scoringPlay': [False, False, False, False, False, True, False, False, False, False, False, True, False, False,
                    False, False, False],
    'down': [1, 2, 2, 1, 2, 3, 1, 2, 1, 2, 3, 4, 0, 1, 2, 3, 4],
    'timeLeft': [3336, 3304, 3288, 3248, 3207, 3160, 2452, 2448, 2412, 2370, 2362, 2323, 3600, 3594, 3589, 3547, 3515]
}

demo_event_df_ex2 = pd.DataFrame(data3)


### Helper function provided as part of the starter code
def converted_by_drive(group: pd.DataFrame) -> pd.DataFrame:
    group = group.sort_values('timeLeft', ascending=False) \
        .reset_index(drop=True)
    offensive_touchdown_types = ['Passing Touchdown', 'Rushing Touchdown',
                                 'Fumble Recovery (Own)', 'Rush', 'Pass Reception']
    # `pd.DataFrame.shift` might be useful later...
    first_downs = (group['down'] == 1).shift(-1, fill_value=False)
    scores = (group['scoringPlay'] == True) & (group['type'].isin(offensive_touchdown_types))
    group['converted'] = (first_downs | scores)
    return group


### Your solution
def converted(event_df: pd.DataFrame) -> pd.DataFrame:
    df = event_df.groupby('drive_id').apply(lambda x: converted_by_drive(x)).reset_index(drop=True)
    return df


# converted(demo_event_df_ex2)

# Exercise 3 (2 points)
demo_event_df_ex3 = convert_string_to_dataframe('''awayScore	homeScore	homeTeamPoss	timeLeft
0	0	0	True	3600
1	0	0	False	3600
2	0	0	False	3559
3	0	0	False	3523
4	0	0	False	3490
139	6	26	False	149
140	6	26	False	121
141	6	26	True	111
142	6	26	True	66
143	6	26	True	31''')


### Exercise 3 solution
def who_won(event_df: pd.DataFrame) -> pd.DataFrame:
    df = event_df.copy()
    homeMax = int(df['homeScore'].max())
    awayMax = int(df['awayScore'].max())

    def checkWhoWon(row):
        offense = True if row['homeTeamPoss'] == "True" else False
        return offense if homeMax > awayMax else not offense

    df['won'] = df.apply(checkWhoWon, axis=1)
    return df


# Exercise 4 (3 points)

data4 = {
    'awayScore': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 10, 10, 13, 13, 13, 13, 13, 13, 16, 16, 16, 16, 16,
                  16],
    'homeScore': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 7, 7, 7, 7, 7, 7, 14, 14],
    'timeLeft': [3477, 3358, 3239, 3115, 3002, 2885, 2767, 2650, 2534, 2413, 2299, 2182, 2065, 1949, 1826, 1707, 1594,
                 1471, 1348, 1230, 1106, 987, 867, 746, 625, 503, 383, 265, 147, 26],
    'scoringPlay': [False, False, False, False, False, False, False, False, False, False, True, False, False, False,
                    False, False, True, False, True, False, False, False, True, False, True, False, False, False, True,
                    False],
    'homeTeamPoss': [False, True, True, True, False, False, False, True, False, False, False, False, True, True, True,
                     True, True, True, False, True, True, True, False, True, True, False, False, True, True, True]
}

demo_event_df_ex4 = pd.DataFrame(data4)


def get_update_list(df: pd.DataFrame) -> list:
    scoring = df.loc[df['scoringPlay'], ['awayScore', 'homeScore']]
    scoring[['previousAway', 'previousHome']] = scoring.shift(1, fill_value=0)
    scoring['next_score'] = (scoring['homeScore'] - scoring['previousHome']) - \
                            (scoring['awayScore'] - scoring['previousAway'])
    return [(0, 0), *[(k + 1, v) for k, v in scoring['next_score'].to_dict().items()], (len(df), 0)]


# with open('resource/asnlib/publicdata/demo_output_ex4.pkl', 'rb') as f:
#     true_demo_output_ex4 = pickle.load(f)

# with open('resource/asnlib/publicdata/demo_event_df_ex4.pkl', 'rb') as f:
#     demo_event_df_ex4 = pickle.load(f)

### Exercise 4 solution
def add_next_score(event_df: pd.DataFrame) -> pd.DataFrame:
    df = event_df.copy().sort_values(by=["timeLeft"], ascending=False)
    update_list = get_update_list(df)
    print(update_list)

    def get_zipped_array(update_list, i):
        score = update_list[i + 1][1]
        rng = list(range(update_list[i][0], update_list[i + 1][0]))
        arr = list(zip(rng, [score] * len(rng)))
        return arr

    output = []
    for i in range(len(update_list) - 1):
        output += get_zipped_array(update_list, i)

    # test1 = [range(update_list[i][0], update_list[i+1][0]) for i in range(len(update_list) - 1)]
    test1 = [get_zipped_array(update_list, i) for i in range(len(update_list) - 1)]
    print(output)
    print(len(output))

    return df


demo_output_ex4 = add_next_score(demo_event_df_ex4)
# print(demo_output_ex4)
