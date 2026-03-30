class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        pointer_1 = m - 1
        pointer_2 = n - 1
        pointer_3 = m + n - 1

        while pointer_1 >= 0 and pointer_2 >= 0:
            if nums1[pointer_1] >= nums2[pointer_2]:
                nums1[pointer_3] = nums1[pointer_1]
                pointer_1 -= 1
            else:
                nums1[pointer_3] = nums2[pointer_2]
                pointer_2 -= 1
            pointer_3 -= 1

        # ⚠️ critical missing piece
        while pointer_2 >= 0:
            nums1[pointer_3] = nums2[pointer_2]
            pointer_2 -= 1
            pointer_3 -= 1





        


        