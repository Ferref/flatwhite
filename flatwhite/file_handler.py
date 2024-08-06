import os
import shutil

# Define file extensions for each category
pic_extensions = [
    '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg',
    '.ico', '.webp', '.heic', '.raw', '.nef', '.cr2', '.orf', '.sr2',
    '.arw', '.pef', '.dng', '.raf', '.rw2'
]
sound_extensions = [
    '.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.aiff',
    '.alac', '.amr', '.au', '.mid', '.midi', '.opus', '.ra', '.voc',
    '.vox'
]
doc_extensions = [
    '.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx',
    '.odt', '.ods', '.odp', '.rtf', '.tex', '.wpd', '.md', '.html',
    '.htm', '.xml', '.csv', '.tsv', '.log', '.epub', '.mobi', '.azw3',
    '.fb2', '.djvu'
]

### Functions
def get_file_names(file_path):
    """
    Get the list of file names in the specified directory.

    Parameters:
    file_path (str): The path of the directory.

    Returns:
    list: List of file names in the directory.
    """
    return os.listdir(file_path)

def path_exists(file_path, if_not_exists_create=False):
    """
    Check if a path exists and optionally create it if it does not.

    Parameters:
    file_path (str): The path to check.
    if_not_exists_create (bool): If True, create the path if it does not exist (default: False).

    Returns:
    bool: True if the path exists or was created, False otherwise.
    """
    exists = os.path.exists(file_path)
    if not exists and if_not_exists_create:
        os.makedirs(file_path)
        return True
    return exists

def organize_files(file_path, pics=False, sounds=False, docs=False):
    """
    Organize files in the specified directory into subdirectories based on file type.

    Parameters:
    file_path (str): The path of the directory to organize.
    pics (bool): If True, move picture files to the 'Pictures' subdirectory (default: False).
    sounds (bool): If True, move sound files to the 'Sounds' subdirectory (default: False).
    docs (bool): If True, move document files to the 'Documents' subdirectory (default: False).
    """
    # Define directory names
    pics_dir = os.path.join(file_path, 'Pictures')
    sounds_dir = os.path.join(file_path, 'Sounds')
    docs_dir = os.path.join(file_path, 'Documents')

    # Create directories if they do not exist
    if pics and not os.path.exists(pics_dir):
        os.makedirs(pics_dir)
    if sounds and not os.path.exists(sounds_dir):
        os.makedirs(sounds_dir)
    if docs and not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    # Iterate through each file in the given directory
    for filename in os.listdir(file_path):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(file_path, filename)

        # Skip directories
        if os.path.isdir(source_file):
            continue

        # Move files to the correct directories
        if pics and file_ext in pic_extensions:
            shutil.move(source_file, os.path.join(pics_dir, filename))
        elif sounds and file_ext in sound_extensions:
            shutil.move(source_file, os.path.join(sounds_dir, filename))
        elif docs and file_ext in doc_extensions:
            shutil.move(source_file, os.path.join(docs_dir, filename))
        else:
            if docs:
                shutil.move(source_file, os.path.join(docs_dir, filename))

def delete_files(file_path, pics=False, sounds=False, docs=False, additional_extensions=''):
    """
    Delete files in the specified directory based on the provided criteria.

    Parameters:
    file_path (str): The path of the directory where files need to be deleted.
    pics (bool): If True, delete picture files (default: False).
    sounds (bool): If True, delete sound files (default: False).
    docs (bool): If True, delete document files (default: False).
    additional_extensions (str): A comma-separated string of additional file extensions to delete.

    Returns:
    None
    """
    if not os.path.exists(file_path):
        print(f'{file_path} does not exist!')
        return
    if not os.path.isdir(file_path):
        print(f'Error: {file_path} is not a directory!')
        return

    try:
        additional_extensions = [ext.strip() for ext in additional_extensions.split(',') if ext.strip()]
        extensions_to_delete = []

        if pics:
            extensions_to_delete.extend(pic_extensions)
        if sounds:
            extensions_to_delete.extend(sound_extensions)
        if docs:
            extensions_to_delete.extend(doc_extensions)
        if additional_extensions:
            extensions_to_delete.extend(additional_extensions)

        if not extensions_to_delete:
            print('No criteria given!')
            return

        files_deleted = False
        files_in_dir = os.listdir(file_path)

        for file in files_in_dir:
            file_extension = os.path.splitext(file)[1].lower()
            if file_extension in extensions_to_delete:
                file_to_delete = os.path.join(file_path, file)
                os.remove(file_to_delete)
                print(f'Deleted: {file_to_delete}')
                files_deleted = True

        if not files_deleted:
            print('No matching files found for deletion.')

    except PermissionError as e:
        print(f'Permission error: {e}')
    except FileNotFoundError as e:
        print(f'File not found error: {e}')
    except Exception as e:
        print(f'An unexpected error occurred: {e}')

def generate_folders(base_path, folders):
    """
    Generates nested folders based on the provided dictionary structure.

    Parameters:
    base_path (str): The base directory path where folders need to be created.
    folders (dict): A dictionary representing the folder structure.

    Example:
        folders = {
            'books': {
                'fantasy': {},
                'crime': {}
            },
            'audiobooks': {}
        }
        generate_folders(base_path, folders)
    """
    for folder_name, subfolder_structure in folders.items():
        folder_path = os.path.join(base_path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        if isinstance(subfolder_structure, dict):
            generate_folders(folder_path, subfolder_structure)


def list_directory_structure(root_dir, indent_level=0):
    """
    Recursively lists the directory structure starting from the root_dir.

    Parameters:
    root_dir (str): The root directory to start listing from.
    indent_level (int): The current level of indentation for pretty printing.
    """
    try:
        # List all files and directories in the current directory
        items = os.listdir(root_dir)
    except PermissionError:
        # Skip directories that we don't have permission to access
        return

    for item in items:
        item_path = os.path.join(root_dir, item)
        print(' ' * indent_level + '|-- ' + item)

        # If the item is a directory, recursively list its contents
        if os.path.isdir(item_path):
            list_directory_structure(item_path, indent_level + 4)


