class MyAssertionRaisesContext:
    def __init__(self, error):
        self.error = error

    def __enter__(self):
        print("Entering context")

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")
        print("Error: {}".format(self.error))
        if exc_type is self.error:
            print("Caught error")
            return True


with MyAssertionRaisesContext(ValueError):
    raise ValueError("Something went wrong")

