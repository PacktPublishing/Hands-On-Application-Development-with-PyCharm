def change_middle(my_list):
    print('Start function')
    x = int(input('Enter a number: '))
    my_list[1] = x
    print('End function')


if __name__ == '__main__':
    a = [0, 1, 2]
    b = a

    change_middle(a)

    print(a)
    print(b)
