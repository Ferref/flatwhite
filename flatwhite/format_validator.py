# flatwhite/format_validator.py
import re 

def validate_email(email) -> bool:

    valid_email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(valid_email_pattern, email):
        return True
    else:
        return False
    
def validate_phone(phone) -> bool:

    extract_numbers = r'\d+'

    numbers_from_phone = re.findall(extract_numbers, phone)
    numbers_from_phone = ''.join(numbers_from_phone)

    correct_phone_number_length = 10

    if len(numbers_from_phone) == correct_phone_number_length:
        return True
    else:
        return False
        








    






