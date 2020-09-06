import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user and credentials class behaviours.
    Args: 
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Setup method to run before each test case
        '''
        self.new_user = User("Mykey", "Bruno", "Sandra", "4567")

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''
        self.assertEqual(self.new_user.first_name,"Mykey")
        self.assertEqual(self.new_user.last_name,"Bruno")
        self.assertEqual(self.new_user.user_name, "Sandra")
        self.assertEqual(self.new_user.password, "09876")

    def tearDown(self):
        '''
        tearDown method that does the clean up after each test case has run.
        ''' 
        User.user_list = []
    
    def test_save_user(self):
        '''
        test_save_user test case to test if a new user is saved into the user_list
        '''
        self.new_user.save_user()
        self. assertEqual(len(User.user_list),1)    

    def test_save_multiple_user(self):
        '''
        test_save_multiple_user to check if we can save multiple user objects to our user_list
        '''
        self.new_user.save_user()
        test_user = User("Test","user","12345","test@user.com")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)

    def test_delete_user(self):
        '''
        test_delete_user to test if we can remove a user from our user list
        '''
        self.new_user.save_user()
        test_user = User("Mykey","Bruno","Sandra","45678")
        test_user.save_user()
        self.new_user.delete_user()    
        self.assertEqual(len(User.user_list),1)

    def test_find_user_by_user_name(self):
        '''
        Test to check if we can find a user by their username and display their details"
        '''
        self.new_user.save_user()
        test_user = User("Sandra", "Yvvy", "Shanice", "Nicky")
        test_user.save_user()

        find_user = User.find_by_user_name("Yvvy")

        self.assertEqual(find_user.password, test_user.password)
    def test_user_exists(self):
        '''
        test to check if we can return a boolean if we can not find the user.
        '''
        self.new_user.save_user()
        test_user = User("Charlo","Shash","Igna","Joe")
        test_user.save_user()

        user_exists = User.user_exist("Charlo")
        self.assertTrue(user_exists)  

        #!/usr/bin/env python3.8

if __name__ == '__main__':
    unittest.main()    
