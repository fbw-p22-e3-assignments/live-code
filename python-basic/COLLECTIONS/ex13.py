students = [
  {
    'name': 'Peter', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'C'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Robin', 
    'subjects': [
      {'name': 'English', 'grade': 'D'},
      {'name': 'German', 'grade': 'B'},
      {'name': 'Maths', 'grade': 'B'}
    ]
  },
  {
    'name': 'Michael', 
    'subjects': [
      {'name': 'English', 'grade': 'A'},
      {'name': 'German', 'grade': 'F'},
      {'name': 'Maths', 'grade': 'F'}
    ]
  },
]

import collections
from itertools import groupby

def get_student3():
  result = []
  for student in students:
    result = [*result, *[{'student': student['name'], **subject} for subject in student['subjects']]]
  for key, value in groupby(result, lambda x: x['student']):
    print(key)
    for grade, subject in groupby(value, lambda x: x['grade']):
      print(grade)
      print(len(list(subject)))


# def get_student2():
#   chain_sub = collections.ChainMap({})
#   for student in students:
#     chain_sub = chain_sub.new_child(student['subjects'])
#   print(chain_sub.maps)

def get_student():
  for student in students:
    ct = collections.Counter()  
    ct.update([subject['grade'] for subject in student['subjects']])
    if not ct['F'] >= 2:
      print(student)

get_student3()




