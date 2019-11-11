'''
keywords.py

Create functions that use keyword arguments
with default values.
'''

# Create a function called welcome_message():
# if no input argument is provided
# it returns the string 'Hello and welcome'
# if a keyword argument called user_name is provided
# it returns 'Hello, <user_name>, and welcome'
# if a keyword argument called place is provided
# it returns 'Hello and welcome to <place>'
# if both user_name and place are provided
# it returns 'Hello, <user_name>, and welcome to <place>

def welcome_message(user_name=None, place=None):
    if user_name != None and place != None:
        output = ('Hello, {}, and welcome to {}'.format(user_name, place))
    elif user_name != None:
        output = ('Hello, {}, and welcome'.format(user_name))
    elif place != None:
        output = ('Hello and welcome to {}'.format(place))
    else:
        output = 'Hello and welcome'
    return output


# Create a function called list_average()
# without using any libraries to do the maths for you
# (the point of this exercise is to practice interacting
# with lists)
# the first argument is a list of numbers
# the second optional keyword arguemt is called avg_type
# if nothing for avg_type provided, return the mean of the list
# if avg_type='mode', return the mode of the list 
# (return list of all modes if there is a tie between multiple values)
# if avg_type='mean', return the mean of the list
# if avg_type='median', return the median of this list

def list_average(input_list, avg_type='mean'):
    if avg_type == 'mean':
        if input_list == []:
            return 0
        else:
            return sum(input_list) / len(input_list)
    elif avg_type == 'mode':
        if input_list == []:
            mode_list = []
        else:
            dict = {}
            for n in input_list:
                keys = dict.keys()
                if n in keys:
                    dict[n] += 1
                else:
                    dict[n] = 1
            max_value = max(dict.values())
            mode_list = [i for i, v in dict.items() if v == max_value]
        return mode_list
    elif avg_type == 'median':
        input_list.sort()
        if input_list == []:
            return None
        elif len(input_list) % 2 != 0:
            median_index = len(input_list) // 2
        else:
            median_index = (len(input_list) // 2) + 1
        return input_list[median_index]
