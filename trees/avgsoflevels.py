# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        
        q = []
        q.append(root)

        avgs = []

        while q:
            
            n = len(q)
            avg = 0

            for i in range(n):

                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                avg += node.val

            avg = avg / n

            avgs.append(avg)

        return avgs