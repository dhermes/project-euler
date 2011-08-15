#!/usr/bin/env python

# a_n ... a_2 a_1
# Gives s_1 s_2 ... s_2 s_1
# where s_1 = a_n + a_1, s_k = a_k + a_{n + 1 - k}
# We have a choice s_k even, odd and s_k > 10, < 10
# With these choices, we can solve the entire problem

# For n < 10**9, we need to consider digits 1,...,9
# We use the fact that s_k = s_{n + 1 - k}

# We represent each sum by the possibility that
# it is >9 or <10 and even or odd

from python_code.decorators import euler_timer
from python_code.functions import all_subsets

def all_choices(n):
    result = []
    number_digit_sums = (n + 1)/2

    candidates = [('>=10', 1), ('>=10', 0), ('<10', 1), ('<10', 0)]
    for subset in all_subsets(candidates, number_digit_sums, unique=False):
        if n % 2 == 1:
            even_index = (n + 1)/2
            signature = subset[even_index - 1]
            # parity
            if signature[1] == 1:
                continue

        to_add = {}
        for k in range(1, n + 1):
            digit_sum_index = min(k, n + 1 - k)
            to_add[k] = subset[digit_sum_index - 1]
        result.append(to_add)

    return result

def valid_choice(choice, n):
    # all indices except final
    if choice[1][1] == 0:
        return False

    for k in range(2, n + 1):
        previous = choice[k - 1]
        curr = choice[k]

        parity = curr[1]
        if previous[0] == '>=10':
            parity = (parity + 1) % 2

        if parity == 0:
            return False

    return True

def choice_to_count(choice, n):
    number_digit_sums = (n + 1)/2

    result = 1
    for sum_index in range(1, number_digit_sums + 1):
        signature = choice[sum_index]
        if signature == ('<10', 0):
            if sum_index == 1:
                # 0 not allowed as a lead digit
                result *= 16
            elif n % 2 == 1 and sum_index == number_digit_sums:
                # if the final digit sum, it is 2*a_k
                result *= 5
            else:
                result *= 25
        elif signature == ('<10', 1):
            if sum_index == 1:
                # 0 not allowed as a lead digit
                result *= 20
            else:
                result *= 30
        elif signature == ('>=10', 0):
            if n % 2 == 1 and sum_index == number_digit_sums:
                # if the final digit sum, it is 2*a_k
                result *= 4
            else:
                result *= 25
        elif signature == ('>=10', 1):
            result *= 20
        else:
            raise Exception("Signature not recognized")

    return result

def main(verbose=False):
    running_sum = 0
    for digits in range(1, 9 + 1):
        for choice in all_choices(digits):
            if valid_choice(choice, digits):
                running_sum += choice_to_count(choice, digits)
    return running_sum

if __name__ == "__main__":
    print euler_timer(145)(main)(verbose=True)
