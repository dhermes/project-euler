import time
from math import floor
from math import log10

def euler_timer(problem_number):

    def result_timer(method):
        def timed_method(*args, **kwargs):
            print ('The answer to Euler Project,' \
                  ' question %s is:' % problem_number),
            start_time = time.time()
            result = method(*args, **kwargs)
            finish_time = time.time()

            runtime = finish_time - start_time
            exponent = int(floor(log10(runtime)))
            print "\nThis solution ran in %sE%s seconds." % (
                round(10**(-exponent)*runtime, 3), exponent)

            return result

        return timed_method

    return result_timer
