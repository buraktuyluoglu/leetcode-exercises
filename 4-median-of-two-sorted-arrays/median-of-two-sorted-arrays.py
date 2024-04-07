class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        l = len(nums1)
        nums1.sort()    
        if l % 2 == 0:
            return (nums1[l//2] + nums1[l//2 - 1])/2
        else:
            return nums1[l//2]
