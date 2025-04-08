def main():
    menu = input('What would you like to do (Login, Register, Quit): ').lower().strip()
    while True:
        match menu:
            case 'login':
                username = input('What is your username: ')
            case 'register':
                register = input('(Username) (password): ')
            case 'quit':
                print('End Program')
            case 'change password':
                passchange = input('What is your new password: ')
            case 'logout':
                logout = print('user is logged out')




def login():
    global account = (username, password)
    
    while True:
        match username:
            case 'sithLord Ancient' | 'd_Vader' | 'GENERALleia' | 'grogu' | 'there_is_no_try' | 'MyRey' | 'Luke':
                password = input('What is your password')
                break
            case _:
                print('username not found, try again: ')
        
    match password:
        case 'Ancient enimes r us' | "I'm Your Father" | 'May the Force be with you' | 'patu' | 'Yoda' | 'I Am All The Jedi' | 'May the Force be with you':
            menu2 = input('Login Succesful, Change password?, Logout?')
        case _:
            print('Login unsuccessful')




accounts = [{'username':'sithLord', 'password':'Ancient enimes r us' } {'username':'d_Vader' , 'password':"I'm Your Father"  } {'username':'GENERALleia' , 'password':'May the Force be with you'  } {'username':'grogu', 'password':'patu'  } {'username':'there_is_no_try' , 'password':'Yoda'  } {'username':'MyRey' , 'password':'I Am All The Jedi'  } {'username':'Luke', 'password': 'May the Force be with you'  }]



]






    #while True:
    #    import csv
#
        #accounts = []
        
        #with open('plain_text.txt') as file:
        #    reader = csv.DictReader(file)
        #    for row in reader:





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






