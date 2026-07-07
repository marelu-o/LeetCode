class Solution(object):
    def canReach(self, arr, start):
        return self.buscaProf(arr, start, 0)
    

    def buscaProf(self, arr, start, contador):
        if start < 0 or start >= len(arr):
            return False
        if contador >= len(arr):
            return False
        if arr[start] == 0:
            return True

        return self.buscaProf(arr, start + arr[start], contador + 1) or \
               self.buscaProf(arr, start - arr[start], contador + 1)
    
    
    
