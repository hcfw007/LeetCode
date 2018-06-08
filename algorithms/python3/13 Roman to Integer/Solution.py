class Solution:
    def romanToInt(self, s):
        map_ = {'I' : 1, 'V': 5, 'X': 10, 'L':50, 'C': 100, 'D': 500, 'M': 1000}        
        if s is None:
            return -1
        if len(s) == 0:
            return -1
        current_index = 0
        res = 0
        while (current_index < len(s)):
            if current_index+1 < len(s):
                if map_[s[current_index]] <  map_[s[current_index+1]]:
                    res +=  map_[s[current_index+1]]- map_[s[current_index]] 
                    current_index += 2
                else:
                    res +=  map_[s[current_index]]
                    current_index += 1
            else:
                res +=  map_[s[current_index]]
                current_index += 1
        return res