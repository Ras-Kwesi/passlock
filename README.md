# Password Locker

## Built By [Ras Kwesi](https://github.com/Ras-Kwesi/)

## Description
Password Locker is a python application that allows users to store password of various online services 

## User Stories

As a user I would like:
* To create an account with my details - log in and password
* Generate a password for a new credential
* Copy my credentials to the clipboard

## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display codes for navigation | **In terminal: $./pass_locker.py** | Welcome, choose an option: ca-Create Account, login-Log In, exit-Exit |
| Display prompt for creating an account | **Enter: ca** | Enter your first name, last name and password |
| Display prompt for login in | **Enter: li** | Enter your account name and password |
| Display codes for navigation | **Successful login** | Choose an option: cc - Create Credential, dc - Display Credentials, copy - Copy Credential, ex - exit |
| Display prompt for creating a credential | **Enter: cc** | Enter the account name, your username and password |
| Display a list of credentials | **Enter: dc** | Prints a list of saved credentials |
| Display prompt for which credential to copy | **Enter: copy** | Enter the account name of the credential you wish to copy. |
| Exit application | **Enter: ex** | Exit the current navigation stage |


### Installations & Prerequisites
* python3.6
* pip
* pyperclip

### Cloning
* In your terminal:
        
        `git clone https://github.com/ras-kwesi/passlock/`
        `cd pass_locker`

## Running the Application
* To run the application, in your terminal:

        `chmod +x run.py`
        `./run.py`
        
## Testing the Application
* To run the tests for the class file:

        `python3.6 test_user.py`
        `python3.6 test_credentials.py`
## Technologies Used
* Python3.6

## License
MIT &copy;2017 [Ras Kwesi](https://github.com/ras-kwesi/)