import math
import heapq

# PARAMETERS
W, H = 80, 24   # grid width and height
# obstacle: circle at (5,10) radius 7
obs_cx, obs_cy, obs_r = 5, 10, 7
# points of interest
POIs = {
    'A': (0, 0),
    'B': (0, 23),
    'C': (79, 5),
    'D': (20, 15),
}


def main():
    blocked, paths, dirs, weights, names, dists = compute_paths()
    print_paths(blocked, paths, names, dists)


def dijkstra(start:tuple[int,int], dirs, weights, blocked):
    dist = [[math.inf]*W for _ in range(H)]
    prev = [[None]*W   for _ in range(H)]
    sx, sy = start
    dist[sy][sx] = 0
    pq = [(0, sx, sy)]
    while pq:
        d, x, y = heapq.heappop(pq)
        if d>dist[y][x]:
            continue
        for dx, dy in dirs:
            nx, ny = x+dx, y+dy
            if 0 <= nx < W and 0 <= ny < H and not blocked[ny][nx]:
                nd = d + weights[(dx,dy)]
                if nd < dist[ny][nx]:
                    dist[ny][nx] = nd
                    prev[ny][nx] = (x,y)
                    heapq.heappush(pq, (nd, nx, ny))
    return dist, prev


def compute_paths():
    # blocked by obstacle = true
    blocked = [[False]*W for _ in range(H)]
    for y in range(H):
        for x in range(W):
            if math.hypot(x-obs_cx, y-obs_cy) < obs_r:
                blocked[y][x] = True

    # 8-connect, heigher weight for diagonal
    dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
    weights = {d: (1.0 if d[0]==0 or d[1]==0 else math.sqrt(2)) for d in dirs}

    # build
    names = list(POIs.keys())
    dists = {}   # (i,j)->distance
    paths = {}   # (i,j)->list of coords along path
    for i,name_i in enumerate(names):
        di, prev = dijkstra(POIs[name_i], dirs, weights, blocked)
        for j,name_j in enumerate(names):
            if j <= i: continue
            sx, sy = POIs[name_j]
            d = di[sy][sx]
            dists[(name_i,name_j)] = d
            # reconstruct path
            path = []
            cur = (sx,sy)
            while cur != POIs[name_i]:
                path.append(cur)
                cur = prev[cur[1]][cur[0]]
                if cur is None:
                    break
            path.append(POIs[name_i])
            paths[(name_i,name_j)] = path

    return blocked, paths, dirs, weights, names, dists


def print_paths(blocked, paths, names, dists):
    grid = [[' ']*W for _ in range(H)]
    # obstacles
    for y in range(H):
        for x in range(W):
            if blocked[y][x]:
                grid[y][x] = '.'

    # all paths
    for (i,j), path in paths.items():
        for x,y in path:
            # don't overwrite POI letters or obstacles
            # sanity check
            if grid[y][x] == ' ':
                grid[y][x] = '*'

    # POI letters
    for letter,(x,y) in POIs.items():
        grid[y][x] = letter

    # OUTPUT
    for row in grid:
        print(''.join(row))

    # last line: all distances
    pairs = []
    for i in range(len(names)):
        for j in range(i+1,len(names)):
            a, b = names[i], names[j]
            pairs.append(f"{a}-{b}: {dists[(a,b)]:5.1f}m")
    print('   '.join(pairs))


if __name__ == "__main__":
    main()
