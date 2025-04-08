import collections

#User function Template for python3
class Solution:
    # Function to return Breadth First Search Traversal of given graph.
    def bfs(self, adj):
         # to do bfs on a graph at vertex 0 with adj list representation, 
         # need to use a queue to hold the neighbors of each current node
         
        res = []
        q = collections.deque([0])
        visited = set()
         
        while q:
            vertex = q.popleft()
            visited.add(vertex)
            res.append(vertex)
             
            for i in range(len(adj[vertex])):
                if adj[vertex][i] not in visited:# append vertex neigbors
                    q.append(adj[vertex][i])
                    visited.add(adj[vertex][i])
        return res
