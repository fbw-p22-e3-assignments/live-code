class FourDigitConverter:
    regex = '[0-9]{4}'
    
    def to_python(self, value):
        """Tells Django to convert URL string to a Python value"""
        return int(value)
    
    def to_url(self, value):
        """Tells Django to convert Python value to URL string"""
        return '%04d' % value
    