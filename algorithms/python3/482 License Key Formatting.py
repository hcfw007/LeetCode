class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        chars = s.replace("-", "").upper()
        groups = []
        first = len(chars) % k
        if first:
            groups.append(chars[:first])
        for i in range(first, len(chars), k):
            groups.append(chars[i:i + k])
        return "-".join(groups)
