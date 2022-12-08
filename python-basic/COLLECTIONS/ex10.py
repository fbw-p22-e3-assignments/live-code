import re
l33t = ['Digital Car33r Institute', 'DCI', 'Digital', 'Career', 'Inst1tut3']

def digit_filter(strings):
    return [string for string in strings if re.search(r'^[a-zA-z\s]+$', string)]


def digit_filter1(original):
  new = []
  for string in original:
    if any(char for char in string if char.isdigit()):
      continue
    else:
      new.append(string)
  return new

# print(digit_filter1(l33t))
# print(all([char for char in 'bla3awd' if char.isdigit()]))
# print(([char.isdigit() for char in 'bjahw3d']))

###Refactored Version
def digit_filter2(strings):
    return [string for string in strings if not any([char.isdigit() for char in string])]

print(digit_filter2(l33t))