#task1

with open('./data/text1.txt', 'r') as file1:
        content = file1.read()
        with open('./data/task1.txt', 'bw') as file2:
            # print(content.encode('utf-8'))
            file2.write(content.encode('utf-8'))


#task2
import os

files = [
    {
        "name": "todos.txt",
        "content": ["My ToDos:", "", "Go shopping", "Finish module"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["My links:", "", "https://google.com", "https://digitalcareerinstitute.org"]
    }
]

for file in files:
    with open('./data/' + file['name'], 'w') as f:
        for line in file['content']:
            f.write(line + '\n')

#task3

additions = [
    {
        "name": "todos.txt",
        "content": ["Call mom", "Walk the dog"]
    },
    {
        "name": "bookmarks.txt",
        "content": ["https://python.org", "https://www.djangoproject.com/"]
    }
]

for file in additions:
    with open('./data/' + file['name'], 'a') as f:
            f.writelines(line + '\n' for line in file['content'])
    
#task4

changes = [
    {
        "name": "todos.txt",
        "change": ("Call mom", "Clean up house")
    },
    {
        "name": "bookmarks.txt",
        "change": ("https://google.com", "https://www.w3resource.com")
    }
]

for file in changes:
    text_from = file['change'][0]
    text_to = file['change'][1]

    with open('./data/' + file['name'], 'r+') as f:
        content = f.read()
        start = content.index(text_from)
        end = start + len(text_from)
        suffix = content[end:]
        f.seek(start)
        f.write(text_to + suffix)

#task5

with open('./data/todos.txt', 'r') as f:
    with open('./data/todo.secret', 'w') as secret:
        content = f.read()
        encrypted = [str(ord(char)) + '\n' for char in content]
        secret.writelines(encrypted)

with open('./data/todo.secret', 'r') as secret:
    content = secret.read()
    joined = content.split('\n')
    decrypted = ''.join([chr(int(num)) for num in joined if num != ''])
    print(decrypted)



