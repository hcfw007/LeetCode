class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        first = second = third = None
        for num in nums:
            if num == first or num == second or num == third:
                continue
            if first is None or num > first:
                first, second, third = num, first, second
            elif second is None or num > second:
                second, third = num, second
            elif third is None or num > third:
                third = num
        return third if third is not None else first
