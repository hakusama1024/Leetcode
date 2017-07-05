#!/usr/bin/python
import random

def flipBias():
   if random.randint(0, 9) > 5: return True
   else: return False

def flipCoin(l, r, val):
   boundary = l * 0.4 + r * 0.6
   if boundary > val:
       if flipBias(): return True
       return flipCoin(l, boundary, val)
   else:
       if not flipBias(): return False
       return flipCoin(boundary, r, val)

def main():
   top = base = 0
   for i in range(100000):
       if flipCoin(0.0, 1.0, 0.5): base += 1
       else: top += 1

   print top, base

if __name__ == '__main__':
   main()
