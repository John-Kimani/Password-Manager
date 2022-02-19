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