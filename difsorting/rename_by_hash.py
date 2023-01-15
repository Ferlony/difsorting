from sortingdep import platform_checker, folder_name_getter, folder_creater
from os import listdir, path
from shutil import copy
import xxhash


class RenamerByHash:
    def __init__(self, filepath):
        self.__path_abs = filepath

    def platform_worker(self):
        if platform_checker.platform_checker() == "linux":
            # Sorted file location
            path_sep = "/"
            renamed_files_folder = path_sep + "SortedFiles" + path_sep + "FilesRenamedByHash"

            dir_name = folder_name_getter.get_folder_name(self.__path_abs, path_sep)
            return self.__rename_by_hash(renamed_files_folder, self.__path_abs, dir_name, path_sep)
        elif platform_checker.platform_checker() == "windows":
            # Sorted file location
            path_sep = "\\"
            renamed_files_folder = path_sep + "SortedFiles" + path_sep + "FilesRenamedByHash"

            dir_name = folder_name_getter.get_folder_name(self.__path_abs, path_sep)
            return self.__rename_by_hash(renamed_files_folder, self.__path_abs, dir_name, path_sep)
        else:
            raise Exception("NotSupportedPlatformError")

    @staticmethod
    def __rename_by_hash(renamed_files_folder, path_abs, dir_name, path_sep):
        file_location_path = path.dirname(__file__)
        file_list = listdir(path_abs)
        new_dir = file_location_path + renamed_files_folder + dir_name
        try:
            folder_creater.create_folder(new_dir, file_location_path, renamed_files_folder)
        except Exception as e:
            return e

        for i in range(0, len(file_list)):
            file_name, file_extension = path.splitext(file_list[i])
            file_hash = xxhash.xxh3_128_hexdigest(file_list[i])
            copy(path_abs + path_sep + file_list[i], new_dir + path_sep + file_hash + file_extension)

        return str(new_dir + path_sep)
