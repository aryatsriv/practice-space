class Solution:


    def rotateStringOpt(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in (s + s)



    def rotateString(self, s: str, goal: str) -> bool:
        m,n=len(s),len(goal)
        if m!=n:
            return False

        for i in range(n):
            if s[0]==goal[i]:
                k=i
                isRotated=False
                for j in range(0,m):
                    if s[j]!=goal[(i+j)%n]:
                            isRotated=False
                            break
                    isRotated=True
                if isRotated:
                    return True
        

        return False
