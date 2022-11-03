# coding: utf-8
import re
re.search('0*(\w+)\.*(\w+)',"hello world")
re.search('0*(\[^.]+)\.*(\w+)',"hello world")
re.search('0*(\[^\.]+)\.*(\w+)',"hello world")
re.search('0*(.+)\.*(\w+)',"hello world")
re.search('0*(.+)(\.*\w+)',"hello world")
re.search('0*(.+)(\.*\w+)0*',"hello world")
re.search('^0*(\\d+\\.\\d*?[1-9])0*$',"hello world")
re.search('^0*(\\d+\\.\\d*?[1-9])0*$',"0023.07623070")
re.search('0*(\w+)(\\.\d+)',"0023.07623070")
re.search('0*(\w+)(\\.\d+)',"0023.07623070").groups
re.search('0*(\w+)(\\.\d+)',"0023.07623070").groups()
re.search('0*([\w\s]+)(\\.\d+)',"0023.07623070").groups()
re.search('0*([\w\s]+)(\\.\d+)',"hello world").groups()
re.search('0*([\w\s]+)(\\.\d+)',"hello world")
re.search('0*([\w\s]+)(\\.\d+)0*',"hello world")
re.search('0*([\w\s]+)(\\.\d*?)0*',"hello world")
re.search('0*([\w\s]*)(\\.\d*?)0*',"hello world")
re.search('0*([\w\s]*)',"hello world")
re.search('0*([\w\s]*)(\\.?\d*?)0*',"hello world")
re.search('0*([\w\s]*)(\\.?\d*?)0*',"hello world").groups()
re.search('0*([\w\s]*)(\\.?\d*?)0*',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)0*',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)(?=0*)',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)(?=0+)',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)(?=0+)',"hello world").groups()
re.search('0*([\w\s]*)(\\.?\d*)(0$)',"hello world").groups()
re.search('0*([\w\s]*)(\\.?\d*)(0*$)',"hello world").groups()
re.search('0*([\w\s]*)(\\.?\d*)(0*$)',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)0',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)0+',"0023.07623070").groups()
re.search('0*([\w\s]*)(\\.?\d*)0*',"0023.07623070").groups()
re.search('(.+)',"0023.07623070").groups()
re.search('(.+)(\\.([1-9])',"0023.07623070").groups()
re.search('(.+)(\\.([1-9])',"0023.07623070")
re.search('(.+)(\\.([1-9]))',"0023.07623070")
re.search('(.+)(\\.([1-9]*))',"0023.07623070")
re.search('(.+)(\\.(0*[1-9]*))',"0023.07623070")
re.search('(.+)(\\.(0*[1-9]*)*)',"0023.07623070")
re.search('(.+)(\\.(0*[1-9]+)*)',"0023.07623070")
re.search('(.+)(.+)(\\.(0*[1-9]+)*)',"0023.07623070")
re.search('(.+)(.+)(\\.(0*[1-9]+)*)',"0023.07623070").groups()
re.search('0(.+)(\\.(0*[1-9]+)*)',"0023.07623070").groups()
re.search('0*(.+)(\\.(0*[1-9]+)*)',"0023.07623070").groups()
re.search('0*(.*)(\\.(0*[1-9]+)*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.(0*[1-9]+)*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.(0*[1-9]+)*)(0*)',"hello world").groups()
re.search('^0*(.*)(\\.(0*[1-9]*)*)(0*)',"hello world").groups()
re.search('^0*(.*)(\\.*(0*[1-9]*)*)(0*)',"hello world").groups()
re.search('^0*(.*)(\\.*(0*[1-9]*)*)(0*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.*(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(.*)(\\.*(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(.*)((\\.*)(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(\w*)((\\.*)(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*(\w*)((\\.*)(0*[1-9]+)*)(0*)',"hello world").groups()
re.search('^0*([\w\s]*)((\\.*)(0*[1-9]+)*)(0*)',"hello world").groups()
re.search('^0*([\w\s]*)((\\.*)(0*[1-9]+)*)(0*)',"0023.07623070").groups()
re.search('^0*([\w\s]*)((\\.*)(0*[1-9]+)*)0*',"0023.07623070").groups()
re.search('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*',"0023.07623070").groups()
re.search('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*',"hello world").groups()
re.search('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*',"0023.07623070").groups()
re.sub('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*', '\\1\\2' , "0023.07623070")
re.sub('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*', '\\1\\2' , "hello world")
re.sub('^0*([\w\s]*)(\\.*(0*[1-9]+)*)0*', '\\1\\2' , "01230")
get_ipython().run_line_magic('save', '%current_session ~0/')
get_ipython().run_line_magic('save', '%current_session ~0/')
