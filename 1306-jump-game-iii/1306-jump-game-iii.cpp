class Solution {
public:
    bool canReach(vector<int>& arr, int start) {
        queue <int> q;
        q.push(start);

        while (!q.empty()){
            int atual = q.front();
            q.pop();

            if (arr[atual] == 0 ){
                return true;
            }

            // verifica se a posição atual já foi visitada anteriormente
            if (arr[atual] < 0){
                // caso já tenha sido verificada anteriormente
                // continua toda a operação
                continue;
            }

            // verifica se está dentro dos limites do array
            // verifica à direita
            if(atual + arr[atual] < arr.size()){
                //adiciona a fila 'q' a nova posição a analisar
                q.push(atual + arr[atual]);
            }

            // verifica se está dentro dos limites do array
            // verifica à esquerda
            if(atual - arr[atual] >= 0){
                //adiciona a fila 'q' a nova posição a analisar
                q.push(atual - arr[atual]);
            }

            // marca que aquela posição já foi visitada 
            arr[atual] = -arr[atual];
        }

        return false;

    }
};