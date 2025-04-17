class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums or k == 0:
            return
        k %= len(nums)
        if k == 0:
            return

        nums.reverse()

        (i, j) = (0, k-1)
        while i < j:
            (nums[i], nums[j]) = (nums[j], nums[i])
            i+=1
            j-=1

        (i, j) = (k, len(nums)-1)
        while i < j:
            (nums[i], nums[j]) = (nums[j], nums[i])
            i+=1
            j-=1
