class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edge_list, src):
        # Step 1: Convert edge list to adjacency list
        adj = [[] for _ in range(V)]
        for u, v, w in edge_list:
            adj[u].append((v, w))
            adj[v].append((u, w))  # Since the graph is undirected

        # Step 2: Standard Dijkstra
        distances = [float("inf")] * V
        distances[src] = 0
        
        pq = [(0, src)]  # (distance, node)
        
        while pq:
            curr_dist, curr_node = heapq.heappop(pq)
            if curr_dist > distances[curr_node]:
                continue
            
            for nei, weight in adj[curr_node]:
                dist = curr_dist + weight
                if dist < distances[nei]:
                    distances[nei] = dist
                    heapq.heappush(pq, (dist, nei))
        
        return distances
