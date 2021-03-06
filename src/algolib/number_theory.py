threshold = 0
prime_set = set()


def prime_linear_sieve(n):
    is_composite = [False] * (n + 1)
    primes = list()
    for i in range(2, n + 1):
        if not is_composite[i]:
            primes.append(i)
        for j in primes:
            if j * i > n:
                break
            is_composite[j * i] = True
            if i % j == 0:
                break
    global threshold
    global prime_set
    if n > threshold:
        threshold = n
        prime_set = set(primes)
    return primes


def factor_naive(n):
    ans = dict()
    i = 2
    while i * i < n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                n //= i
                cnt += 1
            ans[i] = cnt
        i += 1
    if n != 1:
        ans[n] = 1
    return ans


def is_prime_naive(k):
    global threshold
    global prime_set
    if k < threshold:
        return k in prime_set
    else:
        if k < 2:
            return False
        else:
            i = 2
            while i * i <= k:
                if k % i == 0:
                    return False
                i += 1
            return True
