from collections import deque
from typing import Optional
from common import TreeNode
from common import print_tree


class Solution:
    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return 1 + max(self.maxDepthDFS(root.left), self.maxDepthDFS(root.right))

    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:

        queue = deque([root])
        level = 0
        while queue:

            for i in range(len(queue)):
                node = queue.popleft()

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return level

    def DFSIterative(self, root: Optional[TreeNode]) -> int:
        # Uses Stack
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])

        return res




t = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))

# t = TreeNode(1, None, TreeNode(2))

print(Solution().maxDepthBFS(t))
