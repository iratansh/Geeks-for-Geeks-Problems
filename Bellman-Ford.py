#User function Template for python3

class Solution:
    '''
    Function to implement Bellman Ford
    V: nodes in graph
    edges: adjacency list for the graph
    src: source vertex
    '''
    def bellmanFord(self, V, edges, src):
        dist = [10**8] * V
        dist[src] = 0
        
        # Relax all edges V-1 times
        for _ in range(V - 1):
            for u, v, w in edges:
                if dist[u] != 10**8 and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        # Check for negative weight cycle reachable from source
        for u, v, w in edges:
            if dist[u] != 10**8 and dist[u] + w < dist[v]:
                return [-1]  # Negative weight cycle detected
        
        return dist
