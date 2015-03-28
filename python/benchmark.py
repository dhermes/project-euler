#!/usr/bin/env python

import argparse
import os
import time

parser = argparse.ArgumentParser()
parser.add_argument('--iterations', metavar='N', type=int,
                    help='number of times to run the benchmark')
parser.add_argument('--sum', action='store_true',
                    help='sum the times (default: find the average)')
parser.add_argument('--fast', action='store_true',
                    help='just execute the short running problems')
args = parser.parse_args()
iterations = 1 if args.iterations is None else args.iterations

if args.fast:
    problem_list = [1, 2, 3, 5, 6, 8, 13, 15, 16, 18, 19, 20, 24, 28, 40, 45]
else:
    problem_list = range(1, 50 + 1)

for problem_number in problem_list:
    path = 'complete/no%03d.py' % problem_number
    if os.path.exists(path):
        module = 'complete.no%03d' % problem_number
    else:
        module = 'too_slow.no%03d' % problem_number

    main = __import__(module, fromlist=['main'])
    begin = time.time()
    for i in range(iterations):
        result = main.main()
    end = time.time()

    total = end - begin
    if not args.sum:
        total = total * 1.0 / iterations

    print '%s: %s, %sms' % (problem_number, result, int(1000 * total))
