import re
import pandas as pd
import numpy as np
import sqlite3
from collections import Counter
from collections import defaultdict

### Solution - Exercise 0

# Exercise 0 (2 points)
def get_table_cols(table_name, conn):
    if not re.match("^[A-Za-z0-9_]*$", table_name):
        raise ValueError()

    c = conn.cursor()
    c.execute("""
       SELECT 
           sql 
       FROM 
           sqlite_master 
       WHERE 
           type = 'table' AND 
           name = ?""", (table_name,))
    conn.commit()
    results = c.fetchall()
    str = results[0][0].replace("\n", "")
    cols = str[str.index("(") + 1: str.index(")")].split(",")
    formatted = sorted([x[x.index('"') + 1: x.rindex('"')] for x in cols])
    print(formatted)
    return formatted


# Exercise 1 (1 points)
def intersection_of_cols(lol: list, num=None) -> set:
    assert len(lol) > 1, '`lol` must have at least 2 items'
    if num is None:
        num = len(lol)

    arr = [val for x in lol for val in set(x)]
    res = set([key for key, value in Counter(arr).items() if value >= num])
    return res

### Demo function call
for num in [2,3]:
    demo_intersection = intersection_of_cols(
        lol=[['ringo', 'phyllis', 'angela', 'paul'],
             ['kevin', 'paul', 'oscar', 'kelly', 'phyllis'],
             ['phyllis', 'oscar', 'ryan', 'john', 'toby']],
        num=num)
    #print(f'num={num}; intersection={demo_intersection}')


### Solution - Exercise 2
result = [('10/26/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('11/21/2016', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/24/2019', 'Injured'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Injured'), ('10/26/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/02/2019', 'Unspecified'), ('10/22/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/26/2019', 'Injured'), ('10/24/2019', 'Unspecified'), ('10/23/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Injured'), ('10/25/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/23/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/10/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Injured'), ('10/26/2019', 'Unspecified'), ('10/26/2019', 'Unspecified'), ('10/24/2019', 'Unspecified'), ('10/25/2019', 'Unspecified'), ('10/26/2019', 'Unspecified')]
def summarize_person(result):
    mapped_arr = [(x[0].split("/")[2], x[1]) for x in result]

    data = {}

    for row in mapped_arr:
        year = row[0]
        injury = row[1]

        key = ""
        if injury == "Injured":
            key = "INJURY_COUNT"
        elif injury == "Killed":
            key = "DEATHS_COUNT"
        else:
            key = "UNSPECIFIED_COUNT"

        if (year in data):
            if key in data[year]:
                data[year][key] += 1
            else:
                data[year][key] = 1
        else:
            data[year] = {}
            data[year][key] = 1

    sorted_data = dict(sorted(data.items()))
    pd_data = {
        'YEAR': list(sorted_data.keys()),
        'INJURY_COUNT': [value['INJURY_COUNT'] for key, value in sorted_data.items()],
        'DEATHS_COUNT': [value['DEATHS_COUNT'] for key, value in sorted_data.items()],
        'UNSPECIFIED_COUNT': [value['UNSPECIFIED_COUNT'] for key, value in sorted_data.items()]
    }

    dataframe = pd.DataFrame(pd_data)
    return dataframe

data = {'2019': {'UNSPECIFIED_COUNT': 792637, 'INJURY_COUNT': 61388, 'DEATH_COUNT': 244}, '2016': {'UNSPECIFIED_COUNT': 740038, 'INJURY_COUNT': 60076, 'DEATH_COUNT': 239}, '2020': {'INJURY_COUNT': 44614, 'UNSPECIFIED_COUNT': 368310, 'DEATH_COUNT': 269}, '2018': {'UNSPECIFIED_COUNT': 884054, 'INJURY_COUNT': 61918, 'DEATH_COUNT': 231}, '2015': {'INJURY_COUNT': 51357, 'UNSPECIFIED_COUNT': 571, 'DEATH_COUNT': 243}, '2022': {'UNSPECIFIED_COUNT': 310335, 'INJURY_COUNT': 51931, 'DEATH_COUNT': 289}, '2012': {'INJURY_COUNT': 27447, 'DEATH_COUNT': 137, 'UNSPECIFIED_COUNT': 87}, '2013': {'INJURY_COUNT': 55127, 'UNSPECIFIED_COUNT': 191, 'DEATH_COUNT': 297}, '2017': {'UNSPECIFIED_COUNT': 900859, 'INJURY_COUNT': 60655, 'DEATH_COUNT': 261}, '2014': {'INJURY_COUNT': 51212, 'DEATH_COUNT': 262, 'UNSPECIFIED_COUNT': 379}, '2023': {'UNSPECIFIED_COUNT': 284491, 'INJURY_COUNT': 54230, 'DEATH_COUNT': 273}, '2021': {'INJURY_COUNT': 51782, 'UNSPECIFIED_COUNT': 333997, 'DEATH_COUNT': 296}, '2024': {'UNSPECIFIED_COUNT': 41617, 'INJURY_COUNT': 8037, 'DEATH_COUNT': 41}}

def create_pd(data):
    sorted_data =  dict(sorted(data.items()))
    pd_data = {
        'YEAR' : list(sorted_data.keys()),
        'INJURY_COUNT': [value['INJURY_COUNT'] for key, value in sorted_data.items()],
        'DEATHS_COUNT': [value['DEATH_COUNT'] for key, value in sorted_data.items()],
        'UNSPECIFIED_COUNT': [value['UNSPECIFIED_COUNT'] for key, value in sorted_data.items()]
    }

    dataframe = pd.DataFrame(pd_data)
    print(dataframe)
    return dataframe
    # years = list(sorted_data.keys())
    # injury_count = [value['INJURY_COUNT'] for key, value in sorted_data.items()]
    # print(years)
    # print(injury_count)

### Demo function call
#summarize_person(result)
# create_pd(data)


### Solution - Exercise 3
def summarize_crashes(conn):
    c = conn.cursor()
    # CAST(SUBSTR("CRASH DATE", 1, 4) AS integer)
    query = '''SELECT YEAR, COUNT(YEAR) AS CRASH_COUNT, SUM(DEATH_COUNT) AS DEATHS, SUM(PED_DEAD) AS PEDESTRIAN_DEATHS,
                (SUM(PED_DEAD) / SUM(DEATH_COUNT)) AS PEDESTRIAN_DEATH_SHARE,
                (SUM(DEATH_COUNT) /  COUNT(YEAR)) AS DEATHS_PER_CRASH
                FROM (SELECT SUBSTR("CRASH DATE", 7, 12) AS YEAR, "NUMBER OF PERSONS KILLED" AS DEATH_COUNT,
                    "NUMBER OF PEDESTRIANS KILLED" AS PED_DEAD
                    FROM CRASHES)
                GROUP BY YEAR
            '''
    c.execute(query)
    conn.commit()
    result = c.fetchall()

    df = pd.read_sql(query, conn)
    return df


### Solution - Exercise 5
def geo_filter_crashes(qry, conn, params):
    df = pd.read_sql(qry, conn, params=params)
    df['CRASH_DATE'] = pd.to_datetime(df['CRASH_DATE'])
    return df