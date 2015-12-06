#http://adventofcode.com/day/3
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
from future import standard_library
standard_library.install_aliases()

if __name__ == '__main__':
    data=[]
    coord=[[]]
    ns=0
    we=0
    with open('/Users/eben/Desktop/input3.txt', "r") as myfile:
       data=myfile.read().replace('\n', '')

   
    for item in data:
        if item == '^':
            ns += 1
        if item == 'v':
            ns -= 1
        if item == '>':
            we += 1
        if item == '<':
            we -= 1
            
        coord.append([ns,we])
    coord[0] =[0,0]
    uniq_coord = list(set(map(tuple, coord)))
    print('Number of houses: '+str(len(uniq_coord)))
        
