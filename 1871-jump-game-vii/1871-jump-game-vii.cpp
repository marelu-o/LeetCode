class Solution {
public:
    bool canReach(string s, int minJump, int maxJump) {
        queue<int> q;
        q.push(0);
        
        int mais_longe = 0;
        int n = s.length();

        
        if (s.back() == '1') {
            return false;
        }
        if (maxJump == n - 1) {
            return true;
        }

        while (!q.empty()) {
            int i = q.front(); // Pega o primeiro elemento
            q.pop();           // Remove o primeiro elemento 

            
            int comeco = max(i + minJump, mais_longe + 1);
            
            // Calcula o limite do loop 
            int limite = min(i + maxJump + 1, n);

            for (int j = comeco; j < limite; ++j) {
                if (s[j] == '0') {
                    q.push(j);
                    if (j == n - 1) {
                        return true;
                    }
                }
            }
            
            mais_longe = i + maxJump;
        }

        return false;
    }
};