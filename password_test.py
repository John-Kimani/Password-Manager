import unittest #unitest module
from password import Credential #imports Credential class for testing
from password import User #imports User class for testing

class TestUser(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    Args:
        Testcase class taht helps create test cases for User
    '''
    # test to check if user object is instatiated properly
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_profile = User('Vernice','Hakuna Mipaka')
    
    def test__init(self):
        '''
        Test case to test if User object is instantiated correctly
        '''
        self.assertEqual(self.new_profile.userName, 'Vernice')
        self.assertEqual(self.new_profile.password, 'Hakuna Mipaka')


#end of class user test
#start of class credential test
class TestCredential(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    
    Args:
        Testcase class that helps create test cases for Credential
    '''

    #test to check if credential object is instantiated properly
    def setUp(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98') #sample login details for a new pintrest account 

    def test__init(self):
        '''
        Test case to test if credential object is instantiated correctly
        '''
        self.assertEqual(self.new_account.accountName, 'Pintrest')
        self.assertEqual(self.new_account.accountUsername,'kimperria')
        self.assertEqual(self.new_account.accountPassword,'Aura-Dev98')


    def test_save_account(self):
        '''
        Test case to check account object is saved into the contact list
        '''
        self.new_account.save_account()
        self.assertEqual(len(Credential.credentials_list),1)

    def tearDown(self):
        '''
        cleans up each credential list after instance
        '''
        Credential.credentials_list = []

    def test_save_multiple_contact(self):
        '''
        Test case to check if users can save multiple accounts
        '''
        self.new_account.save_account()
        test_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98')
        test_account.save_account()
        self.assertEqual(len(Credential.credentials_list),2)
    def test_delete_account(self):
        '''
        Test case to check if user can delete an account
        '''
        self.new_account.save_account()
        test_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98')
        test_account.save_account()

        self.new_account.delete_account() #deletes account object
        self.assertEqual(len(Credential.credentials_list),1)

    def test_find_account_by_username(self):
        '''
        Test case to check if we can find an account by username and display information
        '''
        self.new_account.save_account()
        test_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98')
        test_account.save_account()

        found_account = Credential.find_by_accountUsername('kimperria')
        self.assertEqual(found_account.accountUsername,test_account.accountUsername)

    def test_account_exist(self):
        '''
        Test case to check if a user account already exist returns a boolean
        '''
        self.new_account.save_account()
        test_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98')
        test_account.save_account()

        account_exists = Credential.account_exist('kimperria')
        self.assertTrue(account_exists)

    def test_display_all_accounts(self):
        '''
        Method that returns a list of all saved accounts
        '''

        self.assertEqual(Credential.display_accounts(),Credential.credentials_list)


#class condition
if __name__ == '__main__':
    unittest.main()