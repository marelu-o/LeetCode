class Solution(object):
    def canReach(self, arr, start):
        return self.buscaProf(arr, start, 0)
    

    # Solução recursiva
    def buscaProf(self, arr, start, contador):
        # Caso start menor que 0 ou satart maior que o tamanho do array
        # Retorna False
        if start < 0 or start >= len(arr):
            return False
        
        # Caso o contador (inicialmente == 0) maior ou igual ao tamanho do array
        # Retorna False
        if contador >= len(arr):
            return False
    
        # Caso o arr[start] == 0
        # Retorna True
        if arr[start] == 0:
            return True

        # Retorna buscando pela direita ou pela esquerda caso nenhum dos casos acima seja verdadeiro
        return self.buscaProf(arr, start + arr[start], contador + 1) or \
               self.buscaProf(arr, start - arr[start], contador + 1)
    
    
    
