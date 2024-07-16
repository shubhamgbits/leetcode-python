from collections import deque
from typing import Optional, List
from common import TreeNode
from common import print_tree


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        return self.dfs(root, [])

    def dfs(self, node: Optional[TreeNode], rightView: Optional[List]):

        if not node:
            return

        if not node.right and not node.left:
            rightView.append(node.val)

        if not node.right:
            return self.dfs(node.left, rightView)

        rightView.extend(self.dfs(node.right, rightView))

    def bfs(self, root: Optional[TreeNode]) -> List[int]:

        level = 0
        queue = deque([root])
        answer = []
        while queue:
            rightMost = None
            q_len = len(queue) - 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if i == q_len:
                    rightMost = node.val
            if rightMost is not None:
                answer.append(rightMost)

        return answer


t = TreeNode(1, TreeNode(2, None, TreeNode(5)), TreeNode(3, TreeNode(None, TreeNode(4))))

print(Solution().bfs(t))
