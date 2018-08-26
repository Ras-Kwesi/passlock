#!/usr/bin/env python3.6

from user import User
from credentials import Credentials
import random

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


def delete_profile(user):
    '''
     function to delete a user profile
    '''

    user.delete_user()


def create_credential(account,passwords):
    '''
    Creating an account for the
    '''

    new_credential = Credentials(account,passwords)
    return new_credential

def save_credential(credentials):
    '''
    to save user input credentials
    '''

    credentials.save_credentials()


def del_credential(credentials):
    '''
    fuction that deletes a credential
    '''

    credentials.delete_credentials()

def find_credentials(accounts):
    '''
    function to search for a credential and return a boolean value
    '''

    return Credentials.find_credential(accounts)

def extracted_credentials(accounts):
    '''
    provides the queried credential
    '''

    return Credentials.extract_credential(accounts)

def display_credentials():
    '''
    Function to show all credentials
    '''

    return Credentials.show_credentials()

def main():
    print("Hello and Welcome to the Passlocker App, What is your name?")
    user_name = input()

    print(f"Welcome {user_name}, The key in the following commands to perform the tasks you wish to....")


    while True:
        print('new - to create a new profile ---')

        key_strokes = input().lower()
        if key_strokes == "new":
            print("new Profile")

            print("First name")
            fname = input()

            print('surname')
            sname = input()

            print('email')
            mailer = input()

            print('password')
            passward = input()

            save_profile(create_profile(fname,sname,mailer,passward)) # Create new instance of user

            print(f'Profile for {fname} {sname} created')

        #
        while True:
            print("the following short codes allow you to interact with your account password")
            print("nac - create a new account password, del - delete an acoount password, dac - display account passwords")

            short_code = input().lower()
            if short_code == 'nac':
                print("new Account Password")

                print("Account Service")
                account_services = input()

                auto_password = random.randint(1000,9999)

                print(f"{auto_password} is youre password for {account_services},")

                save_credential(create_credential(account_services,auto_password)) #save the new acount service password

            elif short_code == 'del':
                print('enter the account service you want to delete')

                delete_account = input()
                if find_credentials(delete_account):
                    remove_account = find_credentials(delete_account)
                    del_credential(remove_account)

                else:
                    print(f"{delete_account} not an existing account password")
            elif  short_code == 'dac':

                if display_credentials():
                    print("Here is a list of youre accounts")
                    print("\n")

                    for account in display_credentials():
                        print(f"{account.account_service} {account.password}")
                        print('\n')

                else:
                        print('\n')
                        print('You have no account passwords')

            elif


if __name__=='__main__':
    main()