from typing import Optional, List
from common import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Can we maintain max value till that point?
        if not root:
            return 0
        return self.dfs(root, root.val)

    def dfs(self, node, maxTillNow):
        if not node:
            return 0
        count = 0
        if node.val >= maxTillNow:
            count = 1
            maxTillNow = node.val

        count += self.dfs(node.left, maxTillNow)
        count += self.dfs(node.right, maxTillNow)

        return count
        # return count


t = TreeNode(3, TreeNode(1, TreeNode(3), None), TreeNode(4, TreeNode(1), TreeNode(5)))

print(Solution().goodNodes(t))