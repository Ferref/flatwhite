# flatwhite/file_handler.py
import os, shutil

def get_file_names(file_path):
    os.listdir(file_path)

def path_exists(file_path, if_not_exists_create=False):

    exists = os.path.exists(file_path)

    if not exists and if_not_exists_create:
        with open(file_path, 'w') as f:
            pass
        return True

    return exists
    


