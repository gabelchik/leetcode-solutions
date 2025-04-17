class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return False
        dict = {}
        for i in range(len(nums)):
            if dict.get(nums[i]) is None:
                dict[nums[i]] = 1
            else:
                return True

        return False
