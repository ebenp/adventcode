#http://adventofcode.com/day/4
# modified from reddit because I'm unfamilar with MD5
# https://www.reddit.com/r/adventofcode/comments/3vdn8a/day_4_solutions/
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
from future import standard_library
standard_library.install_aliases()

if __name__ == '__main__':
    import itertools
    from hashlib import md5
    key='abcdef'
    key='iwrupvqb'
    for i in itertools.count():
        if md5(key + str(i)).hexdigest().startswith('00000'):
            print(i)
            break
