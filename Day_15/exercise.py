## SYNTAX ERROR

print 2 + 6

print(2 + 6)

## NAME ERROR

print( num + 6)

num = 4
print( num + 6)


## INDEX ERROR

lst = [4,8,'go','8',4.5]
print(lst[6])

lst = [4,8,'go','8',4.5]
print(lst[4])

## MODULE NAME ERROR

import Math

import math

## ATTRIBUTE ERROR

from math import square

from math import sqrt

## KEY ERROR


tuples = {'Name':'Munzali','Age':26,'Sex':'Male'}
print(tuples['name'])

print(tuples['Name'])

## TYPE ERROR

print(5 + '8')

print(5 + int('8'))

## IMPORT ERROR

from math import power

from math import pow

### VALUE ERROR

int(23.8a)

int(23.8)

## ZERO DEVISION ERROR

3/0