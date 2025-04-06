
def mediansearch(median_index:float, array:list[float]) -> float:
    """
    D&C find median in unsorted array using Median of Medians method
    """
    x:float = find_pivot(array)

    a_1:list[float] = [n for n in array if n < x]
    a_2:list[float] = [n for n in array if n == x]
    a_3:list[float] = [n for n in array if n > x]

    if (len(a_1) > median_index):
        return mediansearch(median_index, a_1)
    elif (len(a_1) + len(a_2) > median_index):
        return x
    else:
        return mediansearch(median_index - (len(a_1) + len(a_2)), a_3)

def find_pivot(array:list[float]) -> float:
    arr:list[list[float]] = list()

    # split array into quintuplets
    for i in range(len(array) // 5):
        arr.append(array[5*i:5*(i+1)])
    # add any remainder (can be empty)
    arr.append(array[len(array) // 5 * 5 : len(array)])

    medians:list[float] = list()

    for chunk in arr:
        # skip empty remainder
        if len(chunk) < 1:
            continue
        # bruteforce median
        chunk.sort()
        if len(chunk) % 2 == 1:
            medians.append(chunk[len(chunk) // 2])
        else:
            value:float = (chunk[len(chunk) // 2 ] + chunk[len(chunk) // 2 - 1]) / 2
            medians.append(value)

    # either recursion or bruteforce on small array
    if len(medians) > 5:
        return find_pivot(medians)
    else:
        medians.sort()
        if len(medians) % 2 == 1:
            return medians[len(medians) // 2]
        else:
            val:float = (medians[len(medians) // 2 ] + medians[len(medians) // 2 - 1]) / 2
            return val

if __name__ == "__main__":
    c:float = mediansearch(15, [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(c)
