#!/usr/bin/env python

import os
import time

for problem_number in range(1, 50 + 1):
  path = 'complete/no%03d.py' % problem_number
  if os.path.exists(path):
      module = 'complete.no%03d' % problem_number
  else:
      module = 'too_slow.no%03d' % problem_number

  main = __import__(module, fromlist=['main'])
  begin = time.time()
  result = main.main()
  end = time.time()
  print '%s: %s, %sms' % (problem_number, result, int(1000*(end - begin)))
