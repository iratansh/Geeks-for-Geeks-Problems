from collections import deque

class Solution:
    
    def topoSort(self, V, edges):
        
        in_degree = [0] * V
        adj_list = {i: [] for i in range(V)}
        for u, v in edges:
            adj_list[u].append(v)
            in_degree[v] += 1
        
        queue = deque([i for i in range(V) if in_degree[i] == 0])
        topo_order = []
        
        while queue:
            node = queue.popleft()
            topo_order.append(node)
            
            for nei in adj_list[node]:
                in_degree[nei] -= 1
                if in_degree[nei] == 0:
                    queue.append(nei)
        
        if len(topo_order) == V:
            return topo_order
        else:
            return []
