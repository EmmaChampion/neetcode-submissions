class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if total % 2 == 1:
            return self.getKth(nums1, nums2, (total + 1) / 2)
        else:
            m1 = self.getKth(nums1, nums2, total / 2)
            m2 = self.getKth(nums1, nums2, total / 2 + 1)
            return (m1 + m2) / 2

    def getKth(self, A, B, k):
        if len(A) > len(B):
            temp = A
            A = B
            B = temp
        if len(A) == 0:
            return B[(int)(k - 1)]
        if k == 1:
            return min(A[0], B[0])
        i = min(len(A), (int)(k // 2))
        j = min(len(B), (int)(k // 2))
        if A[i - 1] <= B[j - 1]:
            return self.getKth(A[i:], B, k - i)
        else:
            return self.getKth(A, B[j:], k - j)


