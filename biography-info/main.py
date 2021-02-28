# biography info


def get_biography_info(usr_info):
    print('getting user info')
    for usr in usr_info:
        print('- {} : {}'.format(usr, usr_info[usr]))

def set_biography_info():
    user_info = dict()
    user_credentials = ('Name', 'Date of Birth', 'Address', 'Personal goals')
    for credential in user_credentials:
        user_info[credential] = str(input('{} : '.format(str(credential))))
    
    print('record has been saved!')
    return user_info



def main():
    user_info = set_biography_info()
    get_biography_info(user_info)



if __name__ == '__main__':
    main()







