from collections import deque

class Solution:
    def bottomView(self, root): 
        if not root:
            return []
    
        horiDist = {}
        q = deque([(root, 0)]) # choose bfs because we need to process through each level
        while q:
            curr, hd = q.popleft()
            horiDist[hd] = curr.data

            if curr.left:
                q.append((curr.left, hd - 1))
            if curr.right:
                q.append((curr.right, hd + 1))
    
        result = [horiDist[hd] for hd in sorted(horiDist)]
        
        return result
