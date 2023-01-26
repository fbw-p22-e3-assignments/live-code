def upper1(text):
    try:
        return text.upper()
    except AttributeError as er:
        print('re-raise Attribute')
        raise TypeError

upper1(1)