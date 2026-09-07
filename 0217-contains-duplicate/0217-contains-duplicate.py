class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums_dupl = set()

        for num in nums:
            # Tempo de busca O(1)
            if num in nums_dupl:
                return True
            
            nums_dupl.add(num)

        return False

        '''
        # Opção extremamente rápida porque a conversão ocorre diretamente em C por baixo dos panos
        
        return len(nums) != len(set(nums))
        '''