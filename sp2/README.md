# KIV/ZEP-E SP2

- Jakub Vokoun
- A23B0235P
- ~ 5 hours + ~ 1 hour making this readme

## Task 1: Derivation

The code for this task can be found in the folder **derivative**.
It is written in C#, dotnet 8.0 and can be run via:

```bash
cd <some_path>/derivative
dotnet build
dotner run```

### Subtask a: Calculate the derivative for 𝑥 = 𝜋

The program returned $0$ while the analytically correct result is $-1$,
because $sin'(𝜋) = cos(𝜋) = -1$.
The assigned $h = 1e-16$ is too small for double to recognize difference
between $\pi$ and $\pi + h$ - as $\pi$ have infinite expansion,
double will store all it's digits starting with 3.
This means, that it is precise around the value $3$, as with any other digit
it is required to use more bits. Adding value as small as $1e-16$
doesn't make any difference, because it cannot be saved.

### Subtask b: Modify algorithm

The value of $sin(x + h)$ can be expanded as:
$sin(x)cos(h) + cos(x)sin(h)$
Which now doesn't suffer from the difference in numbers,
meaning each $sin$ and $cos$ is calculated precisely and after this operation
we operate with numbers between $[-1, 1]$.

## Task 2: Matrix multiplication

The code for this task can be found in the folder **matrix**.
It is written in C#, dotnet 9.0 and can be run via:

```bash
cd <some_path>/matrix
dotnet build
dotner run```

Two type of matricies was created, one storing all values inside a matrix,
the second only storing non-zero values inside a band (note that these values
can be zero, but it is no guaranteed) as a 1D array.

The memory complexity for both matricies is, relative to the size of double,
when saying that $n$ is the dimension of a matrix (number of rows and columns),
and $m$ is the width of band:

$Complexity(DumbMatrix) = n \cdot n$
$Complexity(SmartMatrix) = (2 \cdot m - 1) \cdot n - m \cdot (m - 1)$

The second one, though looking more intimidatingly is for small $m$ obviously better.
The first term represents the count of all values, if we doesn't take
the matrix boundaries into consideration.
The second term is exactly that - a count of *cut-off* values,
due to the first and last *few* rows, in which a band is in fact shorter than $m$.

When measuring the time difference, only the time spent multipling is taken
into account. The output of spoken program is below (shortened), showing
the major time difference.

```
Measuring time difference between smart and dumb band matrix multiplication implementation.
Matrix dimension: 5000x5000
Band width: 5
Will repeat 100 times.
Time is measured in milliseconds.
 RUN | Dumb | Smart | Equals
01/100| 1193 | 0201  | True
02/100| 1172 | 0199  | True
03/100| 1133 | 0207  | True
04/100| 1127 | 0204  | True
05/100| 1121 | 0224  | True
...
95/100| 1221 | 0214  | True
96/100| 1121 | 0212  | True
97/100| 1125 | 0207  | True
98/100| 1126 | 0210  | True
99/100| 1124 | 0211  | True
100/100| 1127 | 0208  | True

###########
# Average #
###########
Dumb: 1130.19 ms
Smart: 207.55 ms```

## Task 3: Euler+ Contest Medium: #5 Smallest multiple

> All following tasks including this have the same specification given here:
> Written in python 3.13.
> Can be found in a folder named **euler**.
> The proofs of successfully submiting them are in folder **euler/proofs**.
> Can be run (assuming you have an input) via:

```bash
cd <some_path>/euler
python <task_file>.py```

The program search for smallest multiple by splitting all numbers below $n$
into their prime factors. The smallest multiple is multiple of these primes,
where each prime is included that many times, that it is in the number that
has it the most times.
Eg. the smallest multiple of 4:
Prime factors:
$2 = 2, 3 = 3, 4 = 2^2$
So the smallest multiple is $2^2 \cdot 3 = 12$.

The primes could have been precalculated, but the program calculate them in the runtime.

## Bonus A: Euler+ Contest Hard: #50 Consecutive prime sum

The program starts by estimating how many primes are needed to exceed $n$.
Then, the primes up to the estimate are generated via the [Sieve of Eratosthenes](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes).
Next, a little bit of dynamic programming is used in making a prefix-sum array.
After, the program creates a de-facto floating window, which check the longest possible
chain of numbers and if not plausable, shrink the window and check each sub-chain,
which reminds of *floating window* as the window is essentially floating along the array.
This repeats until the chain is found or not, in that case a (0, 0) is returned,
as no chain could be found.

## Bonus B: Euler+ Contest Advanced: #51 Prime digits replacement

The program starts by creating a list (and set) of primes in the searched range and
all combinations/permutations of the indexed where the * is.
Then these * marked positions are replaced with the same digit and if it is a prime,
we save it as a candidate.
Lastly, select the (lexicographically) smallest family and return it.

## The Hackerrank proofs

As mentioned above, all image proofs of successfully solved challenges are in the folder
**euler/proofs** and can be described as:

![All solved]("./euler/proofs/all_solved.png")
This image shows, that all three required challenges were solved.
Note, that you can see my avatar in the upper right corner (I added it just for this).

![Solved at total three]("./euler/proofs/solved_total_three.png")
This image shows the same, but in another settings.

![My profile with avatar]("./euler/proofs/my_profile_with_picture.png")
As I wrote earlier, the avatar I add just for this occasion, so you can distinguish it.

