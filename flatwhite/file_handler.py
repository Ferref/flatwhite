# flatwhite/file_handler.py
import os
import shutil

# Define file extensions for each category
pic_exentions = [
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
        if pics and file_ext in pic_exentions:
            shutil.move(source_file, pics_dir)
        elif sounds and file_ext in sound_extensions:
            shutil.move(source_file, sounds_dir)
        elif docs and file_ext in doc_extensions:
            shutil.move(source_file, docs_dir)
        else:
            if docs:
                shutil.move(source_file, docs_dir)

def delete_files(file_path, pics=False, sounds=False, docs=False, additional_extensions=''):
    exists = os.path.exists(file_path)
    isdir = os.path.isdir(file_path)

    if not exists:
        print(f'{file_path} does not exists!')
        return
    if not isdir:
        print(f'Error: {file_path} is not a directory!')

    try:
        additional_extensions = [extension for extension in additional_extensions]

        extensions_to_delete = []

        if pics:
            extensions_to_delete.extend(pic_exentions)
        if sounds:
            extensions_to_delete.extend(sound_extensions)
        if docs:
            extensions_to_delete.extend(doc_extensions)
        if additional_extensions:
            extensions_to_delete.extend(additional_extensions)

        if not extensions_to_delete:
            print('No criteria given!')

        files_deleted = False

        files_in_dir = os.listdir(file_path)

        for file in files_in_dir:
            file_extension = os.path.splitext(file)[1]

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
        print('File not found error: {e}')
    except Exception as e:
        print(f'An unexpected error occored: {e}')



        




