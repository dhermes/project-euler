#!/usr/bin/env python

from python_code.decorators import euler_timer
from python_code.functions import ascending
from python_code.functions import total_perms

def generate_addons(num, smallest, biggest):
    if num == 1:
        return [[i] for i in range(smallest, biggest + 1)]

    result = []
    for i in range(smallest, biggest + 1):
        result.extend([[i] + addon for addon
                       in generate_addons(num - 1, i, biggest)])
    return result

def main(verbose=False):
    MATCHES = []
    for bottom in range(1, 12 + 1):
        MATCHES.extend(ascending(10, 70, bottom, 12))

    add_ons = {}
    for biggest in range(1, 8):
        add_ons[biggest] = generate_addons(10, 1, biggest)

    count = 0
    for match in MATCHES:
        bottom = match[0]
        for addon in add_ons[bottom]:
            curr = addon + match
            count += total_perms(curr)
    return count

if __name__ == "__main__":
    print euler_timer(240)(main)(verbose=True)
