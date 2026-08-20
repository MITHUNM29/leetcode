class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        nums1=[nums[0]]
        nums2=[nums[1]]
        for ch in range(2,len(nums)):
            if nums1[-1]>nums2[-1]:
                nums1.append(nums[ch])
            else:
                nums2.append(nums[ch])
        return nums1 +nums2            