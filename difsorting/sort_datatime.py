from os import listdir, path
from shutil import copy
from sortingdep import platform_checker, folder_name_getter, files_in_dir_checker, folder_creater


class SorterDataTime:
    def __init__(self, filepath):
        self.__path_abs = filepath

    def platform_worker(self):
        if platform_checker.platform_checker() == "linux":
            # Sorted file location
            path_sep = "/"
            renamed_files_folder = path_sep + "SortedFiles" + path_sep + "FilesSortedDatatime"

            dir_name = folder_name_getter.get_folder_name(self.__path_abs, path_sep)
            return self.__sorter_datatime(renamed_files_folder, self.__path_abs, dir_name, path_sep)
        elif platform_checker.platform_checker() == "windows":
            # Sorted file location
            path_sep = "\\"
            renamed_files_folder = path_sep + "SortedFiles" + path_sep + "FilesSortedDatatime"

            dir_name = folder_name_getter.get_folder_name(self.__path_abs, path_sep)
            return self.__sorter_datatime(renamed_files_folder, self.__path_abs, dir_name, path_sep)
        else:
            raise Exception("NotSupportedPlatformError")

    @staticmethod
    def __sorter_datatime(renamed_files_folder, path_abs, dir_name, path_sep):
        file_location_path = path.dirname(__file__)
        file_list = listdir(path_abs)

        sorted_by_data_files_tuple = files_in_dir_checker.files_in_dir(file_list, path_abs, path_sep)
        keys = []
        for i in range(0, len(file_list)):
            keys.append(sorted_by_data_files_tuple[i][0])

        new_dir = file_location_path + renamed_files_folder + dir_name
        try:
            folder_creater.create_folder(new_dir, file_location_path, renamed_files_folder)
        except Exception as e:
            return e

        j = 0
        while j != len(file_list):
            i = 0
            while file_list[i] != keys[j]:
                i += 1
                if i > len(file_list):
                    raise NameError("MissingFilesError")
            copy(path_abs + path_sep + file_list[i], new_dir + path_sep + str(j + 1) + ". " + file_list[i])
            j += 1

        print("Files in new dir\n ", new_dir, "\n", listdir(new_dir))
        return str(new_dir + path_sep)
