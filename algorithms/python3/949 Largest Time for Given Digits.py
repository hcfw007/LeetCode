class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        best = -1
        for i in range(4):
            for j in range(4):
                if j == i:
                    continue
                for k in range(4):
                    if k in (i, j):
                        continue
                    for l in range(4):
                        if l in (i, j, k):
                            continue
                        h = arr[i] * 10 + arr[j]
                        mnt = arr[k] * 10 + arr[l]
                        if h < 24 and mnt < 60:
                            best = max(best, h * 60 + mnt)
        if best < 0:
            return ""
        return "{:02d}:{:02d}".format(best // 60, best % 60)
