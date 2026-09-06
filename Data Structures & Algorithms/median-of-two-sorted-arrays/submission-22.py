class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        half = (len(A) + len(B)) // 2

        right = len(A)-1
        left = 0
        while True:
            mid = (left + right) // 2

            a1 = A[mid] if mid >= 0 else float('-inf')
            a2 = A[mid+1] if (mid+1) < len(A) else float('inf')
            b1 = B[half-mid-2] if (half-mid-2) >= 0 else float('-inf')
            b2 = B[half-mid-1] if (half-mid-1) < len(B) else float('inf')

            if a1 <= b2 and b1 <= a2:
                if (len(A)+len(B)) % 2 == 0:
                    return (max(a1, b1) + min(a2, b2)) / 2
                return min(a2, b2)
            elif a1 > b2:#
                right = mid - 1
            else:
                left = mid + 1



        