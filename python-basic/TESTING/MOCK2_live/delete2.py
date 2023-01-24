import os

def rm(filename):
    print('os.path', os.path.isfile(filename))
    if os.path.isfile(filename) == True:
        os.remove(filename)
    else:
        raise FileNotFoundError('file not found')


if __name__ == '__main__':
    rm('./bla.txt')