
def pig_latin_inner(wordList, **kwargs):
    """
    Takes a list of strings as first required positional
    argument and settings/(kwargs) as keyword argument
    returns a string
    """
    result = []
    for string in wordList: # iterate over each word of the wordList
        if string[0].lower() in 'aeoui':#check if word starts with a vowel 
            result.append(f"{string}{kwargs['suffix']}")#change word
        else: # slice from second character until the last and concatenate
            result.append(f"{string[1:] + string[0] + kwargs['suffix']}".capitalize())
    return " ".join(result) # join all words of the list result

        
def pig_latin(wordList, suffix='ay', single=False):
    """
    Take a list of strings as first required positional
    argument and settings as keyword arguments
    """
    default = {'suffix': suffix, 'single': single} #define default settings
    results = []
    for ele in wordList: #iterate over all elements of the wordList 
        words_split = ele.split(' ') #split each elements into a list
        #pass the split_word list to our inner function and 
        #append the return value to the results list 
        results.append(pig_latin_inner(words_split, **default))
    if default['single']:
        return ' '.join(results)
    return results
    

# Test cases

test1_data = ["Word", "Apple"]
test1_config = {}
test2_data = ["Python", "Functions"]
test2_config = {"suffix": "oi"}
test3_data = ["If the word starts with a vowel", "add the suffix to the word"]
test3_config = {"single": True, "suffix": "ep"}

print(pig_latin(test1_data, **test1_config))
print(pig_latin(test2_data, **test2_config))
print(pig_latin(test3_data, **test3_config))