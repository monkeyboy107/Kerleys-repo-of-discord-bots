# This function uses something called an arg. Basically it will take all the arguments you give to it as an array
def compress(*friends):
    return zip(friends)


if __name__ == '__main__':
    print(compress('test', 'test2', 'test3'))