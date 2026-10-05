// The API isBadVersion is defined for you.
// bool isBadVersion(int version);

class Solution {
public:
    int firstBadVersion(int n) {
        int a = 1;         
        int b = n;         
        int resposta = n;          
        while (a <= b) {             
            int k = a + (b - a) / 2;              
            if (isBadVersion(k)) {                 
                resposta = k;                 
                b = k - 1;             
            } else {                 
                a = k + 1;             
            }         
        }          
        return resposta;     
        } 
    }
;