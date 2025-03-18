

def sieve_of_eratosthenes(n:int) -> list[int]:
    array:bytearray = bytearray(b'\x01') * (n + 1)
    array[:2] = b'\x00\x00'
    index:int = 0
    res:list[int] = list()

    while index * index < n:

        if array[index]:
            array[index * index : n + 1 : index] = b'\x00' * ( (n - index*index) // index + 1 )

        index += 1

    for i in range(len(array)):
        if array[i]:
            res.append(i)

    return res


if __name__ == "__main__":
    print(sieve_of_eratosthenes(int(1e10)))
