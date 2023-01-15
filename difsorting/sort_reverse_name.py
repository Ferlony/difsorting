from os import listdir, mkdir, path
from shutil import rmtree, copy
from sortingdep import platform_checker, folder_name_getter


class ReverseNameSorter:
    # Write your path to numerate Files By time edit
    # PathAbsolute = "\\ToEnum"
    # PathAbsolute = "/home/theuser/Downloads/prep/"
    __PathAbsolute = ""

    # if OS = linux -> change "\\" on "/"
    # if OS = windows -> change "/" on "\\"
    @property
    def PathAbsolute(self):
        return self.__PathAbsolute

    @PathAbsolute.setter
    def PathAbsolute(self, path):
        self.__PathAbsolute = path

    def platform_worker(self):
        if platformChecker.platform_checker() == "linux":
            # Sorted file location
            osspec = "/"
            FilesCreatedByProgramSorted = osspec + "FilesSortedReverseName"

            dirname = folderNameGetter.get_folder_name(self.PathAbsolute, osspec)

            self.__sorter_reverse_name(FilesCreatedByProgramSorted, self.PathAbsolute, dirname, osspec)
        elif platformChecker.platform_checker() == "win":
            # Sorted file location
            osspec = "\\"
            FilesCreatedByProgramSorted = osspec + "FilesSortedReverseName"

            dirname = folderNameGetter.get_folder_name(self.PathAbsolute, osspec)

            self.__sorter_reverse_name(FilesCreatedByProgramSorted, self.PathAbsolute, dirname, osspec)
        else:
            raise Exception("CantWorkPlatformOnYourPlatform")

    def __sorter_reverse_name(self, FilesCreatedByProgramSorted, PathAbsolute, dirname, osspec):

        return
