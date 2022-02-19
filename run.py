#!/usr/bin/env python3.6

from dis import show_code
from password import Credential

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
    Function that retur all the saved account
    '''
    return Credential.account_exist(accountUsername)

def display_accounts():
    '''
    Function that returns all saved accounts
    '''
    return Credential.display_accounts()

def main():
    print("Hello, Welcome to Password-Manager. We are your onestop online password wallet.")

    print(f'Hello {{username}}. What would you like to do?')
    print('\n')

    while True:
        print("Use these short codes: ca - create a new account, da - display your saved accounts, fa - find an account, ex - exit the account log in account credential list")
        
        short_code = input().lower() #sets a variable to store short codes navigating this app

        #create account condition
        if short_code == 'ca':
            print('New account')
            print('-'*10)

            print("Account Brand name e.g: 'Pintrest' ... ")
            accountName = input()

            print('Your account username ...')
            accountUsername = input()

            print('Keyin Password ...')
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
    #exit app
        elif short_code == 'ex':
            print('Thank you for considering our service. Goodbye for now see you later!')
            break
        else:
            print('I really didnt get that. Please use the short codes')



if __name__ == '__main__':
    main()

