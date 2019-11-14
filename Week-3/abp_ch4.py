def listing(list_1):
    for i in list_1[:-1]:
        i += ', '
        print(i, end = '')
    print('and ' + list_1[-1])
       
list_1 = ['cat', 'dog', 'Tim', 'Khai', 'Fernanda']
listing(list_1)