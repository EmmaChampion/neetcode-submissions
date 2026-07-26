# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def buildLevel(preorder, inorder):
            if not preorder or not inorder:
                return None
            rootVal = preorder[0]
            leftVals = inorder[0 : inorder.index(rootVal)]
            rightVals = inorder[inorder.index(rootVal) + 1 : ]
            root = TreeNode(rootVal)
            preLeft = []
            preRight = []
            for val in preorder:
                if val in leftVals:
                    preLeft.append(val)
                elif val in rightVals:
                    preRight.append(val)
            root.left = buildLevel(preLeft, leftVals)
            root.right = buildLevel(preRight, rightVals)
            return root
        
        return buildLevel(preorder, inorder)