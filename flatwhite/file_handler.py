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
    return os.listdir(file_path)

def path_exists(file_path, if_not_exists_create=False):
    exists = os.path.exists(file_path)
    if not exists and if_not_exists_create:
        os.makedirs(file_path)  # Changed to create directories
        return True
    return exists

def organize_files(file_path, pics=False, sounds=False, docs=False):
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

def generate_folders(**folders):
    """
    Generates nested folders based on the provided dictionary structure.

    Example:
        folders = {
            'books': {
                'fantasy': {},
                'crime': {}
            },
            'audiobooks': {}
        }
        generate_folders(base_path, **folders)
    """
    def create_subfolders(base_path, subfolders):
        for folder_name, subfolder_structure in subfolders.items():
            folder_path = os.path.join(base_path, folder_name)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            if isinstance(subfolder_structure, dict):
                create_subfolders(folder_path, subfolder_structure)

    create_subfolders(os.getcwd(), folders)

# Example usage:
# organize_files('/path/to/directory', pics=True, sounds=True, docs=True)
# delete_files('/path/to/directory', pics=True, additional_extensions='.tmp,.log')
# generate_folders(books={'fantasy': {}, 'crime': {}}, audiobooks={})
