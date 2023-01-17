class MyContext:
    def __enter__(self):
        print('entering context')
        return 'BLA'
    def __exit__(self, exc_type, exc_value, traceback):
        print('exiting context')
        print('exc_type:', exc_type)
        print('exc_value:', exc_value)
        print('traceback:', traceback)
        print('line of error (traceback):', traceback.tb_frame)
        print('line of error (traceback):', traceback.tb_lineno)
        if exc_type is ValueError:
            print('ValueError')
            print('*******ERROR******')
            print('')
            return False
            return True


def my_func():
    with MyContext() as value:
        raise ValueError('Whatever')


if __name__ == '__main__':
    my_func()
