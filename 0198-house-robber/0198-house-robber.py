class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            nums[i] = max (nums[i] + nums[i - 2], nums[i - 1 ])
        return nums[len(nums) - 1]  

# Didática do código:
        #  nums = [ 2, 7, 9, 3, 1 ]
        #  índices=[0, 1, 2, 3, 4 ]

        #  if len(nums) == 1: -> Se o tamanho do vetor for igual à 1, retorna o único valor  presente no vetor.
        
        # nums[1] = max(nums[0], nums[1]) -> O índice 1 recebe o maior valor entre o índice 0 e o índice 1 (Ótimo para vetores de apenas 2 índices, 0 e 1);

        # for i in range(2, len(nums)): -> Inicia no segundo índice e vai adiante

        # nums[2] = máximo entre (nums[2] + nums [0], nums[1]) = (9 + 2, 7) = 11
        # nums[3] = máximo entre (nums[3] + nums [1], nums[2]) = (3 + 7, 11) = 11
        # nums[4] = máximo entre (nums[4] + nums [2], nums[3]) = (1 + 11, 11) = 12
        
        # return nums[len(nums) - 1]  -> retorna o último valor presente na lista = nums[4] = 12
