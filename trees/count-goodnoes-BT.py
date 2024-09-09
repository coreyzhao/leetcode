# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        
        def dfs(node, max_val):
            if not node:
                return 0
            
           
            if node.val >= max_val:
                good = 1
            else:
                good = 0
            
        
            max_val = max(max_val, node.val)
            
            
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        
        return dfs(root, root.val)
        


        # if not root.right and not root.left:
        #     return 1

        # if root.right and not root.left:
        #     if root.right.right == None and root.right.left == None:
        #         return 1

        # if not root.right and root.left:      
        #     if root.left.right == None and root.left.left == None:
        #         return 1

        # if root.left: 
        #     if root.right:
        #         if root.left.right == None and root.left.left == None and root.right.right == None and root.right.left == None:
        #             return 1


        # if root.right and root.right.val > root.val:
        #     return 1
        # if root.left and root.left.val > root.val:
        #     return 1
        
        