class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums)[-k:]

    def add(self, val: int) -> int:
        lo, hi = 0, len(self.nums)
        while lo < hi:
            mid = (lo + hi) // 2
            if self.nums[mid] < val:
                lo = mid + 1
            else:
                hi = mid
        self.nums.insert(lo, val)
        if len(self.nums) > self.k:
            self.nums.pop(0)
        return self.nums[0]
