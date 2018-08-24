class User:
    '''This will serve as our
    class for user instances'''

    def __init__(self,first_name,last_name,password,email):

        '''The init function is used to define object properties
        first_name and last_name take the names, while password is
        a credential for modern day login
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email