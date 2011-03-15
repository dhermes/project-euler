def sieve(n):
    # requires n > 0
    prime_sieve = range(n+1)
    prime_list = []

    for index in range(2,n+1):
        if prime_sieve[index]:
            prime_list += [index]
            for sub_index in range(2*index,n+1,index):
                prime_sieve[sub_index] = 0

    return prime_list

def exceeds(primes, max_):
    index = 1
    for prime in primes[::2]:
        if (2*index % prime)*prime > max_:
            return index, prime
        index += 2
    return -1, 1

if __name__ == "__main__":
    print "The answer to Euler Project, question 122 is:",
    # Since there are approx n/ln(n) primes up to n,
    # there are 248465/ln(248465) ~ 20000 primes up to 248465
    # p_1 = 2
    # For n odd, we need (2*n % p[n])*p[n] > 10**10
    PRIMES = sieve(248465)
    index, prime = exceeds(PRIMES, 10**10)
    print index
