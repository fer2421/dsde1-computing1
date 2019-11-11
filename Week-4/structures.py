'''
structures.py
Simple functions performing operations on basic Python data structures.
'''

# Lists

# write a function that returns a list containig the first and the last element
# of "the_list".
def first_and_last(the_list):
    new_list = [the_list[0], the_list[-1]]
    return new_list


# write a function that returns part of "the_list" between indices given by the
# second and third parameter, respectively. The returned part should be in
# reverse order than in the original "the_list".
# If "end" is greater than "beginning" or any of the indices is out of the
# list, raise a "ValueError" exception.
def part_reverse(the_list, beginning, end):
    if (beginning > end) or (end > len(the_list)):
        raise ValueError
    else:
        reverse_list = the_list[beginning: end]
        reverse_list.reverse()
        return reverse_list


# write a function that at the "index" of "the_list" inserts twice the
# same value. For example if the_list = [0,1,2,3,4] and index = 3 the function
# will return [0,1,2,3,3,3,4].
def repeat_at_index(the_list, index):
    i = 0
    while i < 2:
        the_list.insert(index, the_list[index])
        i += 1
    return the_list

# Strings

# write a function that checks whether the word is a palindrome, i.e. it reads
# the same forward and backwards
def palindrome_word(word):
    import copy
    word = word.lower()
    list_word = list(word)
    word_rev = copy.copy(list_word)
    word_rev.reverse()
    return list_word == word_rev

# write a function that checks whether the sentence is a palindrome, i.e. it
# read the same forward and backward. Ignore all spaces and other characters
# like fullstops, commas, etc. Also do not consider whether the letter is
# capital or not.
def palindrome_sentence(sentence):
    import copy
    s = sentence.replace(',', '')
    s = s.replace('.', '')
    s = s.replace(' ', '')
    s = s.lower()
    list_sentence = list(s)
    rev_sentence = copy.copy(list_sentence)
    rev_sentence.reverse()
    return list_sentence == rev_sentence


# write a function that concatenates two sentences. First the function checks
# whether the sentence meets the following criteria: it starts with a capital
# letter and it ends with a full stop, question mark, or an exclamation point.
# Keep in mind, that the sentence might have whitespace at the beginning or at
# the end.  The concatenated sentence must have no white space at the beginning
# or at the end and the must be exactly one space after the end of the first
# sentence.
def concatenate_sentences(sentence1, sentence2):
    import copy
    cap_sentence1 = copy.copy(sentence1.strip())
    cap_sentence2 = copy.copy(sentence2.strip())
    a = cap_sentence1.capitalize() == sentence1.strip()
    b = cap_sentence2.capitalize() == sentence2.strip()
    end = ['.', '?', '!']
    end_1 = sentence1[-1]
    end_2 = sentence2[-1]
    if a == True and b == True and end_1 in end and end_2 in end:
        return sentence1.strip() + ' ' + sentence2.strip()

# Dictionaries

# write a function that checks whether there is a record with given key in the
# dictionary. Return True or False.
def index_exists(dictionary, key):
    return key in dictionary.keys()

# write a function which checks whether given value is stored in the
# dictionary. Return True or False.
def value_exists(dictionary, value):
    return value in dictionary.values()

# write a function that returns a new dictionary which contains all the values
# from dictionary1 and dictionary2.
def merge_dictionaries(dictionary1, dictionary2):
    d1_keys = list(dictionary1.keys())
    d2_keys = list(dictionary2.keys())
    d1_values = list(dictionary1.values())
    d2_values = list(dictionary2.values())
    new_keys = d1_keys + d2_keys
    new_values = d1_values + d2_values
    new_dictionary = {}
    for i in range(len(new_keys)):
        new_dictionary[new_keys[i]] = new_values[i]
    return new_dictionary
