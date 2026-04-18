class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        combos = list(itertools.combinations(nums, 2))
        for i in range(len(combos)):
            if combos[i][0] + combos[i][1] == target:
                if combos[i][0] == combos[i][1]:
                    return [j for j, x in enumerate(nums) if x == combos[i][0]]
                return nums.index(combos[i][0]), nums.index(combos [i][1])
    # Ineficiente para listas grandes

'''
        caderninho = {} 
        
        for i, num in enumerate(nums): 
            parceiro = target - num
            if parceiro in caderninho:
                return [caderninho[parceiro], i]
            caderninho[num] = i
    # Lê a lista apenas uma vez, ano os valores e os índices
    # Pega o target e subtrai o primeiro número da lista, a variável recebe o nome de 'parceiro'
    # Após, se o número parceiro estiver no dicionário, retorna o índice do primeiro número e o índice de seu parceiro 
    # Caso contrário, anota o número atual e a posição dele no caderno
    
    # Código mais eficiente! Pimba! 