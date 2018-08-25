class Credentials :
    '''
    This is the class for the passwords of the various websie our user is going to use
    '''

    credentials_list = []

    def __init__(self,account_service,password):

        """
        definig the instance classes for a specific website/app
        :param account_service:  The service, IG, FB etc
        :param password: Password belonging to password
        """

        self.account_service = account_service
        self.password = password





    def save_credentials(self):
        '''
        appends to our dictionary, with the account as the key and password as value
        '''

        Credentials.credentials_list.append(self)

    '''@classmethod
    def search_dict(cls,):
        """
        search for the credential password from credential key
        """
        """for Credentials.credentials_dict['account_service'] in Credentials.credentials_dict:
            if Credentials.credentials_dict.keys(self) == 'account_service':
                return Credentials.credentials_dict """

        dict_query = Credentials.credentials_dict[]

        for Credential in cls.credentials_dict.keys():
            return Credential
            if Credentials.credentials_dict.keys(self) == 'account_service':
                return Credentials.credentials_dict

        if Credentials.credentials_dict.keys(self) == 'account_service':
            return Credentials.credentials_dict

        #Credentials.credentials_dict.keys[] '''


    def delete_credentials(self):
        """
        delete an account and its passwords
        """

        Credentials.credentials_list.remove(self)



