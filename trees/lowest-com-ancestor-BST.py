# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while True:
            if p.val <= root.val and root.val <= q.val:
                return root
            elif q.val <= root.val and root.val <= p.val:
                return root

            if p.val < root.val and q.val < root.val:
                root = root.left
            else:
                root = root.right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if p.val > q.val:
            temp = p
            p = q
            q = temp

        def findLCA(root, p, q):
            print(p.val, q.val)
            if p.val <= root.val and q.val >= root.val:
                return root

            else:
                if p.val < root.val and q.val < root.val:
                    return findLCA(root.left, p, q)
                else:
                    return findLCA(root.right, p , q)

        return findLCA(root, p, q)

        