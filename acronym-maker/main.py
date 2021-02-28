# acronym maker

def get_acronym(word):
    _acronym = ''
    split_w = word.split(' ')
    for split in split_w:
        _acronym+=str(split[0].upper())
    
    print(_acronym)

def main():
    words = str(input('Enter words : '))
    get_acronym(words)



if __name__ == '__main__':
    main()


