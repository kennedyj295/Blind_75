
from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def maxDepth(self, root):
        checker = deque()

        if root:
            checker.append(root)
        level = 0

        while checker:
            for i in range(len(checker)):
                curr = checker.popleft()

                if curr.right:
                    checker.append(curr.right)
                if curr.left:
                    checker.append(curr.left)
            level += 1

        return level


