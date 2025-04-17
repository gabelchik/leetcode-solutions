class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter = {}
        for i in range(len(nums1)):
            if counter.get(nums1[i]) is None:
                counter[nums1[i]] = 1
            else:
                counter[nums1[i]] += 1
        j = 0
        for i in range(len(nums2)):
            if counter.get(nums2[i], 0) == 0:
                continue
            else:
                nums1[j] = nums2[i]
                counter[nums2[i]] -= 1
                j+=1
        return nums1[:j]
