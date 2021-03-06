class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        index = m + n - 1
        while j >= 0:
            if i>=0 and nums1[i] > nums2[j]:
                nums1[index] = nums1[i]
                i -= 1
                index -= 1
            else:
                nums1[index] = nums2[j]
                j -= 1
                index -= 1