# odd or even
# python junior challenge

def is_even(num):
    if num % 2 == 1:
        return False
    else:
        return True


def greet_user():
    print('hi user!')
    num = int(input('what are you thinking?: '))
    _res = is_even(num)
    if (_res):
        print('that\'s an even number! Have another?')
    else:
        print('that\'s an odd  number! Have another?')


def main():
    greet_user()


if __name__ == '__main__':
    main()






