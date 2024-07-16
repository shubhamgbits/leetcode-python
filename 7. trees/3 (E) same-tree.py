from collections import deque
from typing import Optional
from common import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        if (p and not q) or (q and not p):
            return False

        if p == q:
            return True

        if p == q:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return False
