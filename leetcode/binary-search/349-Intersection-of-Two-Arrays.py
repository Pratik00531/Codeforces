class Solution(object):
    def intersection(self, nums1, nums2):
        c = []
        for i in range(len(nums1)):
            if nums1[i] in nums2 : 
                c.append(nums1[i])
        l = set(c)
        return list(l)
        