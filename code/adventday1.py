if __name__ == '__main__':
    from __future__ import absolute_import, division, print_function
    from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
    from future import standard_library
    standard_library.install_aliases()
    with open('input1.txt', "r") as myfile:
        # strip new lines just in case
        data=myfile.read().replace('\n', '')

    count = 0

    for i in data:
        
        if i =="(":
            count += 1
        else:
            count -= 1
    print count
