class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        permutations = []
        nums.sort()
        self.generatePermutation([], nums, permutations)
        return permutations
    
    def generatePermutation(self, permutation, leftover, permutations):
        if (len(leftover) == 0):
            permutations.append(permutation)
        else:
            for i in range(len(leftover)):
                if i != 0 and leftover[i] == leftover[i - 1]: continue
                t = permutation[:]
                t.append(leftover[i])
                t_left = leftover[:]
                t_left.pop(i)
                self.generatePermutation(t, t_left, permutations)