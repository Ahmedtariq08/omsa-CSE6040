import sqlite3 as db

# Connect to a database (or create one if it doesn't exist)
conn = db.connect('example.db')
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS Students")
c.execute("CREATE TABLE Students (gtid INTEGER, name TEXT)")

# An important (and secure!) idiom
more_students = [(123, 'Vuduc'), (456, 'Chau'), (381, 'Bader'), (991, 'Sokol'), (723, 'Rozga'),
                 (882, 'Zha'), (401, 'Park'), (377, 'Vetter'), (904, 'Brown')]

# '?' question marks are placeholders for the two columns in Students table
c.executemany('INSERT INTO Students VALUES (?, ?)', more_students)
conn.commit()

# EXERCISE 1 (2 points)
# Run this cell
c.execute('DROP TABLE IF EXISTS Takes')
c.execute('CREATE TABLE Takes (gtid INTEGER, course TEXT, grade REAL)')

def getIdFromName(name):
    c.execute("SELECT gtid FROM Students WHERE name = '{}'".format(name))
    return c.fetchone()[0]


VuducId = getIdFromName('Vuduc')
SokolId = getIdFromName('Sokol')
ChauId = getIdFromName('Chau')

takes = [(VuducId, 'CSE 6040', 4.0), (VuducId, 'ISYE 6644', 3.0), (VuducId, 'MGMT 8803', 1.0),
         (SokolId, 'CSE 6040', 4.0), (SokolId, 'ISYE 6740', 4.0),
         (ChauId, 'CSE 6040', 4.0),  (ChauId, 'ISYE 6740', 2.0), (ChauId, 'MGMT 8803', 3.0)]

c.executemany('INSERT INTO Takes VALUES (?, ?, ?)', takes)
conn.commit()

c.execute("SELECT * FROM Takes")
results = c.fetchall()
print("Your results:", len(results), "\nThe entries of Takes:\n", results)

# Exercise 2 (2 points)
query = '''
        SELECT Students.name, Takes.grade
        FROM Students
        INNER JOIN Takes ON Students.gtid = Takes.gtid
        WHERE Takes.course = 'CSE 6040' 
'''

c.execute(query)
results1 = c.fetchall()
#print(results1)

# Exercise 3 (2 points)
query = '''
        SELECT Students.name, Takes.grade
        FROM Students
        LEFT JOIN Takes ON Students.gtid = Takes.gtid 
'''

c.execute(query)
results2 = c.fetchall()



### PART 1

# Exercise 1
queryp1 = '''
  SELECT LOWER(ComplaintType) AS type, COUNT(*) AS freq
    FROM data
    GROUP BY LOWER(ComplaintType)
    ORDER BY freq DESC
'''

queryp2 = '''
  SELECT name, freq
    FROM (SELECT LOWER(ComplaintType) AS type, COUNT(*) AS freq, UPPER(City) AS name 
        FROM data
        GROUP BY name
        ORDER BY -freq)
    LIMIT 10
'''


def strs_to_args(str_list):
    assert type (str_list) is list
    assert all ([type (s) is str for s in str_list])
    return ", ".join(['"{}"'.format(x) for x in str_list])


str_list = ['a', 'b', 'c', 'd']
print(strs_to_args(str_list))