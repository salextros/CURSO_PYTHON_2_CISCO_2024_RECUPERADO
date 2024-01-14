import math

print(math.sin(math.pi/2))
print("")

def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14

print(sin(pi/2))
print("")
print(math.sin(math.pi/2))

from math import sin, pi
print("")
print(sin(pi/2))

from math import sin, pi
print("")
print(sin(pi / 2))

pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print("")
print(sin(pi / 2))

#########################################################################
pi = 3.14


def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None

print("")
print(sin(pi / 2))

from math import sin, pi
print("")
print(sin(pi / 2))

##########################################################################

import math
  
for name in dir(math):
  print(name, end="∖t")
  
print("")
##########################################################################

from math import pi, radians, degrees, sin, cos, tan, asin

ad = 90
ar = radians(ad)
ad = degrees(ar)

print(ad == 90.)
print(ar == pi / 2.)
print(sin(ar) / cos(ar) == tan(ar))
print(asin(sin(ar)) == ar)
  
print("")
##########################################################################

from math import e, exp, log

print(pow(e, 1) == exp(log(e)))
print(pow(2, 2) == exp(2 * log(2)))
print(log(e, e) == exp(0))

print("")
##########################################################################


from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))

print("")
##########################################################################

from random import random

for i in range(5):
    print(random())
    
print("")
##########################################################################

from random import random, seed

seed(0)

for i in range(5):
    print(random())
    
print("")
##########################################################################

from random import randrange, randint

print(randrange(1), end=' ')
print(randrange(0, 1), end=' ')
print(randrange(0, 1, 1), end=' ')
print(randint(0, 1))

print("")
##########################################################################

from random import randint

for i in range(10):
    print(randint(1, 10), end=',')
    
print("")
########################################################################## 
    
from random import choice, sample

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(choice(my_list))
print(sample(my_list, 5))
print(sample(my_list, 10))

print("")
########################################################################## 

from platform import platform

print(platform())
print(platform(1))
print(platform(0, 1))


print("")
########################################################################## 

from platform import machine

print(machine())

print("")
########################################################################## 

from platform import processor

print(processor())

print("")
########################################################################## 

from platform import system

print(system())

print("")
########################################################################## 

from platform import version
 
print(version())

print("")
########################################################################## 

from platform import python_implementation, python_version_tuple

print(python_implementation())

for atr in python_version_tuple():
    print(atr)
  
print("")
##########################################################################   

import sys

for p in sys.path:
  print(p)

print("")
########################################################################## 

import MODULOS_SAMIR

print(MODULOS_SAMIR.OperacionM(5,10,20))


 

