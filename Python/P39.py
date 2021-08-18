def getPrimeRange(_start, _end) :
    '''
    This function finds the prime numbers in given range.

    :arg a: this is a
    Parameters :
        _start (int) : start of the range to find prime numbers in.
        _end (int) : end of the range to find prime numbers in.

    Returns :
        List of prime numbers in the given range.
    '''

    primes = [True for i in range(_end+1)]

    # Start with 2
    p = 2

    # for every element eliminate all it's multiples
    while p*p <= _end :
        if primes[p] == True :
            for i in range(p*p, _end+1, p) :
                primes[i] = False

        p += 1

    _start = 2 if _start < 2 else _start

    return [x for x in range(_start, _end+1) if primes[x]]

if __name__ == '__main__' :
    print(getPrimeRange(0, 97))