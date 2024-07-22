# flatwhite/file_handler.py
import os
import shutil

def get_file_names(file_path):
    return os.listdir(file_path)

def path_exists(file_path, if_not_exists_create=False):
    exists = os.path.exists(file_path)
    if not exists and if_not_exists_create:
        os.makedirs(file_path)  # Changed to create directories
        return True
    return exists

def organize_files(file_path, pics=True, sounds=True, docs=True):
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

    # Define file extensions for each category
    pics_ext = [
        '.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.svg', 
        '.ico', '.webp', '.heic', '.raw', '.nef', '.cr2', '.orf', '.sr2', 
        '.arw', '.pef', '.dng', '.raf', '.rw2'
    ]
    sounds_ext = [
        '.mp3', '.wav', '.ogg', '.flac', '.aac', '.m4a', '.wma', '.aiff', 
        '.alac', '.amr', '.au', '.mid', '.midi', '.opus', '.ra', '.voc', 
        '.vox'
    ]
    docs_ext = [
        '.pdf', '.doc', '.docx', '.txt', '.xls', '.xlsx', '.ppt', '.pptx', 
        '.odt', '.ods', '.odp', '.rtf', '.tex', '.wpd', '.md', '.html', 
        '.htm', '.xml', '.csv', '.tsv', '.log', '.epub', '.mobi', '.azw3', 
        '.fb2', '.djvu'
    ]

    # Iterate through each file in the given directory
    for filename in os.listdir(file_path):
        # Get the file extension
        file_ext = os.path.splitext(filename)[1].lower()
        source_file = os.path.join(file_path, filename)

        # Skip directories
        if os.path.isdir(source_file):
            continue

        # Move files to the correct directories
        if pics and file_ext in pics_ext:
            shutil.move(source_file, pics_dir)
        elif sounds and file_ext in sounds_ext:
            shutil.move(source_file, sounds_dir)
        elif docs and file_ext in docs_ext:
            shutil.move(source_file, docs_dir)
        else:
            if docs:
                shutil.move(source_file, docs_dir)

# Example usage
# organize_files('/path/to/your/files')
