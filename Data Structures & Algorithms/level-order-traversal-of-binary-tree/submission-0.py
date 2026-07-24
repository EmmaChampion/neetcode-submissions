# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        queue = deque([root])
        result = []
        levelSize = 1
        while queue:
            result.append([])
            nextLevel = 0
            for i in range(levelSize):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    nextLevel += 1
                if node.right:
                    queue.append(node.right)
                    nextLevel += 1
                result[-1].append(node.val)
            levelSize = nextLevel
        return result