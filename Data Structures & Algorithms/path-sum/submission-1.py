# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
            traverse through all paths. base case is when root == None
            stop and return true if you stumble upon path quicker
            otherwise keep recursing 
        '''
       
        def dfs(root, currSum):
            if not root:
                return False
            currSum += root.val

            if not root.left and not root.right: 
                return currSum == targetSum
            return dfs(root.left, currSum) or dfs(root.right, currSum)

        return dfs(root, 0)