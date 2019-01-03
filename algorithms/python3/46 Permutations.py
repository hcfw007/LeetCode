class Solution:
    def permute(self, nums):
        permutations = []
        self.generatePermutation([], nums, permutations)
        return permutations
    
    def generatePermutation(self, permutation, leftover, permutations):
        if (len(leftover) == 0):
            permutations.append(permutation)
        else:
            for i in range(len(leftover)):
                t = permutation[:]
                t.append(leftover[i])
                t_left = leftover[:]
                t_left.pop(i)
                self.generatePermutation(t, t_left, permutations)