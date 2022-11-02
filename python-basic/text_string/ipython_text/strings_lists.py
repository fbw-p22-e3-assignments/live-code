# coding: utf-8
x =1
id(x)
import ctypes
ctypes.cast(140110900472112, ctypes.py_object).value
list1 = [1,2,3]
id(list1)
ctypes.cast(140110850594688, ctypes.py_object).value
list1[0]
id(list1[0])
list[1:2]
list1[1:2]
list2 = [1,2,3,4,5,6]
list1[1:2:1]
list[1:2:1]
list2
list2[1:4]
list2 = ['a', 'b', 'c', 'd', 'e']
list2[1:4]
list2[0:5]
id(list2)
id(list2[0:5])
list2[:]
id(list2[:])
y = x
y is x
y = 2
y is x
x = 2
y is x
list2
list3 = list2.copy
list2
list3
list3 = list2.copy()
list3
list2 is list3
list2 = list3
list2 is list3
list2 == list3
list3 = list2.copy()
list2 == list3
list2 is list3
list3[0] = 'a'
list2 == list3
list3
list3[0] = '1'
list2 == list3
list[0]
list1[0]
list3[2]
list3[-1]
list[0:5]
list3[0:5]
list3[0:5:2]
list3[0:5:-1]
list3[5:0:-1]
list3[5:0]
list3[5:0:-1]
list3[4:-1:-1]
list3[4]
list3[4:0:-1]
list3[4::-1]
list3[-1:0:-1]
list3
list[:]
list3[:]
list3[1:4:1]
list3[0:4:1]
list3[0:5:1]
list3[:]
list3[4::-1]
list3[4:0:-1]
list3[5:0:-1]
list3[6:0:-1]
list3[0:6]
list3[4:-6:-1]
list3[-6]
list3[-5]
list3
list3[0] = 'a'
list3[-1:-6:-1]
list3
list3[4:0]
list3[4:0:-1]
list3[0:4]
list3[0:-1]
list3[0:5]
list3[0:6]
list3[:]
list3[1:4]
list3[-4:-1]
list3[1:-1]
list3[-2:-5:-1]
list3[-2:0:-1]
list3[3:0:-1]
list3
'a' in list3
1 in list3
string1 = 'Hello World'
id(string1)
string1 = 'Hello World1'
id(string1)
string1[0]
string1[0:5]
string1[5]
string1[6:11]
string1[0:4]
string1[0:]
string1[0:3]
string1[0:4]
string1[-5:-1]
string1[-8:-11]
string1[-8]
string1[-7]
string1
string1= 'Hello World'
string1[-7]
string[-5]
string[-5:-1]
string1[-5:-1]
string1[-5:-1:-1]
string1[-5:-1:1]
string1[-7:-12:-1]
string1[-11:-7:1]
string1[-11:-7]
string1[-1:-12:-1]
string1[:-12:-1]
string1[::-1]
type(string1)
type(string1[0])
string1.casefold()
string1.lower()
string1.isalpha()
string1
string1.isalpha()
'12'.isalpha()
'a'.isalpha()
' '.isalpha()
string1.lower()
string2 = string1.lower()
string2
string2.capitalize()
string2 = string1.upper()
string2
string2.casefold()
string3 = 'straße'
string3.casefold()
string3.lower()
string3.title()
string.title()
string2.title()
string2.capitalize()
string2.upper()
string2.count('l')
string2
string2.count('L')
string2.find('L')
string2.index('L')
string2.find('ß')
string2.index('ß')
string2.split('L')
string = 'bla, 1, City'
string.split(',')
string = 'bla; 1; City'
string.split(';')
list(string)
" bla \"bib\" "
"  Hello   ".trim
"  Hello   ".strip()
"  Hello   ".rstrip()
"  Hello   ".lstrip()
"{}1. {}2.".format(1,2,3)
"{}1. {}2.".format('hello','world')
"{b}1. {a}2.".format(a='hello',b='world')
f"{string} bla"
"%d" %1
"%d" %'a'
"%s" %'a'
"%d" %1.1
"%f" %1.1
"%f" %(1+1j)
"%c" %(1+1j)
"%.2f" % 1.777777
str(1+1j)
"%s" % str(1+1j)
"%c" % 1
"%c" % a
"%c" % 'a'
"%c" % 'al'
"%d" %1.1
"%d %s" % (1, 'bla')
from string import Template
Template('${noun}ification').substitute(noun='Ident')
list1
list1[len(list1)]
list1[len(list1)-1]
myData = [1, 2, 1, 2, 1]
myData[1:4]
my_string = 'Hello world'
my_substring = my_string[:5]
my_reversed_substring = my_substring[::-1]
print(my_reversed_substring)
get_ipython().run_line_magic('clear', '()')
ext
