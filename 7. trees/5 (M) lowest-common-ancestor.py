from typing import Optional
from common import TreeNode
from common import print_tree

# This is a BST

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current:
            # Case where both number are greater than root => LCA has to be in right
            if p.val > current.val and q.val > current.val:
                current = current.right

            # Case where both number are less than root => LCA has to be in left
            elif p.val < current.val and q.val < current.val:
                current = current.left

            # Two cases: 1) If one num is greater than current, and one is less than current => current is LCA
            # 2) If one of the number matches the root, then current is LCA
            else:
                return current
