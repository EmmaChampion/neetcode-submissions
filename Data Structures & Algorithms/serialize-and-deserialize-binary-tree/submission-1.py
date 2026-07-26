# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        result = []
        
        def dfs(node):
            if not node:
                result.append("null")
            else:
                result.append(str(node.val))
                dfs(node.left)
                dfs(node.right)
        dfs(root)

        resStr = "$".join(result)
        return resStr
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = data.split("$")
        root = TreeNode(arr[0])
        i = 0

        def dfs(arr):
            nonlocal i

            if arr[i] == "null":
                i += 1
                return None
            node = TreeNode(arr[i])
            i += 1
            node.left = dfs(arr)
            node.right = dfs(arr)
            return node
        return dfs(arr)