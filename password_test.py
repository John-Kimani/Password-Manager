import unittest #unitest module
from password import Credential #imports Credential class for testing

class TestCredential(unittest.TestCase):
    '''
    Test class that helps define test cases for the credentials class behaviours
    
    Args:
        Testcase class that helps create test cases
    '''

    #test to check if credential object is instantiated properly
    def setup(self):
        '''
        Set up method to run before each test case.
        '''
        self.new_account = Credential('Pintrest', 'kimperria', 'Aura-Dev98') #sample login details for a new pintrest account 
    
    def test__init__(self):
        '''
        Test case to test if credential object is instantiated correctly
        '''
        self.assertEqual(self.new_account.accountName, 'Pintrest')
        self.assertEqual(self.new_account.accountUsername,'kimperria')
        self.assertEqual(self.new_account.accountPassword,'Aura-Dev98')


#class condition
if __name__ == '__main__':
    unittest.main()