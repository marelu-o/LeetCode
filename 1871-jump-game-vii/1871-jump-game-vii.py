class Solution(object):
    def canReach(self, s, minJump, maxJump):
        q = deque([0])
        mais_longe = 0
        if s[-1]=='1':
            return False
        if maxJump == len(s) - 1:
            return True
        while q:
            i = q.popleft()
            comeco = max(i + minJump, mais_longe + 1)

            for j in range (comeco, min(i + maxJump + 1, len(s))):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) - 1:
                        return True
            mais_longe = i + maxJump
        return False
