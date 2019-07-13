class Solution:
    def sortColors(self, nums: List[int]) -> None:
        zero, two, p = 0, len(nums) - 1, 0
        while p <= two:
            if nums[p] == 0:
                nums[p], nums[zero] = nums[zero], nums[p]
                zero += 1
                p += 1
            elif nums[p] == 1:
                p += 1
            else:
                nums[p], nums[two] = nums[two], nums[p]
                two -= 1