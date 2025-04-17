class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        count = {}
        for i in range(len(nums)):
            if count.get(nums[i]) is None:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        for key, value in count.items():
            if value == 1:
                return key
