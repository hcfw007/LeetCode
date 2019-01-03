class Solution(object):
    def groupAnagrams(self, strs):
        sortedLetters = []
        words = []
        for i in strs:
            t = list(i)
            t.sort()
            if (t in sortedLetters):
                index = sortedLetters.index(t)
                if (not words[index]):
                    words[index] = []
                words[index].append(i)
            else:
                sortedLetters.append(t)
                tt = []
                tt.append(i)
                words.append(tt)
        return words