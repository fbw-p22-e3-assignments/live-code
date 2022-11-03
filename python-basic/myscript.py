import re
print('\1')
result = re.sub('0*([\w\s]*)(\.*(0*[1-9]+)*)0*','\\1\\2', "00023.0440560000")
print(result)