class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

        # Didática do código:
        #  custo = [ 1 ,100, 1 , 1, 1 ,100, 1 , 1 , 100, 1 ]
        #  índices=[ 0,   1, 2 , 3, 4,   5, 6,  7,    8, 9 ]

        # for i in range inicia no 2 e vai até o tamanho do vetor

        # cost[2] = 1 + minímo entre (cost[1], cost[0]) = 1 + 1 = 2
        # cost[3] = 1 + minímo entre (cost[2], cost[1]) = 1 + 2 = 3
        # cost[4] = 1 + minímo entre (cost[3], cost[2]) = 1 + 2 = 3
        # cost[5] = 100 + minímo entre (cost[4], cost[3]) = 1 + 3 = 104
        # cost[6] = 1 + minímo entre (cost[5], cost[4]) = 1 + 3 = 4
        # cost[7] = 1 + minímo entre (cost[6], cost[5]) = 1 + 4 = 5
        # cost[8] = 100 + minímo entre (cost[7], cost[6]) = 100 + 4 = 104
        # cost[9] = 1 + minímo entre (cost[8], cost[7]) = 1 + 5 = 6

        #retunr min(cost[-1], cost[-2]) = return(min(cost[9], cost[8])) == 6
        
