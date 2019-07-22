class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        first, last = 0, len(nums) - 1
        while first <= last:
            while first < len(nums) - 1 and nums[first] == nums[first + 1]:
                first += 1
            while last > 1 and nums[last] == nums[last - 1]:
                last -= 1
            mid = first + int((last - first) / 2)
            if (nums[mid] == target): return True
            if (nums[first] <= nums[mid]):
                if (nums[first] <= target and target < nums[mid]):
                    last = mid
                else:
                    first = mid + 1
            else:
                if (nums[mid] < target and target <= nums[last]):
                    first = mid + 1
                else:
                    last = mid
        return False