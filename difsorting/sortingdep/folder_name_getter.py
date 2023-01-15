# For linux
# Not checked on win
def get_folder_name(folder, path_sep):
    if folder[-1] == path_sep:
        string_name = ""
        i = -1
        while True:
            i -= 1
            if folder[i] == path_sep:
                string_name = path_sep + str(string_name[::-1])
                return string_name
            string_name += folder[i]
    else:
        return path_sep + "SomeFileName"
