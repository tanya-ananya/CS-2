'''
Task2 (Custom Exception)

Write a python function ‘is_valid_email(str)’ that:
That takes an email address as the parameter. An email address is considered valid if:
It consists of two parts separated by the ‘@’ symbol (username@domain)
Username part starts with a letter 
Domain part ends with ‘student.gsu.edu’
If the provided email address is valid, the function should return True.
Otherwise, the function should:
‘raise’ a custom exception named ‘EmailFormatError’ which prints the following error message ‘Please enter a valid email address.’
Return False

Note: you have to define the custom exception first and then you can raise it.

Author: Taaruni Ananya
'''

class EmailFormatError(Exception):
    def __init__(self):
        self.message = "Please enter a valid email address."
        print(self.message)

def is_valid_email(email):
    try:
        username, domain = email.split('@')
        if not username[0].isalpha():
            raise EmailFormatError()
        if not domain.endswith('student.gsu.edu'):
            raise EmailFormatError()
        return True
    except (ValueError, IndexError):
        raise EmailFormatError()
    except EmailFormatError as e:
        print(e)
        return False
    
print()
email = 'tananya1@student'
is_valid_email(email)