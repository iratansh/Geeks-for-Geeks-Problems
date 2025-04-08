#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        visited = set()
        stack = [0]
        res = []
        
        while stack:
            node = stack.pop()
            
            if node not in visited:
                visited.add(node)
                res.append(node)
                
                for nei in reversed(adj[node]):
                    if nei not in visited:
                        stack.append(nei)
    
        return res
