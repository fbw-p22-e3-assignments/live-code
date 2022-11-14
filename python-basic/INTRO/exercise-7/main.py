import sys

arguments = sys.argv[1:]

print(sys.argv[1:])
print(arguments)


if '--help' in arguments:
    print('help')
if '--fast' in arguments:
    print('fast mode enabled')