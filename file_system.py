"""
File:    file_system.py
Author:  Jason Appiah-Kubi
Date:    12/1/22
E-mail:  jasona2@umbc.edu
Description:
  simulated file system
"""


def pwd(path):
    """
           function returns the path that you are on
           :param: path, list of current path
    """
    thePath = [rootKey]

    for i in range(len(path)):
        if path[i] != "/":
            pathPrint = path[i] + "/"
            thePath.append(pathPrint)
    printList(thePath)


def ls(home, path):
    """
            displays content that a directory holds
           :param: home, current directory
           :param: path, list of current path
    """

    data = []

    if lengthCheck(path):
        for i in home[rootKey]:
            data.append(" ".join(home[rootKey][i]))
            # appends data from root key

        print(f"contents for {path[0]}")
        printList(data)
    elif not lengthCheck(path):

        for y in home[directory_key]:
            data.append("".join(y))
        for z in home[file_key]:
            data.append(" ".join(home[file_key]))
        # appends content in both file key and directory key of current directory

        print(f"contents for {path[-1]}")
        printList(data)


def cd(directory_name_or_path, home, path):
    """
            function helps with updating current directory
           :param: directory_name_or_path, the name of the directory that you are entering
           :param: home, current directory
           :param: path, list of directory names
           :return: returns new updated list of the path that you are on
    """
    if directory_name_or_path == "..":
        path = path[:-1]
        # deletes the last index
    elif "/" in directory_name_or_path:
        path[1:] = directory_name_or_path.split("/")
        if "" in path:
            path.remove("")
            # gets rid of unwanted indexes to avoid errors
    elif directory_name_or_path == "/":
        del path[1:]
        # deletes every index except root
    else:
        if lengthCheck(path):
            if directory_name_or_path in home[rootKey][directory_key]:
                for i in home[rootKey][directory_key]:
                    if i == directory_name_or_path:
                        path.append(i)
        elif not lengthCheck(path):
            # happens after you change directory when you are pass the root directory
            if directory_name_or_path in home[directory_key]:
                for d in home[directory_key]:
                    if d == directory_name_or_path:
                        # adds name to path if it matches the name of the directory that is being entered
                        path.append(d)

    return path


def mkdir(directory_name, home, path):
    """
               creates new directory inside current directory
              :param: directory_name, the name of the directory that you are creating
              :param: home, current directory
              :param: path, list of directory names
              :return: current directory
    """

    if "/" not in directory_name[0:-1]:
        # checks if there is a / in any thing besides the last character
        if lengthCheck(path):
            if directory_name not in home[rootKey][directory_key]:
                home[rootKey][directory_key][directory_name] = {directory_key: {}, file_key: []}
                # only adds keys in root keys directory
            else:
                print("Directory already created")

        if not lengthCheck(path):
            if directory_name not in home[directory_key]:
                # adds directory in directory key of current directory
                home[directory_key][directory_name] = {directory_key: {}, file_key: []}

    else:
        print("invalid name")

    return home


def touch(file_name_path, home, path):
    """
                  creates new file in current directories file key
                 :param: file_name, the name of the file that you are creating
                 :param: home, current directory
                 :param: path, list of directory names
                 :return: current directory
    """
    if lengthCheck(path):
        if "/" not in file_name_path:
            if file_name_path not in home[rootKey][file_key]:
                home[rootKey][file_key].append(str(file_name_path))
                # adds file to the file key in the root directory
        else:
            print("invalid name")
    elif not lengthCheck(path):
        if "/" not in file_name_path:
            if file_name_path not in home[file_key]:
                home[file_key].append(str(file_name_path))
        else:
            print("invalid name")
            # adds file to file key in current directory

    return home


def rm(file_name, home, path):
    """
                  removes file inside current directory
                 :param: file_name, the name of the file that you are removing
                 :param: home, current directory
                 :param: path, list of directory names

    """
    if lengthCheck(path):
        if file_name not in home[rootKey][file_key]:
            # only checks the root directory
            print("file not found")
        else:
            home[rootKey][file_key].remove(file_name)
    elif not lengthCheck(path):
        # works for every directory that isn't the root
        if file_name not in home[file_key]:
            print("file not found")
        else:
            home[file_key].remove(file_name)


def locate(file_name, path, home):
    # wasn't able to figure out function added some code to get partial credit
    """
                     finds locations that contains file name
                    :param: file_name, the name of the file that you are removing
                    :param: home, current directory
                    :param: path, list of directory names
                    :returns: either file name if found or message if file was not found

    """
    found = []
    pathCopy = path

    if lengthCheck(pathCopy):
        if file_name in home[rootKey][file_key]:
            print(file_name)
            return "file_name found in", rootKey

    elif not lengthCheck(pathCopy):
        if not found:
            print("file not found")
        if file_name in home[file_key]:
            found.append(file_name)
            return file_name, "found in"
        else:
            for t in system[rootKey][directory_key]:
                if file_name not in home[file_key]:
                    return locate(file_name, path[1:], home)


# helper functions
def validation(string, num1, num2):
    """
                         checks if input is within a certain length
                        :param: string, input that being checked
                        :param: num1, first number
                        :param: num2, second number
                        :returns: either true of false

        """
    if len(string) >= num1 or len(string) < num2:
        print("")
        return False
    else:
        return True


def lengthCheck(xlist):
    """
                         checks if the list equal to 1 or greater than 1
                        :param: xlist, any list passed through parameter
                        :returns: either true or false
    """
    if len(xlist) == 1:
        return True
    elif len(xlist) > 1:
        return False


def printList(xlist):
    """
        prints list
        :param: xlist, any list passed through parameter
        :returns: printed list
    """
    print(" ".join(xlist))


if __name__ == '__main__':

    directory_key = "directories"
    file_key = "files"
    rootKey = "/"

    system = {rootKey: {directory_key: {}, file_key: []}}

    fileSystem = ""
    currentPath = [rootKey]
    # keeps track of directory that you are currently in, always has root in it
    currentDir = system
    # copy of system used for updating the current directory
    test = []
    while fileSystem != "exit":
        fileSystem = input("")
        commands = fileSystem.strip().split()

        if commands[0] == "cd":

            currentPath = cd(commands[1], currentDir, currentPath)
            # current path gets updated
            current = currentPath[-1]
            # last index of currentPath represents the exact directory that you are in

            if lengthCheck(currentPath):
                currentDir = system
                # if the root is current directory then you are in the overall system

            elif len(currentPath) == 2:
                currentDir = system[rootKey][directory_key][current]
                # if the length is more than 1 then the current directory is the directory that matches current in the directory key
            elif len(currentPath) > 2:

                if commands[1] == ".." or "/" in commands[1]:
                    currentKey = currentPath[-2]
                    currentDir = system[rootKey][directory_key][currentKey][directory_key][current]
                    # need to go back to previous directory, and avoid KeyErrors
                else:
                    currentDir = currentDir[directory_key][current]
                    # used when you're just going further into the directories

        if commands[0] == "mkdir":
            if validation(commands, 3, 2):
                mkdir(commands[1], currentDir, currentPath)
            else:
                print("")

        if commands[0] == "touch":
            if validation(commands, 3, 2):
                touch(commands[1], currentDir, currentPath)
            else:
                print("")

        if commands[0] == "pwd":
            if validation(commands, 2, 1):
                pwd(currentPath)
            else:
                print("")

        if commands[0] == "rm":
            if validation(commands, 3, 2):
                rm(commands[1], currentDir, currentPath)
            else:
                print(" ")

        if commands[0] == "ls":
            ls(currentDir, currentPath)

        if commands[0] == "locate":
            locate(commands[1], currentPath, currentDir)
