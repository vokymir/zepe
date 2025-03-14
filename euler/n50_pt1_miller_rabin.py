import random

def one_test(n:int, a:int) -> bool:
    exp:int = n - 1

    while not exp & 1:
        exp >>= 1

    if pow(a, exp, n) == 1:
        return True

    while exp < n - 1:
        if pow(a, exp, n) == n - 1:
            return True

        exp <<= 1

    return False


def miller_rabin(n:int, k:int = 40) -> bool:
    if n in [0,1]:
        return False
    if n in [2,3]:
        return True

    for i in range(k):
        r = random.randint(2, n - 1)
        if not one_test(n, r):
            return False

    return True

if __name__ == "__main__":
    for i in range(100):
        if miller_rabin(i):
            print(f"{i},", end="")




