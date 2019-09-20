class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while i + 1 < n and nums[i + 1] == nums[i] + 1:
                i += 1
            if nums[i] == start:
                ans.append(str(start))
            else:
                ans.append("{}->{}".format(start, nums[i]))
            i += 1
        return ans
