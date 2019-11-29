class Solution:
    def __init__(self, nums: List[int]):
        self.positions = {}
        for i, num in enumerate(nums):
            self.positions.setdefault(num, []).append(i)
        self.seed = 1

    def pick(self, target: int) -> int:
        self.seed = (self.seed * 1103515245 + 12345) % 2147483648
        idxs = self.positions[target]
        return idxs[self.seed % len(idxs)]
