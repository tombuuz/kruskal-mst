from utils import Edge, UnionFind
from typing import List

def partition(arr: List[Edge], low: int, high: int) -> int:
    pivot = arr[high].weight
    i = low - 1
    for j in range(low, high):
        if arr[j].weight <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quicksort(arr: List[Edge], low: int, high: int) -> None:
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def kruskal_mst(edges: List[Edge], n_vertices: int) -> List[Edge]:
  quicksort(edges, 0, len(edges) - 1)
  unions = UnionFind(n_vertices)
  mst_edges = []
  for e in edges:
    root_u = unions.find(e.start)
    root_v = unions.find(e.end)
    if root_u != root_v:  # They are not in the same set -> No cycle
      unions.union(root_u, root_v)
      mst_edges.append(e)
  return mst_edges


if __name__ == '__main__':
    e1 = Edge(1, 0, 3)
    e2 = Edge(1, 0, 1)
    e3 = Edge(1, 2, 6)
    e4 = Edge(1, 2, 3)
    e5 = Edge(0, 2, 1)
    myedges = [e1, e2, e3, e4, e5]
    for e in kruskal_mst(myedges, 3):
        print(f"from {e.start} - to {e.end} with {e.weight} cost")
