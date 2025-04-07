# KIV-ZEPE: SP3

Jakub Vokoun, A23B0235P, Hours spent: 2.5 so far

## Task 1: Simple D&C median

Pivot is always the smallest or largest element.
E.g.: \[4,3,2,1,8,7,6,5,0\]

How this works out:
(for zero-based array)

1. \[4,3,2,1,**8**,7,6,5,0\]
2. \[4,3,2,1,**7**,6,5,0\], \[8\], \[\]
3. \[4,3,2,1,**6**,5,0\], \[7\], \[\]
4. \[4,3,2,1,**5**,0\], \[6\], \[\]
5. \[4,3,2,1,**0**\], \[5\], \[\]
6. \[\], \[0\], \[4,3,2,**1**\]
7. \[\], \[1\], \[4,3,**2**\]
8. \[\], \[2\], \[4,**3**\]
9. \[\], \[3\], \[**4**\]
10. \[\], \[**4**\], \[\]

## Task 2: Median of medians D&C method

Used the exact algorithm as in presentation, only change is
the choosing of pivot is using the median of medians method.
Not showing finding median in quintuplets, that's trivial.

- Step 1:

A = \[20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 11, 12, 13, 14, 15,
16, 17, 18, 19, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10\]

Quintuplets:

- \[20,21,22,23,24\] => 22
- \[25,26,27,28,29\] => 27
- \[30,11,12,13,14\] => 13
- \[15,16,17,18,19\] => 17
- \[1,2,3,4,5\] => 3
- \[6,7,8,9,10\] => 8

Quintuplets II:

- \[22,27,13,17,3\] => 17
- \[8\] => 8

Median of medians: (8 + 17) / 2 = 12.5

A_1 = \[11,12,1,2,3,4,5,6,7,8,9,10\]
A_2 = \[\]
A_3 = \[20,21,22,23,24,25,26,27,28,29,30,13,14,15,16,17,18,19\]

Result: Median_index is half the length of A: 30/2 = 15
That is more than length of A_1 + A_2 meaning we will only continue with A_3
and the new Median_index is gonna be:
    15 - (A_1.Len = 12 + A_2.Len = 0) = 3

- Step 2:

A = \[20,21,22,23,24,25,26,27,28,29,30,13,14,15,16,17,18,19\]

Quintuplets:

- \[20,21,22,23,24\] => 22
- \[25,26,27,28,29\] => 27
- \[30,13,14,15,16\] => 15
- \[17,18,19\] => 18

Quintuplets II:

- \[22,27,15,18\] => (18 + 22) / 2 = 20

Median of medians: 20

A_1 = \[13,14,15,16,17,18,19\]
A_2 = \[20\]
A_3 = \[21,22,23,24,25,26,27,28,29,30\]

Result: Median_index is 3
That is less than length of A_1 meaning the median is in A_1
and the Median_index remains unchanged.

- Step 3:

A = \[13,14,15,16,17,18,19\]

Quintuplets:

- \[13,14,15,16,17\] => 15
- \[18,19\] => (18 + 19) / 2 = 18.5

Quintuplets II:

- \[15,18.5\] => (15 + 18.5) / 2 = 16.75

Median of medians: 16.75

A_1 = \[13,14,15,16\]
A_2 = \[\]
A_3 = \[17,18,19\]

Result: Median_index is 3
That is less than length of A_1 meaning the median is in A_1
and the Median_index remains unchanged.

- Step 4:

A = \[13,14,15,16\]

Quintuplets:

- \[13,14,15,16\] => (14 + 15) / 2 = 14.5

Median of medians: 14.5

A_1 = \[13,14\]
A_2 = \[\]
A_3 = \[15,16\]

Result: Median_index is 3
That is equal to lengths of A_1 + A_2 meaning the median is in A_3
and the Median_index is 3 - (2 + 0) = 1

- Step 5:

A = \[15,16\]

Quintuplets:

- \[15,16\] => (15 + 16) / 2 = 15.5

Median of medians: 15.5

A_1 = \[15\]
A_2 = \[\]
A_3 = \[16\]

Result: Median_index is 1
That is more than the length of A_1 + A_2 meaning the median is in A_3
and the Median_index remains is 1 - (1 + 0) = 0

- Step 6:

A = \[16\]

Quintuplets:

- \[16\] => 16

Median of medians: 16

A_1 = \[\]
A_2 = \[16\]
A_3 = \[\]

Result: Median_index is 0
That is equal to the length of A_1 but less than lengths of A_1 + A-2
meaning the searched median is in A_2.

Therefore, the median is 16.

## Task 3: Square root

Algorith which takes integer *n* and integer *k* as parameters:
Let LOW = 0, HIGH = n, ANS, MID be floats.

1. MID = (HIGH - LOW) / 2
2. Based on MID * MID do either:
    - \< n: LOW = MID
    - \> n: HIGH = MID
    - \= n: return MID
3. If ANS - MID * MID < 10^(-k): return MID
4. ANS = MID * MID
5. Repeat from step 1.

