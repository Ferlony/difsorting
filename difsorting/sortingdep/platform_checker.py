from sys import platform


def platform_checker():
    if platform == "linux" or platform == "linux2":
        return "linux"
    elif platform == "win32":
        return "windows"
