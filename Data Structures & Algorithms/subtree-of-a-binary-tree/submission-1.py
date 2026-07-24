# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                continue
            if node.val == subRoot.val:
                if self.isMatch(node, subRoot):
                    return True
            queue.append(node.left)
            queue.append(node.right)
        return False
    
    def isMatch(self, mainRoot, subRoot):
        main = deque([mainRoot])
        sub = deque([subRoot])
        while sub:
            first = main.popleft()
            second = sub.popleft()
            if not first and not second:
                continue
            if not first or not second:
                return False
            if first.val != second.val:
                return False
            main.append(first.left)
            main.append(first.right)
            sub.append(second.left)
            sub.append(second.right)
        if main:
            return False
        else:
            return True