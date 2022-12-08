# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # doing dfs because bfs won't maintain the order we want of leaf nodes
        def LVseq(root):
            if root.right is None and root.left is None:
                return  [root.val]
            
            if root.right is not None and root.left is not None:
                return LVseq(root.left) + LVseq(root.right)
            
            if root.left is None:
                return LVseq(root.right)
            
            if root.right is None:
                return LVseq(root.left)
            
        if LVseq(root1)== LVseq(root2):
            return True
        else: return False