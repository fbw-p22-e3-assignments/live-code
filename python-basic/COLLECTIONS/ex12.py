import re
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in sentence.lower():
            print(char)
            return False
    return True


sentence1 = "waltz, bad nymph, for quick jigs vex."
sentence2 = 'Glib jocks quiz nymph to vex dwarf.'
sentence3 = 'Sphinx of black quartz, judge my vow.'
sentence4 = 'How vexingly quick daft zebras jump!'
sentence5 = 'The five boxing wizards jump quickly.'
sentence6 = 'Jackdaws love my big sphinx of quartz.'
sentence7 = 'Pack my box with five dozen liquor jugs.'
sentence8 = 'The quick brown fox jumps over the lazy dog'


print(is_pangram(sentence1))
print(is_pangram(sentence2))
print(is_pangram(sentence3))
print(is_pangram(sentence4))
print(is_pangram(sentence5))
print(is_pangram(sentence6))
print(is_pangram(sentence7))
print(is_pangram(sentence8))