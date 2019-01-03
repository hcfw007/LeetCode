class Solution:
    def search(self, nums, target):   
        first, last = 0, len(nums)
        while (first != last):
            mid = first + int((last - first) / 2)
            if (nums[mid] == target): return mid
            if (nums[first] <= nums[mid]):
                if (nums[first] <= target and target < nums[mid]):
                    last = mid
                else:
                    first = mid + 1
            else:
                if (nums[mid] < target and target <= nums[last-1]):
                    first = mid + 1
                else:
                    last = mid
        return -1