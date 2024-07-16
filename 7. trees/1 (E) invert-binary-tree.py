# Definition for a binary tree node.
from typing import Optional
from common import TreeNode
from common import print_tree


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right:
            return root

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root


# root = TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None))
root = TreeNode(4,
                TreeNode(2, TreeNode(1, None, None), TreeNode(3, None, None)),
                TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None))
                )

sol = Solution()

print_tree(root)

print(print_tree(sol.invertTree(root)))

