
users = [
  {'id': 'john', 'name': "John Smith", 'age': 20},
  {'id': 'ann', 'name': "Ann Smith", 'age': 24},
  {'id': 'pete', 'name': "Pete Peterson", 'age': 31},
]

from functools import reduce

def group_by_id(users):
    return reduce(lambda acc, user: {**acc, user['id']: user}, users, {})

print(group_by_id(users))   
