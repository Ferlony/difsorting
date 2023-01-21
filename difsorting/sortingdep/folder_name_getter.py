from os import sep


def get_folder_name(folder):
    if folder[-1] == sep:
        string_name = ""
        i = -1
        while True:
            i -= 1
            if folder[i] == sep:
                string_name = sep + str(string_name[::-1])
                return string_name
            string_name += folder[i]
    else:
        return sep + "SomeFileName"
