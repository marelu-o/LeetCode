class Solution:
    def isValid(self, s: str) -> bool:
        pilha = []
        ok = True
        for i in range(len(s)):
            c = s[i]
            if c == "{" or c == "[" or c == "(":
                pilha.append(c)
            else:
                if len(pilha) == 0:
                    ok = False
                    break
                elif c == "}" and pilha[-1] != "{":
                    ok = False
                elif c == ")" and pilha[-1] != "(":
                    ok = False
                elif c == "]" and pilha[-1] != "[":
                    ok = False
                pilha.pop()

        if len(pilha) == 0 and ok == True:
            return True
        else:
            return False