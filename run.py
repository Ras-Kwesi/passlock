#!/usr/bin/env python3.6

from user import User
from credentials import Credentials

def create_profile(fname,sname,passwad,mail):
    '''
    Function to create a new user profile
    '''

    new_profile = User(fname,sname,passwad,mail)
    return new_profile

def save_profile(user):
    '''
    function to save user profile
    '''
    user.save_user()


