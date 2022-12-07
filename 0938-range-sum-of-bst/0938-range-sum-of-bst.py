# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
            def dfsBST(node):
                if not node: return
                
                if low <= node.val <= high:
                    self.out += node.val
                if node.val > low: dfsBST(node.left)
                if node.val < high: dfsBST(node.right)
            self.out = 0
            dfsBST(root)
            return self.out
        
        