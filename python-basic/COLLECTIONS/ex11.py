participants = ['Brian', 'Britney', 'Ben']
scores = {
  'brian': 25,
  'britney': 80,
  'ben': 50
}

def get_score(name):
    if name in participants:
        return scores[name.lower()]
    return f'{name} did not participate'

print(get_score('Paul'))
print(get_score('Britney'))
