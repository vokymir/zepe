import sys
import math
import itertools

def generate_primes_range(low: int, high: int) -> tuple[list[int], set[int]]:
    """
    Generate a list and a set of prime numbers in the range [low, high) - inclusive down, exclusive up.
    Returns a tuple containing the list of primes and a set for fast membership testing.
    """
    size: int = high
    is_prime: list[bool] = [True] * size

    if size > 0:
        is_prime[0] = False
    if size > 1:
        is_prime[1] = False

    for i in range(2, int(math.sqrt(high)) + 1):
        if is_prime[i]:
            for j in range(i * i, high, i):
                is_prime[j] = False

    p_list: list[int] = [i for i in range(low, high) if is_prime[i]]
    p_set: set[int] = set(p_list)

    return p_list, p_set

class PrimeFamilyFinder:
    """
    Class to find the prime digit replacement family.

    Given n-digit prime, finds a family.
    Do via replacing k positions (of the same number) with all possible digits.
    Checks if a family have at least required_family_size primes.
    If more valid families exist, select the smallest one (lexicographically).
    """

    def __init__(self, n: int, k: int, required_family_size: int) -> None:
        """
        Initialize with number of digits (n), positions to replace (k), and required family size (required_family_size).
        """

        self.n: int = n
        self.k: int = k
        self.req_family_size: int = required_family_size

        self.low: int = 10 ** (n - 1)
        self.high: int = 10 ** n

        self.primes_list:list[int]
        self.primes_set:set[int]
        self.primes_list, self.primes_set = generate_primes_range(self.low, self.high)

        # Prepare all combinations of indices (of length k) for n-digit number
        self.index_combinations: list[tuple[int, ...]] = list(itertools.combinations(range(n), k))

    def find_family(self) -> list[int]:
        """
        Find and return the first valid prime family as a list of integers.
        Returns a sorted list containing the first L prime numbers in the valid family, or an empty list if no such family is found.
        """

        for prime in self.primes_list:
            prime_str: str = str(prime)
            best_family_for_prime: None | list[int] = None

            for indices in self.index_combinations:
                # All selected positions must be the same digit
                digit: str = prime_str[indices[0]]
                if any(prime_str[i] != digit for i in indices):
                    continue

                family: list[int] = []

                # Try replacing positions with every digit from '0' to '9'
                for d in "0123456789":
                    # Avoid leading zeros
                    if 0 in indices and d == "0":
                        continue

                    new_number_list: list[str] = list(prime_str)
                    for pos in indices:
                        new_number_list[pos] = d

                    candidate_str: str = "".join(new_number_list)
                    if len(candidate_str) != self.n or candidate_str[0] == "0":
                        continue

                    candidate: int = int(candidate_str)
                    if candidate in self.primes_set:
                        family.append(candidate)

                family = sorted(set(family))

                if len(family) >= self.req_family_size and family[0] == prime:
                    candidate_family: list[int] = family[:self.req_family_size]

                    if best_family_for_prime is None or tuple(candidate_family) < tuple(best_family_for_prime):
                        best_family_for_prime = candidate_family

            if best_family_for_prime is not None:
                return best_family_for_prime

        return []

def main() -> None:
    input_data: list[str] = sys.stdin.read().split()
    if not input_data:
        return

    n: int = int(input_data[0])
    k: int = int(input_data[1])
    required_family_size: int = int(input_data[2])

    finder: PrimeFamilyFinder = PrimeFamilyFinder(n, k, required_family_size)
    family: list[int] = finder.find_family()

    if family:
        _ = sys.stdout.write(" ".join(str(x) for x in family))
    else:
        _ = sys.stdout.write("")

if __name__ == "__main__":
    main()
