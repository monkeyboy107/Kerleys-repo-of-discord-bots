import os


# This defines the function of get_friends
def get_friends(path):
    # This assigns the local variable for data
    data = os.listdir(path)
    for file in data:
        # This will build the path correctly
        # The index function of a list returns the position of the string being passed to it. If the string being passed
        #   to it does not exist, it will raise an error
        data[data.index(file)] = build_correct_path(path, file)
    # This gets the data back
    return data


# This assigns the is_windows function
def is_windows():
    # This detects the OS
    if os.name == 'nt':
        # If it is windows this returns True
        return True
    else:
        # If this is not windows this will return False
        return False


# This assigns the build_correct_path function
def build_correct_path(path, file):
    # This defines the path slash
    path_slash = ''
    # This checks if the OS is windows or not
    if is_windows():
        # This assigns the slash to be a double backslash to be compatible with windows paths
        path_slash = '\\'
    else:
        # This assigns the slash for the sain way that not stupid people came up with due to windows being dumb
        path_slash = '/'

    # This builds the correct path
    path = path + path_slash + file

    # This gets the path back to us
    return path


if __name__ == '__main__':
    print(get_friends('friends'))