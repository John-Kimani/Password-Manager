class User:
    '''
    This class helps generate instances for creating a new account on this appliation
    '''



## generate credentials instances
class Credential:
    '''
    This class helps generate instances for new and or existing online accounts log in credentials
    '''

    credentials_list = [] # empty list that will hold online accounts log in details

    def __init__(self, accountName, accountUsername, accountPassword):
        '''
        This function helps define properties of new and or existing accounts objects.
        Args:
            accountName: brand name of user online account. For example; 'pintrest'
            accountUsername: user username of a specified online account.
            accountPassword: user password for an online account.
        '''

        self.accountName = accountName
        self.accountUsername = accountUsername
        self.accountPassword = accountPassword

    # save account function
    def save_account(self):
        '''
        save_account method saves account log in credentials object into credential_list
        '''
        Credential.credentials_list.append(self)

    #delete account function
    def delete_account(self):
        '''
        delete_account method deletes a saved account from credential_list
        '''
        Credential.credentials_list.remove(self)

    @classmethod
    def find_by_accountUsername(cls, accountUsername):
        '''
        Method that takes in accountUsername and returns an account that matches that accountUsername
        Args:
            accountUsername: User username to search for
        Returns:
            account of person that matches accountUsername
        '''
        for account in cls.credentials_list:
            if account.accountUsername == accountUsername:
                return account

