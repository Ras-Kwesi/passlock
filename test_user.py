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
        self.new_user = User("Kwesi","Makonnen","0712345678","kwest@a.com") # create contact object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.first_name,"Kwesi")
        self.assertEqual(self.new_user.last_name,"Makonnen")
        self.assertEqual(self.new_user.password,"0712345678")
        self.assertEqual(self.new_user.email,"kwest@a.com")




if __name__ == '__main__':
    unittest.main()