class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)
        half_len = (m + n + 1) // 2
        low, high = 0, m
        
        while low <= high:
            i = low + (high - low) // 2
            j = half_len - i
            L1 = nums1[i - 1] if i > 0 else float('-inf')
            R1 = nums1[i] if i < m else float('inf')
            L2 = nums2[j - 1] if j > 0 else float('-inf')
            R2 = nums2[j] if j < n else float('inf')
            if L1 <= R2 and L2 <= R1:
                if (m + n) % 2 == 1:
                    return float(max(L1, L2))
                else:
                    return (max(L1, L2) + min(R1, R2)) / 2.0
            elif L1 > R2:
                high = i - 1
            else:
                low = i + 1
        return 0.0      