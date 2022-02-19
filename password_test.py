import unittest #unitest module
from password import Credential #imports Credential class for testing

class TestCredential(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    
    Args:
        Testcase class that helps create test cases
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


#class condition
if __name__ == '__main__':
    unittest.main()