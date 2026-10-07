class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        m -= 1
        n -= 1

        tp = n + m + 1

        while (tp != -1):
            if n == -1:
                nums1[tp] = nums1[m]
                m -= 1
            
            elif m == -1:
                nums1[tp] = nums2[n]
                n -= 1

            elif nums1[m] > nums2[n]:
                nums1[tp] = nums1[m]
                m -= 1

            else:
                nums1[tp] = nums2[n]
                n -= 1

            tp -= 1