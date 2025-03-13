import sys
import timeit

def sieve(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for start in range(2, int(limit**0.5) + 1):
        if is_prime[start]:
            for multiple in range(start * start, limit + 1, start):
                is_prime[multiple] = False
    return [num for num, prime in enumerate(is_prime) if prime], is_prime

def find_longest_prime_sum(n):
    primes, is_prime = sieve(n)
    max_length = 0
    max_prime = 0
    
    prefix_sum = [0] * (len(primes) + 1)
    for i in range(len(primes)):
        prefix_sum[i + 1] = prefix_sum[i] + primes[i]
    
    for length in range(max_length + 1, len(primes)):
        for start in range(len(primes) - length):
            total = prefix_sum[start + length] - prefix_sum[start]
            if total > n:
                break
            if is_prime[total]:
                max_length = length
                max_prime = total
    
    return max_prime, max_length


def test():
    for i in range(1, 12):
        inp:int = int(10 ** i)
        t0 = timeit.default_timer()
        prime, length = find_longest_prime_sum(inp)
        t1 = timeit.default_timer()
        print(prime, length)
        print(f"Input: 10e{i}, time: {t1-t0}\n-----")


def main():
    t = int(sys.stdin.readline().strip())
    for _ in range(t):
        n = int(sys.stdin.readline().strip())
        prime, length = find_longest_prime_sum(n)
        print(prime, length)

if __name__ == "__main__":
    test()
    exit()
    main()
