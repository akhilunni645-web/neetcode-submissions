class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        # Always binary search on the smaller array
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A

        total = len(A) + len(B)
        half = total // 2

        left = 0
        right = len(A)

        while True:

            # Partition index in A
            i = (left + right) // 2

            # Partition index in B
            j = half - i

            # Left and Right values around partition
            Aleft = A[i - 1] if i > 0 else float("-inf")
            Aright = A[i] if i < len(A) else float("inf")

            Bleft = B[j - 1] if j > 0 else float("-inf")
            Bright = B[j] if j < len(B) else float("inf")

            # Correct partition found
            if Aleft <= Bright and Bleft <= Aright:

                # Odd number of elements
                if total % 2:
                    return min(Aright, Bright)

                # Even number of elements
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2

            # Move search to the left
            elif Aleft > Bright:
                right = i - 1

            # Move search to the right
            else:
                left = i + 1