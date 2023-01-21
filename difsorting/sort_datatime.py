from os import listdir, path, sep
from shutil import copy
from sortingdep import platform_checker, folder_name_getter, files_in_dir_checker, folder_creater


class SorterDataTime:
    def __init__(self, filepath):
        self.__path_abs = filepath

    def platform_worker(self):
        if platform_checker.platform_checker() == "linux" or platform_checker.platform_checker() == "windows":
            return self.__main()
        else:
            print("Not tested, can be problems")
            return self.__main()

    def __main(self):
        # Sorted file location
        renamed_files_folder = sep + "SortedFiles" + sep + "FilesSortedDatatime"

        dir_name = folder_name_getter.get_folder_name(self.__path_abs)
        return self.__sorter_datatime(renamed_files_folder, self.__path_abs, dir_name)

    @staticmethod
    def __sorter_datatime(renamed_files_folder, path_abs, dir_name):
        file_location_path = path.dirname(__file__)
        file_list = listdir(path_abs)

        sorted_by_data_files_tuple = files_in_dir_checker.files_in_dir(file_list, path_abs)
        keys = []
        for i in range(0, len(file_list)):
            keys.append(sorted_by_data_files_tuple[i][0])

        new_dir = file_location_path + renamed_files_folder + dir_name

        folder_creater.create_folder(new_dir, file_location_path, renamed_files_folder)

        j = 0
        while j != len(file_list):
            i = 0
            while file_list[i] != keys[j]:
                i += 1
                if i > len(file_list):
                    raise NameError("MissingFilesError")
            copy(path_abs + sep + file_list[i], new_dir + sep + str(j + 1) + ". " + file_list[i])
            j += 1

        print("Files in new dir\n ", new_dir, "\n", listdir(new_dir))
        return str(new_dir + sep)
