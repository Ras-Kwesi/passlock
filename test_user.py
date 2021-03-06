import unittest
from user import User


class TestUser(unittest.TestCase):
    '''Test class that defines test cases/procedure
     for the user class cases'''

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.lockusers = []


    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("Kwesi","Makonnen","0712345678","kwest@a.com") # create contact test object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Kwesi")
        self.assertEqual(self.new_user.last_name,"Makonnen")
        self.assertEqual(self.new_user.password,"0712345678")
        self.assertEqual(self.new_user.email,"kwest@a.com")



    def test_save_users(self):
        """
        test if users are added to the list upon login
        """

        self.new_user.save_user()
        self.assertEqual(len(User.lockusers),1)

    def test_delete_users(self):
        '''
        Test to see if remove function works
        '''

        self.new_user.save_user()
        userexample = User("Kwei","Makonen","072345678","kwst@a.com")
        userexample.save_user()
        self.assertEqual(len(User.lockusers),2)

        self.new_user.delete_user()
        self.assertEqual(len(User.lockusers),1)







if __name__ == '__main__':
    unittest.main()