import heapq
 
def tree(V, E, edges):
    adj = [[] for _ in range(V)]
    for i in range(E):
        u, v, wt = edges[i]
        adj[u].append((v, wt))
        adj[v].append((u, wt))
    pq = []
    visited = [False] * V
    res = 0
    heapq.heappush(pq, (0, 0))
    while pq:
        wt, u = heapq.heappop(pq)
        if visited[u]:
            continue 

        res += wt  
        visited[u] = True 
        for v, weight in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (weight, v))  
    return res  


if __name__ == "__main__":
    graph = [[0,1, 3],
            [1,2, 6],
            [1,3, 4],
            [2,4, 9],
            [3,4, 1]]
    # Function call
    print(tree(5, 5, graph))
