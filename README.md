# flatwhite

## Overview

This project contains several modules designed to handle various tasks including web scraping, file handling, format validation, and project structure creation. Below is a detailed description of each module and their respective functions.

## Modules and Functions

### `web_scraper.py`

This module includes functions related to web scraping.

- **Imports:**
  - `requests`
  - `smtplib`
  - `time`
  - `datetime`

### `file_handler.py`

This module includes functions for handling and organizing files.

- **`get_file_names(file_path)`**
  - **Description:** Get the list of file names in the specified directory.
  - **Parameters:** `file_path (str)`: The path of the directory.
  - **Returns:** `list`: List of file names in the directory.

- **`path_exists(file_path, if_not_exists_create=False)`**
  - **Description:** Check if a path exists and optionally create it if it does not.
  - **Parameters:**
    - `file_path (str)`: The path to check.
    - `if_not_exists_create (bool)`: If True, create the path if it does not exist (default: False).
  - **Returns:** `bool`: True if the path exists or was created, False otherwise.

- **`organize_files(file_path, pics=False, sounds=False, docs=False)`**
  - **Description:** Organize files in the specified directory into subdirectories based on file type.
  - **Parameters:**
    - `file_path (str)`: The path of the directory to organize.
    - `pics (bool)`: If True, move picture files to the 'Pictures' subdirectory (default: False).
    - `sounds (bool)`: If True, move sound files to the 'Sounds' subdirectory (default: False).
    - `docs (bool)`: If True, move document files to the 'Documents' subdirectory (default: False).

- **`delete_files(file_path, pics=False, sounds=False, docs=False, additional_extensions='')`**
  - **Description:** Delete files in the specified directory based on the provided criteria.
  - **Parameters:**
    - `file_path (str)`: The path of the directory where files need to be deleted.
    - `pics (bool)`: If True, delete picture files (default: False).
    - `sounds (bool)`: If True, delete sound files (default: False).
    - `docs (bool)`: If True, delete document files (default: False).
    - `additional_extensions (str)`: A comma-separated string of additional file extensions to delete.

- **`generate_folders(base_path, folders)`**
  - **Description:** Generates nested folders based on the provided dictionary structure.
  - **Parameters:**
    - `base_path (str)`: The base directory path where folders need to be created.
    - `folders (dict)`: A dictionary representing the folder structure.

- **`list_directory_structure(root_dir, indent_level=0)`**
  - **Description:** Recursively lists the directory structure starting from the root_dir.
  - **Parameters:**
    - `root_dir (str)`: The root directory to start listing from.
    - `indent_level (int)`: The current level of indentation for pretty printing.

### `format_validator.py`

This module includes functions for validating different formats such as email, phone number, age, name, and password.

- **`validate_email(email, cleaning=False)`**
  - **Description:** Validates an email address. Optionally cleans the email before validation.
  - **Parameters:**
    - `email (str)`: The email address to validate.
    - `cleaning (bool)`: If True, the function will clean the email by stripping whitespace and converting to lowercase before validation.
  - **Returns:** `bool or str`: Returns True if the email is valid. If cleaning is True and the cleaned email is valid, returns the cleaned email. Otherwise, returns False.

- **`validate_phone(phone, cleaning=False)`**
  - **Description:** Validates a phone number. Optionally cleans the phone number before validation.
  - **Parameters:**
    - `phone (str)`: The phone number to validate.
    - `cleaning (bool)`: If True, the function will clean the phone number by removing all non-digit characters before validation.
  - **Returns:** `bool or str`: Returns True if the phone number is valid. If cleaning is True and the cleaned phone number is valid, returns the cleaned phone number. Otherwise, returns False.

- **`validate_age(age, cleaning=False)`**
  - **Description:** Validates an age input. Optionally cleans the age input before validation.
  - **Parameters:**
    - `age (str)`: The age to validate.
    - `cleaning (bool)`: If True, the function will clean the age input by extracting digits before validation.
  - **Returns:** `bool or str`: Returns True if the age is valid. If cleaning is True and the cleaned age is valid, returns the cleaned age. Otherwise, returns False.

- **`validate_name(name, cleaning=False)`**
  - **Description:** Validates and optionally cleans a name input.
  - **Parameters:**
    - `name (str)`: The name to validate and clean.
    - `cleaning (bool)`: If True, the function will clean the name by stripping whitespace and capitalizing each part of the name.
  - **Returns:** `str`: Returns the cleaned name with each part capitalized.

- **`validate_password(password, settings='base')`**
  - **Description:** Validates a password based on specified settings.
  - **Parameters:**
    - `password (str)`: The password to validate.
    - `settings (str)`: The validation settings to use. Default is 'base'.
  - **Returns:** `bool`: Returns True if the password is valid based on the settings. Otherwise, returns False.
  - **Raises:** `TypeError`: If the settings parameter is empty or contains only spaces.

### `templates.py`

This module includes functions for creating project structures with specific templates.

- **`create_project_structure(project_type='web', includes=None, templates='create')`**
  - **Description:** Creates a web project folder structure based on the provided includes and templates.
  - **Parameters:**
    - `project_type (str)`: The type of project. Default is 'web'.
    - `includes (list)`: A list of components to include in the project. Default is `['html', 'js', 'css', 'php', 'sql']`.
    - `templates (str)`: The type of templates to use. Default is 'create'.

### `__init__.py`

This module imports all the other modules to provide a unified interface.

- **Imports:**
  - `format_validator`
  - `file_handler`
  - `web_scraper`

## Usage

Provide instructions or examples on how to use the modules and functions in this project.

```python
from flatwhite import create_project_structure, validate_email, get_file_names

# Example usage
create_project_structure('web', includes=['html', 'js', 'css', 'php', 'sql'], templates='boilerplate')
email_valid = validate_email('example@example.com')
file_names = get_file_names('/path/to/directory')
