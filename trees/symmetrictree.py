# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSym(root1, root2):

            if not root1 and root2:
                return False
            if root1 and not root2:
                return False

            if not root1 and not root2:
                return True
            

            return root1.val == root2.val and isSym(root1.left, root2.right) and isSym(root1.right, root2.left)

        return isSym(root.left, root.right)