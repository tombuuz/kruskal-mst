class Edge:
  def __init__(self, start: int, end: int, weight: int):
    self.start = start
    self.end = end
    self.weight = weight

class UnionFind:
  def __init__(self, size:int):
    self.parent = list(range(size))
    self.rank = [0] * size

  def find(self, u:int) -> int:
    if self.parent[u] != u:
      self.parent[u] = self.find(self.parent[u])
    return self.parent[u]

  def union(self, root_u, root_v):
    if root_u != root_v: # They are not in the same set -> No cycle
      if self.rank[root_u] > self.rank[root_v]: # Rank is used to keep the tree flat as possible, so that find() operation can be minimal. 
        self.parent[root_v] = root_u
      elif self.rank[root_u] < self.rank[root_v]:
        self.parent[root_u] = root_v
      else:
        self.parent[root_v] = root_u
        self.rank[root_u] += 1