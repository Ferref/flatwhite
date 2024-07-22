# flatwhite/format_validator.py
import re 

def validate_email(email):
    valid_email = False

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(regex, email):
        valid_email = True
        return valid_email
    





