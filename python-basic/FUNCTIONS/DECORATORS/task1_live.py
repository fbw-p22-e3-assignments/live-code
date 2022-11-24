
#decorator implementation

def add_div(func):
    def inner():
        print('inner')
        return  f"<div> {func()} </div>" 
    return inner

def add_p(func):
    def inner():
        print('inner')
        return  f"<p> {func()} </p>" 
    return inner


def add_p_or_div(func):
    def inner(isP):
        print('inner')
        if isP:
            return  f"<p> {func()} </p>"
        else:
            return  f"<div> {func()} </div>"

    return inner
## define function which returns a name

# def getName():
#     return 'John'


# print(getName())  # <div> John <div>

@add_p_or_div
def getName():
    return 'John'


print(getName(False))  # <div> John <div>
