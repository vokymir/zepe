#!/bin/python3

import math
import os
import random
import re
import sys
from collections import deque

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    graph = [[] for _ in range(n + 1)]  # 1-based indexing

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)  #  -1 means unreachable
    dist[s] = 0            # distance to start node is 0

    queue = deque([s])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if dist[neighbor] == -1:  # Not visited yet
                dist[neighbor] = dist[current] + 6  # Edge weight is 6
                queue.append(neighbor)

    #  distances excluding the start node
    result = []
    for i in range(1, n + 1):
        if i != s:
            result.append(dist[i])

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
