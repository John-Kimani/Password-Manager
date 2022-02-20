class User:
    '''
    This class helps generate instances for creating a new account on this appliation
    '''

    def __init__(self, userName, password):
        '''
        This function helps define properties to create a PASSWORD-MANAGER account.
        Args: 
            userName: user's username
            password: user's password
        '''
        self.userName = userName
        self.password = password



# end of users instance
#starts of accounts credentials
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

    @classmethod
    def account_exist(cls, accountUsername):
        '''
        Method that check if an account already exists from the credential list
        Args: 
            accountUsername to search if account exist
        Returns: 
            True or false depending id the account exists
        '''

        for account in cls.credentials_list:
            if account.accountUsername == accountUsername:
                return True
            return False

    @classmethod
    def display_accounts(cls):
        '''
        Method that retuns items in credential list
        '''
        return cls.credentials_list


