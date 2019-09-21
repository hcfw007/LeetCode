class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1 = c2 = None
        n1 = n2 = 0
        for num in nums:
            if c1 is not None and num == c1:
                n1 += 1
            elif c2 is not None and num == c2:
                n2 += 1
            elif n1 == 0:
                c1, n1 = num, 1
            elif n2 == 0:
                c2, n2 = num, 1
            else:
                n1 -= 1
                n2 -= 1
        r1 = r2 = 0
        for num in nums:
            if num == c1:
                r1 += 1
            elif num == c2:
                r2 += 1
        ans = []
        if r1 > len(nums) // 3:
            ans.append(c1)
        if r2 > len(nums) // 3:
            ans.append(c2)
        return sorted(ans)
