import re

def validate_email(email, cleaning=False):
    valid_email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(valid_email_pattern, email):
        return True
    elif cleaning:
        email = email.strip().lower()
        if re.fullmatch(valid_email_pattern, email):
            return email
    return False

def validate_phone(phone, cleaning=False):
    extract_numbers = r'\d+'
    numbers_from_phone = re.findall(extract_numbers, phone)
    numbers_from_phone = ''.join(numbers_from_phone)
    
    correct_phone_number_length = 10

    if len(numbers_from_phone) == correct_phone_number_length:
        return True
    elif cleaning:
        phone = ''.join(numbers_from_phone)
        if len(phone) == correct_phone_number_length:
            return phone
    return False

def validate_age(age, cleaning=False):
    extract_numbers = r'\d+'
    numbers_from_age = re.findall(extract_numbers, age)
    age = ''.join(numbers_from_age)

    if age.isdigit():
        return True
    elif cleaning:
        if age.isdigit():
            return age
    return False

def correct_name(name, cleaning=False):
    name = name.strip()
    name_parts = name.split()
    
    capitalize_parts = ' '.join(part.capitalize() for part in name_parts)

    if cleaning:
        return capitalize_parts
    return capitalize_parts
