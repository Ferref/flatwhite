# flatwhite/format_validator.py
import re 

def validate_email(email):
    valid_email_status = False

    valid_email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(valid_email_pattern, email):
        valid_email_status = True
        return valid_email_status
    
def validate_phone(phone):
    validate_phone_status = False

    extract_numbers = r'\d+'

    numbers_from_phone = re.findall(extract_numbers, phone)
    numbers_from_phone = ''.join(numbers_from_phone)

    correct_phone_number_length = 10

    if len(numbers_from_phone) == correct_phone_number_length:
        validate_phone_status = True
        
    return validate_phone_status






    






