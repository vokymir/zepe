import math
import timeit


PRIMES = list()

def generate_primes(upper_bound:int) -> None:

    highest_known_prime:int = PRIMES[-1] if len(PRIMES) > 0 else 2
    sum:int = 0

    for i in range(highest_known_prime, upper_bound+1):
        if is_prime(i):
            PRIMES.append(i)
            sum += i

        if sum >= upper_bound:
            break



def is_prime(n:int) -> bool:

    for p in PRIMES:
        if n % p == 0:
            return False
        if n * 2 > p:
            return True

    return True



def floating_window(upper_bound:int):
    generate_primes(upper_bound)
    summa:int = 0
    start_index:int = 0
    count:int = 0

    while summa + PRIMES[count] < upper_bound:
        summa += PRIMES[count]
        count += 1

    # NOW I HAVE  LONGEST SEQUENCE EVER 

    # shrink the floating window 1 at a time
    for shrink in range(count):
        bkup_summa:int = summa

        # shift the window along the array of primes
        for shift in range(len(PRIMES) - count):
            # stop shifting, if greater than upper_bound
            if summa > upper_bound:
                break

            # if prime, it's DONE
            if is_prime(summa):
                # print(f"MAX: {upper_bound}, SUM: {summa}, COUNT: {count}, START: {start_index}, ARRAY: {PRIMES[start_index:start_index+count]}")
                print(f"{summa} {count}")
                return

            summa -= PRIMES[start_index + shift]
            summa += PRIMES[start_index + shift + count]

        summa = bkup_summa

        count -= 1
        summa -= PRIMES[start_index + count]


def test():
    for i in range(1, 12):
        inp:int = int(10 ** i)
        t0 = timeit.default_timer()
        floating_window(inp)
        t1 = timeit.default_timer()
        print(f"Input: 10e{i}, time: {t1-t0}\n-----")


if __name__ == "__main__":
    test()
    t = int(input().strip())
    for a0 in range(t):
        n = int(input().strip())
        floating_window(n)
































