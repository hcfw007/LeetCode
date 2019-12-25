from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        return "".join(ch * cnt for ch, cnt in Counter(s).most_common())
