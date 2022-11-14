l = ['spam', 'eggs', 'ham', 'bacon', 'spam', 'spam']


d = {}
for item in l:
    d[item] = None

unique_key_list = list(d.keys())

print(unique_key_list) # dict_keys(['spam', 'eggs', 'ham', 'bacon'])