# palyndrome
# ex : 'malam' is palyndrome with 'malam'

def is_palyndrome(word):
    test_case = ''
    itr  = len(word)
    while itr > 0:
        test_case+=str(word[itr-1])
        itr-=1
    
    if word == test_case:
        return True
    else:
        return False
    
def main():
    words = str(input('enter a word : '))
    if is_palyndrome(words):
        print('{} is a palyndrome'.format(words))
    else:
        print('{} is not a palyndrome'.format(words))



if __name__ == '__main__':
    main()

