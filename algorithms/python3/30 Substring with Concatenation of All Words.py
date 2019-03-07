class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(s) == 0 or len(words) == 0: return []
        word_length = len(words[0])
        total_length = word_length * len(words)
        answers = []
        for i in range(len(s) - total_length + 1):
            substring_words = []
            for j in range(len(words)):
                substring_words.append(s[i + word_length * j: i + word_length * j + word_length])
            all_words = True
            _words = words[:]
            for j in range(len(substring_words)):
                try:
                    _words.remove(substring_words[j])
                except:
                    break
            if len(_words) == 0: answers.append(i)

        return answers