#!/usr/bin/env python3.6
from password import Credential
from password import User

def create_profile(username, password):
    '''
    Function to create a new user profile
    '''
    new_profile = User(username, password)
    return new_profile

def save_profile(profile):
    '''
    Function to save user profile
    '''
    profile.save_profile()


## user class code above
## credential class code below
def create_account(accountName, accountUsername, accountPassword):
    '''
    Function to creates a new account
    '''
    new_account = Credential(accountName, accountUsername, accountPassword)
    return new_account

def save_account(account):
    '''
    Function to save account
    '''
    account.save_account()

def find_account(accountUsername):
    '''
    Function that find an account by username and return the account
    '''
    return Credential.find_by_accountUsername(accountUsername)

def check_existing_account(accountUsername):
    '''
    Function that return all the saved account
    '''
    return Credential.account_exist(accountUsername)

def display_accounts():
    '''
    Function that returns all saved accounts
    '''
    return Credential.display_accounts()

def delete_account(accountName):
    '''
    Function that deletes an account
    '''
    return Credential.delete_account(accountName)

def main():
    print("Hello, Welcome to Password-Manager. We are your onestop online password wallet.")

    print('\n')

    while True:
        print('sign up or log in')
        print('Use this short codes: su - create new profile, li - log in')
        start = input()
        if start == 'su':
            print('Please enter your first name')
            first_name = input()
            print('Please enter your last name')
            last_name = input()
            print('Please enter your preferred username')
            username = input()
            print('Enter password')
            password = input()
            print('Please confirm password')
            password = input()
            print('Profile created succesfully')
        elif start == 'li':
            print('Please enter your profile username')
            username = input()
            print('Enter Password')
            password = input()
            print('You are now logged in')
        else:
            print('Kindly use the codes mentioned above')

        print(f'Hello {{username}}. What would you like to do?')
        print("Use these short codes: ca - create a new account, da - display your saved accounts, fa - find an account, dlt - delete a credential account ex - exit the account log in account credential list")
        
        short_code = input().lower() #sets a variable to store short codes navigating this app

        #create account condition
        if short_code == 'ca':
            print('New account')
            print('-'*10)

            print("Account Brand name e.g: 'Pintrest' ... ")
            accountName = input()

            print('Your account username ...')
            accountUsername = input()

            print('Key in Password ...')
            accountPassword = input()

            save_account(create_account(accountName, accountUsername, accountPassword))# creates and save new account

            print('\n')
            print(f"New {accountName} account  with username {accountUsername} has been created successfully")
            print('\n')

            #display account
        elif short_code == 'da':

            if display_accounts():
                print("Here is alist of all your saved account log in credentials")
                print('\n')

                for account in display_accounts():
                    print(f"{account.accountName} {account.accountUsername}")
                    print('\n')
            else:
                print('\n')
                print("You dont seem to have any accounts saved yet")
                print('\n')
                # find account
        elif short_code == 'fa':
            print('Enter the username you want to search for')
            search_accountUsername = input()
            if check_existing_account(search_accountUsername):
                search_account = find_account(search_accountUsername)
                print(f"{search_account.accountName} {search_account.accountUsername} {search_account.accountPassword}")
                print('-'*20)

                print(f"Account name: {search_account.accountName}")
                print(f"Account username: {search_account.accountUsername}")
            else:
                print("That account does not exist")

            # delete account
        elif short_code == 'dlt':
            print('Enter the account username you want to delete')
            accountUsername = input()
            if find_account(accountUsername):
                delete_account(find_account(accountUsername))
                print(f'{accountUsername} has been deleted')
            else:
                print('The account does not exist')

        #exit app
        elif short_code == 'ex':
            print('Thank you for considering our service. Goodbye for now see you later!')
            break
        else:
            print('I really didnt get that. Please use the short codes')



if __name__ == '__main__':
    main()

