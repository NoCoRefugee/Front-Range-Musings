#! /usr/bin/env python3
from decimal import Decimal, getcontext

e = Decimal(0)
f = Decimal(1)
n = Decimal(1)

while True:
      olde = e
      e += Decimal(1) / f
      if e == olde: # if there is no change in the 40 places, stop.
            break
      f *= n
      n += Decimal(1)
      
print(float(e))


