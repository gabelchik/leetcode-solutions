class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root1 = TreeNode(nums[0])
        if len(nums) == 1:
            return root1
        for i in range(1, (len(nums)+1)//2):
            new_node = TreeNode(nums[i])
            new_node.left = root1
            root1 = new_node
        root2 = TreeNode(nums[(len(nums)+1)//2])
        for i in range((len(nums)+3)//2, len(nums)):
            new_node = TreeNode(nums[i])
            new_node.left = root2
            root2 = new_node
        root1.right = root2
        return root1




class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        return TreeNode(nums[len(nums)//2], self.sortedArrayToBST(nums[:len(nums)//2]), self.sortedArrayToBST(nums[len(nums)//2 + 1:]))
