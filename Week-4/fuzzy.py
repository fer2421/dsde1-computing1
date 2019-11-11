'''
fuzzy.py

Lint this file using PyLint.
'''

# This function does some maths on three numbers.
def maths(input_a, input_b, input_c):
    '''This function does some maths on three numbers.'''
    result = input_a * 3 - input_b + input_c
    return result

# This function returns True or False.
def choices(question):
    '''This function returns True or False.'''
    return bool(question)

def main():
    '''first function takes three numbers and second function takes a True or False.'''
    answer = maths(3, 9, 2.3)
    # first function takes three numbers
    answer = maths(3, 9, 2.3)
    print(answer)

    # second function takes a True or False
    NewAnswer = choices(True)
    print(NewAnswer)

if __name__ == '__main__':
    main()
