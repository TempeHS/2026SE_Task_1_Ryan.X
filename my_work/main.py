def main():
    menu = input('What would you like to do: ').lower().strip()
    print('Login, register, quit')
    match menu:
        case 'login':
            login = input('What is your login')
        case 'register':
            register = input('(Username) (password): ')
        case 'quit':
            print('End Program')
        case 'change password':
            passchange = input('What is your new password: ')
        case 'logout':
            logout = print('user is logged out')




def login():
    while True:
        import csv

        accounts = []
        
        with open('plain_text.txt') as file:
            reader = csv.DictReader(file)
            for row in reader:





def register():
        import csv
        
        username = input('What is your username: ')
        password = input('What is your password')

        with open('plain_text.txt', 'a') as file:
            writer = csv.DictWriter(file, fieldnames =['username', 'password'])
            writer.writerow({'username': username, 'password': password})




def menu2(login):
    if login is True:







main()






            #for line in file:
                #username, password = line.rstrip(), split(',')
                #username = {'username': username, 'password': password}
                #user.append(username)