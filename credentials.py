class Credentials :
    '''
    This is the class for the passwords of the various websie our user is going to use
    '''

    credentials_dict = {}

    def __init__(self,account_service,password):

        """
        definig the instance classes for a specific website/app
        :param account_service:  The service, IG, FB etc
        :param password: Password belonging to password
        """

        self.account_service = account_service
        self.password = password





    #def save_passwords(self):
        '''
        appends to our dictionary, with the account as the key and password as value
        '''




