# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 10:01:48 2022

@author: user
"""


import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')
parser.add_argument('-p','--print', action='store_true',
                    help='print out the given integers')

args = parser.parse_args()
print(args.accumulate(args.integers))
if args.print:
    print(args.integers)