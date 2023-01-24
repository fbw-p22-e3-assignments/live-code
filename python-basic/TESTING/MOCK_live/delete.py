import os

def rm(filename):
    os.remove(filename)
    # print('delete file')


if __name__ == '__main__':
    rm('MOCK_live/somefile.txt')