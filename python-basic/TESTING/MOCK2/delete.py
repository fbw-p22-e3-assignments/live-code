import os

def rm(filename):
    if os.path.isfile(filename) == True:
        print('os path:', os.path.isfile(filename))
        os.remove(filename)
    else:
        raise FileNotFoundError('File not found')


