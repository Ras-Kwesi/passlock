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

        Credentials.credentials_list = []
        #Credentials.credentials_list = {}


    def setUp(self):
        """
        set up a new instance of a test class for us to do a trial with
        """

        self.new_credential = Credentials("Account","Password")


        '''
    def setUp(self):
        """
        set up a new instance of a test class for us to do a trial with
        """

        self.new_credential = Credentials.credentials_list["Account"] = "Password"
        self.new_credential = Credentials.credentials_list["Acount"] = "Pasword"
        self.new_credential = Credentials.credentials_list["Twitter"] = "2E22a 
        '''

    def test_init(self):
        '''
        running test to see if new instance for test has been initialised
        '''

        self.assertEqual(self.new_credential.account_service,"Account")
        self.assertEqual(self.new_credential.password,"Password")




    '''def test_init(self):
        """
        test for initiation of a new instance of the credential class
        """

        self.assertEqual(self.new_credential ,"2E22a")'''
        # self.assertEqual(self.new_credential,"2E22a")


    def test_save_credential(self):
        """
        Test if our dredentials are in the dictionary
        """
        self.new_credential.save_credentials() # saving new credential
        self.assertEqual(len(Credentials.credentials_list),1)



    def test_multiple_credentials(self):
        """
        Test to see if our append is happening
        """

        self.new_credential.save_credentials()
        test_credentials = Credentials("Facebook","face")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_delete_users(self):
        """
        Test if we can retrieve a dictionary item from our list of various items
        """

        self.new_credential.save_credentials()
        test_credentials = Credentials("Facebook", "face")
        test_credentials.save_credentials()

        self.new_credential.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)


    def test_extract_credential_by_account(self):
        '''
        test o see if we can fin our account and password
        '''

        self.new_credential.save_credentials()
        test_credentials = Credentials("Facebook", "face")
        test_credentials.save_credentials()

        found_credential = Credentials.extract_credential("Facebook")
        self.assertEqual(found_credential.account_service,test_credentials.account_service)


    def test_find_credential(self):
        '''
        test to see if credentials are available and returns true
        '''

        self.new_credential.save_credentials()
        test_credentials = Credentials("Facebook", "face")
        test_credentials.save_credentials()

        found_credential = Credentials.extract_credential("Facebook")
        self.assertTrue(found_credential)


    def test_display_credential(self):
        '''
        test for the displaying of creentials
        '''

        self.assertEqual(Credentials.credentials_list,Credentials.show_credentials())





if __name__ == '__main__':
    unittest.main()