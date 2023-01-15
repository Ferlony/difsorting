from os import path


def files_in_dir(file_list, path_abs, path_sep):
    files_dict = dict()
    print("Files in original dir: ", file_list)
    for i in range(0, len(file_list)):
        files_dict[file_list[i]] = str((path.getmtime(path_abs + path_sep + file_list[i])))
    sorted_by_data_files_tuple = sorted(files_dict.items(), key=lambda x: x[1])
    return sorted_by_data_files_tuple
