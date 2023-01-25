import my_module

def greeting(name):
    print(my_module)
    return f"Hello {my_module.lower(name)}, I'm {my_module.upper(name)}"

if __name__ == '__main__':
    print(greeting('Bob'))