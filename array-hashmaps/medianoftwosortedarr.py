class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            A = nums2
            B = nums1
        else:
            A = nums1
            B = nums2

        length = len(nums1) + len(nums2)
        half = length // 2

        l = 0
        r = len(A) - 1
        while (True):
            m1 = (l + r) // 2
            m2 = half - m1 - 2
            
            Aleft = A[m1] if m1 >= 0 else float("-inf")
            Aright = A[m1 + 1] if m1 + 1 < len(A) else float("inf")
            Bleft = B[m2] if m2 >= 0 else float("-inf")
            Bright = B[m2 + 1] if m2 + 1 < len(B) else float("inf")

            
            if Aleft <= Bright and Bleft <= Aright:
                if length % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                else:
                    return min(Aright, Bright)

            elif Aleft > Bright:
                r = m1 - 1
            else:
                l = m1 + 1
        