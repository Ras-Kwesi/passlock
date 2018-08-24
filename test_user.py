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