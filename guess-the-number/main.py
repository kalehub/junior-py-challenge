# guess the number
import random

def is_correct(num, mi, ma, usr):
    # isinstance -> to check the type in condition
    if isinstance(usr, int):
        if usr < mi or usr > ma:
            print('invalid range')
        elif num == usr:
            print('correct!')
        else:
            print('wrong number. the correct number is {}'.format(num))
    else:
        print('integer number only!')



def main():
    _min, _max = 1, 50
    val = random.randint(_min, _max)
    usr_guess = int(input('Enter your guesses : '))
    is_correct(val, _min, _max, usr_guess)


if __name__ == '__main__':
    main()

