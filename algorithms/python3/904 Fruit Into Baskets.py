class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        count = {}
        left = 0
        best = 0
        for right, f in enumerate(fruits):
            count[f] = count.get(f, 0) + 1
            while len(count) > 2:
                left_f = fruits[left]
                count[left_f] -= 1
                if count[left_f] == 0:
                    del count[left_f]
                left += 1
            best = max(best, right - left + 1)
        return best
