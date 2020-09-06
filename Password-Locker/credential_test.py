import unittest
from credentials import Credentials
from user import User

class TestCredentials(unittest.TestCase):

    '''
    Test class that defines test cases for the credentials class behaviours.
    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_credential = Credentials("jose", "45678")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        
        self.assertEqual(self.new_credential.account_name, "jose")
        self.assertEqual(self.new_credential.password, "45678")

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        ''' 
        Credentials.credential_list = []
    
    def test_save_credential(self):
        '''
        test_save_user test case to test if a new user is saved into the credential_list
        '''
        self.new_credential.save_credential()
        self. assertEqual(len(Credentials.credential_list),1)    

    def test_save_multiple_credential(self):
        '''
        test_save_multiple_credential to check if we can save multiple credential objects to our credential_list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("jose","45678")
        test_credential.save_credential()
        self.assertEqual(len(Credentials.credential_list),2)

    def test_delete_credentials(self):
        '''
        test_delete_credential to test if we can remove a  credential from our credential list
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("jehnny","7543")
        test_credential.save_credential()
        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)

    def test_find_credential_by_account_name(self):
        '''
        Test to check if we can find a user by their username and display their details"
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("igna", "bruse")
        test_credential.save_credential()

        find_credential = Credentials.find_by_account_name("igna")

        self.assertEqual(find_credential.password, test_credential.password)
    def test_credential_exists(self):
        '''
        test to check if we can return a boolean if we can not find the user.
        '''
        self.new_credential.save_credential()
        test_credential = Credentials("challo","dee")
        test_credential.save_credential()

        credential_exists = Credentials.credential_exist("challo")
        self.assertTrue(credential_exists)   

if __name__ == '__main__':
    unittest.main()    
