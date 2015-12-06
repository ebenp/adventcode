#http://adventofcode.com/day/5

from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
from future import standard_library
standard_library.install_aliases()

if __name__ == '__main__':
    from itertools import groupby

    data=[]
    status=[]
    a=['ab','cd','pq','xy']
    with open('/Users/eben/Desktop/input5.txt', "r") as myfile:
       data = [line.rstrip('\n') for line in myfile]

   
    for item in data:
        flag='naughty'
        if not any(x in item for x in a):
            cv=[item.count(letter) for letter in 'aeiou']

            if sum(cv) >= 3:
        
                if sum(sum(1 for i in g) >= 2 for k,g in groupby(item)) >= 1:
                    flag='nice'
                
            
        status.append(flag)
    print(status.count('nice'))
