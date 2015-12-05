#http://adventofcode.com/day/2
from __future__ import absolute_import, division, print_function
from builtins import (bytes, str, open, super, range,
                      zip, round, input, int, pow, object)
from future import standard_library
standard_library.install_aliases()

if __name__ == '__main__':
    import numpy as np
    l=[]
    w=[]
    h=[]
    data=[]
    with open('/Users/eben/Desktop/input2.txt', "r") as myfile:
       data = [line.rstrip('\n') for line in myfile]
   
    for item in data:
        itemint=[int(x) for x in item.split('x')]
        
        l.append(itemint[0])
        w.append(itemint[1])
        h.append(itemint[2])

    #convert to numpy
    l=np.array(l)
    w=np.asarray(w)
    h=np.asarray(h)
    #calculate sides
    s1=l*w
    s2=w*h
    s3=h*l
    #zip (dstack) together
    s=np.dstack((s1,s2,s3))
    sides=np.array(s[0,:])
    slack=[min(x) for x in sides]
    #determine final square footage
    sq_ft=s1*2+s2*2+s3*2+slack
    #print to screen
    print('Sum of square ft: '+str(np.sum([sq_ft])))
