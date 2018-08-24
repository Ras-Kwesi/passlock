import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Test case method in unittest class that takes
    instances for tests
    """

    def tearDown(self):
        '''
        Clears our dictionary to create a new test instance
        '''

        Credentials.credentials_dict = {}


    def setUp(self):
        """
        set up a new instance of a test class for us to do a trial with
        """

        self.new_credential = Credentials.credentials_dict["Account"] = "Password"
        self.new_credential = Credentials.credentials_dict["Acount"] = "Pasword"
        self.new_credential = Credentials.credentials_dict["Twitter"] = "2E22a"


    def test_init(self):
        """
        test for initiation of a new instance of the credential class
        """

        self.assertEqual(self.new_credential ,"2E22a")
        # self.assertEqual(self.new_credential,"2E22a")


    def test_save_credential(self):
        """
        Test if our dredentials are in the dictionary
        """

        self.assertEqual(len(Credentials.credentials_dict),3)


if __name__ == '__main__':
    unittest.main()