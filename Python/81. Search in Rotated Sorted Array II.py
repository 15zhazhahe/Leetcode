class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        l, r = 0, len(nums)-1
        while l <= r:
            mid = (r-l) // 2 + l
            if nums[mid] == target:
                return True
            if nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid-1
                else:
                    l = mid+1
            elif nums[mid] < nums[l]:
                if nums[mid] < target <= nums[r]:
                    l = mid+1
                else:
                    r = mid-1
            else:
                l += 1
        return False