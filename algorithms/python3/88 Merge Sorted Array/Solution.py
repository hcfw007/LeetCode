class Solution:
    def merge(self, nums1, m, nums2, n):
        i = n - 1
        j = len(nums1) - 1
        k = m - 1
        while i >= 0 and k >= 0:
            if nums2[i] >= nums1[k]:
                nums1[j] = nums2[i]
                j -= 1
                i -= 1    
            else:
                nums1[j] = nums1[k]
                j -= 1
                k -= 1
        while i >= 0:
            nums1[j] = nums2[i]
            j -= 1
            i -= 1