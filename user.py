class User:
    '''This will serve as our
    class for user instances'''

    lockusers = [] #This is a   class variable as any instance has access to this list

    def __init__(self,first_name,last_name,password,email):

        '''The init function is used to define object properties
        first_name and last_name take the names, while password is
        a credential for modern day login
        this are accessed only by the instance, not others
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.password = password
        self.email = email


    def save_user(self):
        '''This is a function that appends our
        user list
        '''

        User.lockusers.append(self)

