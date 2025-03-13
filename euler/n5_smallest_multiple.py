import sys
import math

MAX_N:int = 40

# list of primes starting at 2
# for more info see function ensure_primes()
PRIMES:list[int] = list() 

# e.g. (on position 27) 26 = (1,0,0,0,0,1,0,...) which means 26 = 2 * 13
FACTORS:dict[int,list[int]] = dict()

def is_prime(n:int) -> bool:
    """
    Check if n is prime by trying to divide it by all numbers from range(2, sqrt(n)).
    """

    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True

def ensure_primes(N:int) -> None:
    """
    If primes are empty generates them. 
    Primes is a list of prime numbers, from 2 (inclusive) to N (inclusive).
    """
    if len(PRIMES) > 0:
        return

    for i in range(2, N+1):
        if is_prime(i):
            PRIMES.append(i)


def prime_factor(n:int) -> list[int]:
    """
    Returns the prime factor of number n. 
    Returns list of integers. 
    Integer on i-th position represents the count of i-th prime number in PRIMES.
    """
    ensure_primes(MAX_N)
    factor:list[int] = PRIMES.copy()
    prime:int = 1

    for i in range(len(factor)):
        prime = factor[i]
        factor[i] = 0

        while n > 1 and n % prime == 0:
            n //= prime
            factor[i] += 1
        
    return factor

def get_factor(n:int) -> list[int]:
    """
    Get the prime factor of number n.
    If not already available, calculates and returns.
    """

    if n not in FACTORS:
        FACTORS[n] = prime_factor(n)

    return FACTORS[n]

def smallest_multiple(n:int) -> int:
    """
    Get the smallest multiple of all numbers less and equal to n.
    """

    ensure_primes(MAX_N)
    smallest_factor:list[int] = [0 for _ in range(len(PRIMES))]

    # get the prime factor of wanted number
    for i in range(2, n+1):
        curr_factor = get_factor(i)

        for j in range(len(smallest_factor)):
            smallest_factor[j] = max(smallest_factor[j],curr_factor[j])

    # calculate the number from its prime factor
    res:int = 1
    for i in range(len(smallest_factor)):
        num = 1

        for _ in range(smallest_factor[i]):
            num *= PRIMES[i]

        res *= max(1, num) # to avoid multipling by 0

    return res

if __name__ == "__main__":
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        print(smallest_multiple(n))
