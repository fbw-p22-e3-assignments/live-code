def decorator(func):
    def inner(*args, **kwargs):
        return f"<strong> {func(*args, **kwargs)} </strong>"
    return inner    

def decorator2(func):
    def inner(*args, **kwargs):
        return f"<p> {func(*args, **kwargs)} </p>"
    return inner    


#@decorator2
@decorator
def getName(fname, lname):
    return fname + ' ' + lname

def getName(fname, lname):
    return '<strong>' + fname + ' ' + lname + '</strong>'

print(getName('John', 'Doe'))