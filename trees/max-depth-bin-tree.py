# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) 
    


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def maxDep(root, count, cur):
            
            if not root:
                cur = max(count, cur)
                return cur

            count += 1
            cur_max = max(maxDep(root.left, count, cur), maxDep(root.right, count, cur))
            count -= 1

            return cur_max

        return maxDep(root, 0, 0)

            

            
