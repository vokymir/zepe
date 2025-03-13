import sys
import math

def sieve(limit):
    """ Returns a list of primes up to 'limit' using Sieve of Eratosthenes. """
    is_prime = bytearray(b'\x01') * (limit + 1)
    is_prime[:2] = b'\x00\x00'  # Mark 0 and 1 as non-prime
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            is_prime[i * i: limit + 1: i] = b'\x00' * ((limit - i * i) // i + 1)
    return [i for i, prime in enumerate(is_prime) if prime]

def is_prime(n):
    """ Miller-Rabin primality test for fast large prime checks. """
    if n < 2:
        return False
    for p in (2, 3, 5, 7, 11):
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def estimate_required_m(n):
    """ Estimate how many primes are needed to exceed 'n'. """
    m = 1000
    while (m * m * math.log(m)) / 2 < n:
        m *= 2
    return m

def find_longest_prime_sum(n):
    """ Finds the largest prime that is a sum of the most consecutive primes. """
    # Estimate the required sieve limit
    m_est = estimate_required_m(n)
    U = int(m_est * math.log(m_est) * 1.2)
    U = min(U, n) if n < U else U

    primes = sieve(U)
    prefix = [0]
    for p in primes:
        prefix.append(prefix[-1] + p)

    # Determine max chain length possible
    L_possible = 0
    for i, s in enumerate(prefix):
        if s < n:
            L_possible = i
        else:
            break

    # Search for the longest prime sum
    for L in range(L_possible, 0, -1):
        s = prefix[L]
        if s < n and is_prime(s):
            return s, L
        for i in range(1, len(primes) - L + 1):
            s = prefix[i + L] - prefix[i]
            if s >= n:
                break
            if is_prime(s):
                return s, L
    return 0, 0

def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        prime, length = find_longest_prime_sum(n)
        print(prime, length)

if __name__ == "__main__":
    main()
