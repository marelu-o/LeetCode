class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
       # O(n²)
        '''
        nums3 = set()
        for i in range(len(nums1)):
            if nums1[i] in nums2:
                    nums3.add(nums1[i])
        return list(nums3)
        '''


        # O(1) : tabela hash
        return list(set(nums1) & set(nums2))