from python_code.functions import sieve

def max_digs(n):
    digs = set(str(n))
    counts = [(dig, str(n).count(dig)) for dig in digs]
    return sorted(counts, key=lambda pair: pair[1])[-1]

def find_and_replace(n, dig):
    digits = range(10)
    if str(n)[0] == dig:
        digits.remove(0) # no leading 0s

    string_val = str(n)
    result = [string_val.replace(dig, str(substitute))
              for substitute in digits]
    return [int(xx) for xx in result]

PRIMES = sieve(10**6)

for prime in PRIMES:
    digit, count = max_digs(prime)
    if count > 2:
        candidates = find_and_replace(prime, digit)
        match_count = 0
        for candidate in candidates:
            if candidate in PRIMES:
                match_count += 1
        if match_count == 8:
            winner = prime
            break
print winner
