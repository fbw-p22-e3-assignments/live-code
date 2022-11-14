# coding: utf-8
#####checking for valid phone numbers in the following format: 123-456-7891
my_number = '123-456-7891'
my_number[:3]
my_number[:3].isdigit()
my_number[4] == '-'
my_number[4]
my_number[3]
my_number[3] == '-'
not my_number[0:4].isdigit()
(not my_number[0:4].isdigit())
(!my_number[0:4].isdigit())
not (my_number[0:4].isdigit())
not (my_number[0:3].isdigit())
my_number[0:3] + my_number[3:4]
my_number[0:3] + my_number[3:5]
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:].isdigit():
    print(False)
else:
    print(True)
    
my_number = '123-45-7891'
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:].isdigit():
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:11].isdigit():
    print(False)
else:
    print(True)
    
my_number = '123-453-789'
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:11].isdigit():
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:10].isdigit():
    print(False)
else:
    print(True)
    
my_number[8:10]
my_number[8:11]
my_number[8:12]
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit():
    print(False)
else:
    print(True)
    
my_number
number[8:]
my_number[8:]
len(my_number[8:])
my_number = '123-453-7891'
len(my_number[8:])
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() and len(my_number[8:]):
    print(False)
else:
    print(True)
    
    
    
    
    
    
    
    
my_number = '123-453-789'
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() and len(my_number[8:]):
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() and len(my_number[8:]) == 4:
    print(False)
else:
    print(True)
    
len(my_number[8:])
len(my_number[8:]) == 4
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() and len(my_number[8:]) != 4:
    print(False)
else:
    print(True)
    
my_number = '123-453-789'
my_number[8:] 
len(my_number[8:]) == 4
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() and len(my_number) != 12:
    print(False)
else:
    print(True)
    
if not my_number[0:3].isdigit():
    print(False)
elif my_number[3] != '-':
    print(False)
elif not my_number[4:7].isdigit():
    print(False)
elif my_number[7] != '-':
    print(False)
elif not  my_number[8:12].isdigit() or len(my_number) != 12:
    print(False)
else:
    print(True)
    
import re
re.search("\d\d\d-\d\d\d-\d\d\d\d",my_numbernumber)
re.search("\d\d\d-\d\d\d-\d\d\d\d",my_number)
my_number
my_number = '123-453-7891'
re.search("\d\d\d-\d\d\d-\d\d\d\d",my_number)
import re
re.search("\d\d\d-\d\d\d-\d\d\d\d",my_number)
my regex_obj = re.search("",my_number)
regex_pattern = "\d{3}"
my regex_obj = re.search(regex_pattern,my_number)
regex_obj = re.search(regex_pattern,my_number)
regex_obj
regex_pattern = "\d{3}-\d{3}-\d{4}"
regex_obj = re.search(regex_pattern,my_number)
regex_obj
my_number = '123-453-789'
re.search(regex_pattern,my_number)
regex_obj = re.search(regex_pattern,my_number)
print(regex_obj)
if regex_obj:
    return True
if regex_obj:
    print(True)
else:
    print(False)
    
my_number = '123-453-7891'
regex_obj = re.search(regex_pattern,my_number)
if regex_obj:
    print(True)
else:
    print(False)
    
regex_obj.start()
re.search("(-)\d{3}",my_number)
re.search("(-)(\d{3})(-)",my_number)
result = re.search("(-)(\d{3})(-)",my_number)
result.start()
my_number = '123-453-7891'
result.end()
my_number[8]
result.span()
#######
#######capture  group
result.group()
result.group(0)
result.group(1)
result.group(2)
result.group(3)
result.groups()
re.sub('(-)(d\{3})(-)', ";\\2;",my_number)
re.sub('(-)(d\{3})(-)', ";\\1;",my_number)
re.sub('(-)(\d{3})(-)', ";\\1;",my_number)
re.sub('(-)(\d{3})(-)', ";\\2;",my_number)
re.sub('(\d{2})/(\d{2})/(d{2})', "\\1 \\2 \\3",'01/31/22')
re.search('(\d{2})/(\d{2})/(d{2})', '01/31/22')
re.search('(\d{2})\/(\d{2})\/(d{2})', '01/31/22')
re.search('(\d{2})\/(\d{2})\/(\d{2})', '01/31/22')
re.sub('(\d{2})/(\d{2})/(\d{2})', "\\1 \\2 \\3",'01/31/22')
re.sub('(\d{2})/(\d{2})/(\d{2})', "\\2.\\1.\\3",'01/31/22')
re.findall('\d{2}',"123344")
re.sub('(-)(\d{3})(-)', "\\2",my_number)
'\1'
re.search('(\d{2})\/(\d{2})\/(\d{2})', '01/31/22')
re.search('(\d{2})\/(\d{2})\/(\d{2})', '01/31/22').group(1)
x = re.search('(\d{2})\/(\d{2})\/(\d{2})', '01/31/22').group(1)
x
x = re.sub('(\d{2})/(\d{2})/(\d{2})', "\\2.\\1.\\3",'01/31/22')
x
get_ipython().run_line_magic('save', '%current_session ~0/')
