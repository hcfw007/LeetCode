class Solution:
    def compress(self, chars: List[str]) -> int:
        write = 0
        i = 0
        n = len(chars)
        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            chars[write] = chars[i]
            write += 1
            count = j - i
            if count > 1:
                for d in str(count):
                    chars[write] = d
                    write += 1
            i = j
        return write
