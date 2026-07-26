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
        result = ""
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if not node:
                result = result + "$null"
            else:
                result = result + "$" + str(node.val)
                queue.append(node.left)
                queue.append(node.right)
        #Remove first $
        if len(result) > 1:
            result = result[1:]
        return result
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if data == "":
            return None
        arr = data.split("$")
        root = TreeNode(arr[0])
        queue = deque([root])

        i = 1
        arr_len = len(arr)
        while queue and i < arr_len:
            curr = queue.popleft()

            if i < arr_len:
                if arr[i] != "null":
                    curr.left = TreeNode(arr[i])
                    queue.append(curr.left)
                i += 1
            
            if i < arr_len:
                if arr[i] != "null":
                    curr.right = TreeNode(arr[i])
                    queue.append(curr.right)
                i += 1
        return root