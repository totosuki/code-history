import sys
input = sys.stdin.buffer.readline

from collections import defaultdict

class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in self.all_group_members().items())

N1, N2, M = map(int, input().split())
uf_1 = UnionFind(N1)
uf_2 = UnionFind(N2)

for _ in range(M):
  a, b = map(int, input().split())

  if a <= N1:
    uf_1.union(a-1, b-1)
  else:
    uf_2.union(a-N1-1, b-N1-1)

print(uf_1)
print(uf_2)
print(uf_1.parents)
print(uf_2.parents)

# 一重forループ数のみで4,5回が限度？
# 要は1からの距離を算出出来るようにすれば良いのか