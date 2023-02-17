import openpyxl
file = open('test', 'w+')

# print(file.closed)

# with file as f:
#     print(file.closed)
#     pass
# print(file.closed)


class MyContext:
    def __init__(self, str1):
        self.str1 = str1

    def __enter__(self):
        print('Entering context')
        return 'greetings'

    def __exit__(self, err_type, err_value, traceback):
        print('Exiting context')
        pass
    

context_instance = MyContext('helo')

with MyContext('Hello') as f:
    print('inside context')
    

#openpyxl.load_workbook('mypyxl1.xlsx')