boxes = [{ 'box1': [{'box2': 0}]  }, { 'box3': [  {'box4': ''}, {'box5':  [{'box6':  [{'box7':0}, {'box8': 'key'}]  }] }  ]  }]

# boxes = [{ 'box1': 0 }, {'box2': 'key'}]

# boxes = [{ 'box1': 0 }, {'box2':  [{'box3': 0}, {'box4': 'key'}] }]

def look_for_key(main_box):
    pile = main_box.copy()
    while pile:
        box = pile.pop()
        for box, content in box.items():
            if content == 'key':
                print('found the key in box', box)
                return box
            elif isinstance(content, list):
                for inner_box in content:
                    pile.append(inner_box)

# print(look_for_key(boxes))

def look_for_key2(main_box):
    for box in main_box:
        for box, content in box.items():
            if content == 'key':
                print('found the key in box', box)
                return box
            elif isinstance(content, list):
                look_for_key2(content)

# look_for_key2(boxes)

def fac(n):
    '''non tail recursion'''
    if n == 1:
        return 1
    else:
        return n * fac(n-1)

# print(fac(1000))

def fac2(n, acc=1):
    '''tail recursion'''
    if n == 1:
        return acc
    else:
        return fac2(n-1, acc * n)

print(fac2(100))

