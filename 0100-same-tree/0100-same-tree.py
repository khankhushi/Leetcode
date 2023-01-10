# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preOrder(self,a,l):
        if not a:
            l.append(None)
        else:
            l.append(a.val)
            self.preOrder(a.left,l)
            self.preOrder(a.right,l)
        return l
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        pl=self.preOrder(p,[])
        ql=self.preOrder(q,[])
        return(pl==ql)