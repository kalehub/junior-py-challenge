# word count challenge


def count_words(words):
    word = words.split(' ')
    # print(word)
    return len(word)



def main():
    _words = str(input('what\'s on your mind today? : '))
    num_of_words = count_words(_words)
    print('oh nice you just told me what\'s on your mind in {} words!'.format(num_of_words))




if __name__ == '__main__':
    main()








