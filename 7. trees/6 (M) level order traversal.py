from collections import deque
from typing import Optional
from common import TreeNode
from common import print_tree

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        queue = deque([root, 1])

        answer = []

        level = 0

        while deque:
            curr = queue.popleft()

            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)

            if len(answer) < level + 1:
                answer.append([curr.val])
            else:
                answer.insert(level, answer[level].extend(curr.val))

            level += 1

        return answer



