from os import mkdir
from shutil import rmtree


def create_folder(new_dir, file_location_path, renamed_files_folder):
    try:
        mkdir(new_dir)
    except:
        try:
            mkdir(file_location_path + renamed_files_folder)
            mkdir(new_dir)
        except:
            rmtree(new_dir)
            mkdir(new_dir)
    return
