# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        temp = TreeNode(root.val)
        temp.left = self.invertTree(root.right)
        temp.right = self.invertTree(root.left)
        return temp
    

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invTree(root):
            if not root:
                return

            og_left = root.left
            root.left = root.right
            root.right = og_left
            
            invTree(root.left)
            invTree(root.right)

        invTree(root)
        return root