import re

def validate_email(email, cleaning=False):
    """
    Validates an email address. Optionally cleans the email before validation.
    
    Parameters:
    email (str): The email address to validate.
    cleaning (bool): If True, the function will clean the email by stripping whitespace and converting to lowercase before validation.
    
    Returns:
    bool or str: Returns True if the email is valid. If cleaning is True and the cleaned email is valid, returns the cleaned email.
                 Otherwise, returns False.
    """
    valid_email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

    if re.fullmatch(valid_email_pattern, email):
        return True
    elif cleaning:
        email = email.strip().lower()
        if re.fullmatch(valid_email_pattern, email):
            return email
    return False

def validate_phone(phone, cleaning=False):
    """
    Validates a phone number. Optionally cleans the phone number before validation.
    
    Parameters:
    phone (str): The phone number to validate.
    cleaning (bool): If True, the function will clean the phone number by removing all non-digit characters before validation.
    
    Returns:
    bool or str: Returns True if the phone number is valid. If cleaning is True and the cleaned phone number is valid, returns the cleaned phone number.
                 Otherwise, returns False.
    """
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
    """
    Validates an age input. Optionally cleans the age input before validation.
    
    Parameters:
    age (str): The age to validate.
    cleaning (bool): If True, the function will clean the age input by extracting digits before validation.
    
    Returns:
    bool or str: Returns True if the age is valid. If cleaning is True and the cleaned age is valid, returns the cleaned age.
                 Otherwise, returns False.
    """
    extract_numbers = r'\d+'
    numbers_from_age = re.findall(extract_numbers, age)
    age = ''.join(numbers_from_age)

    if age.isdigit():
        return True
    elif cleaning:
        if age.isdigit():
            return age
    return False

def validate_name(name, cleaning=False):
    """
    Validates and optionally cleans a name input.
    
    Parameters:
    name (str): The name to validate and clean.
    cleaning (bool): If True, the function will clean the name by stripping whitespace and capitalizing each part of the name.
    
    Returns:
    str: Returns the cleaned name with each part capitalized.
    """
    name = name.strip()
    name_parts = name.split()
    
    capitalize_parts = ' '.join(part.capitalize() for part in name_parts)

    if cleaning:
        return capitalize_parts
    return capitalize_parts

def validate_password(password, settings='base'):
    """
    Validates a password based on specified settings.
    
    Parameters:
    password (str): The password to validate.
    settings (str): The validation settings to use. Default is 'base'.
    
    Returns:
    bool: Returns True if the password is valid based on the settings. Otherwise, returns False.
    
    Raises:
    TypeError: If the settings parameter is empty or contains only spaces.
    """
    if settings.replace(' ', '') == '':
        raise TypeError
    
    if settings == 'base':
        '''
        8+ Characters
        Includes at least one number
        Includes at least one special character
        Includes at least one uppercase letter
        '''
        valid_password_pattern = '^(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'

        if re.fullmatch(valid_password_pattern, password):
            return True
        else:
            return False
