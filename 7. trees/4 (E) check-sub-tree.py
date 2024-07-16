from collections import deque
from typing import Optional
from common import TreeNode
from common import print_tree


def isSubtree(root, subRoot):
    if not root and not subRoot:
        return True
    if not root or not subRoot:
        return False

    if checkSubTree(root, subRoot):
        return True
    else:
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)


def checkSubTree(root1, root2):
    if not root1 and not root2:
        return True

    if not root1 or not root2 or (root1.val != root2.val):
        return False

    return checkSubTree(root1.left, root2.left) or checkSubTree(root1.right, root2.right)


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        if not root or not subRoot:
            return False

        if self.checkSubTree(root, subRoot):
            return True
        else:
            return self.isSubtree(root.left, subRoot) and self.isSubtree(root.right, subRoot)

    def checkSubTree(self, root1, root2):
        if not root1 and not root2:
            return True

        if not root1 or not root2 or root1.val != root2.val:
            return False

        return self.checkSubTree(root1.left, root2.left) and self.checkSubTree(root1.right, root2.right)


r1 = TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)), TreeNode(5))
r2 = TreeNode(4, TreeNode(1), TreeNode(2))

print_tree(r1)
print_tree(r2)

# sol = Solution()
# print(sol.checkSubTree(r1, r2))

print(isSubtree(r1, r2))
