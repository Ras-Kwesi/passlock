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

    @classmethod
    def extract_credential(cls,passkey):
        '''
        Takes a string and returns the instance
        '''

        for credential in cls.credentials_list:
            if credential.account_service == passkey:
                return credential


    @classmethod
    def find_credential(cls,passkey):
        '''
        method to declare if a credential exists
        '''

        for credential in cls.credentials_list:
            if credential.password == passkey:
                return True

        return False

    @classmethod
    def show_credentials(cls):
        '''
        Method that shows the xredentials of the
        :return:
        '''

        return cls.credentials_list



