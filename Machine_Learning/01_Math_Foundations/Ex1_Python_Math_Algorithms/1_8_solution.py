from heapq import *
from collections import defaultdict

with open('wordsEn.txt') as f:
    lines = f.readlines()
    f.close()
s = []
for i in lines:
    s.append((i[0:2], i[-3:-1], 1))

def dijkstra(edges, strat_node, end_node):
    g = defaultdict(list)
    for start, end, weight in edges:
        g[start].append((weight, end))
    q, visited = [(0, strat_node, ())], set()
    while q:
        (cost, v1, path) = heappop(q)
        if v1 not in visited:
            visited.add(v1)
            path = (v1, path)
            if v1 == end_node:
                return (cost, path)
            for c, v2 in g.get(v1, ()):
                if v2 not in visited:
                    heappush(q, (cost + c, v2, path))
    return float("inf")


kt_bd = input('nhap ki tu bat dau  ')
kt_kt = input('nhap ki tu ket thuc ')
d = dijkstra(s, kt_bd[-2:], kt_kt[0:2])
if isinstance(d, float):
    print("There is no such chain")
    exit(0)
(k, k1) = d
(k, k1) = k1
tt = [kt_kt]
while len(k1) > 0:
    (k2, k1) = k1
    for i in lines:
        if i[0:2] == k2 and i[-3:-1] == k:
            tt.append(i[:-1])
            break
    k = k2
tt.append(kt_bd)
print(tt[::-1])
