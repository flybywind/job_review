# https://practice.geeksforgeeks.org/problems/the-celebrity-problem/1?page=1&difficulty[]=1&sortBy=difficulty
class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        isCelebrity = [True] * n

        def _scane_one(r):
            row = M[r]
            for i, know in enumerate(row):
                if know == 1:
                    # r knows i
                    isCelebrity[r] = False
                    #
                else:
                    if i != cur:
                        isCelebrity[i] = False

        cur = 0
        while cur < n:
            _scane_one(cur)
            if isCelebrity[cur]:
                for i in range(n):
                    if i != cur:
                        if M[i][cur] != 1:
                            return -1
                return cur
            if cur == n - 1:
                return -1
            s = cur+1
            cur = n
            for i in range(s, n):
                if isCelebrity[i]:
                    cur = i
                    break

        return -1


sol = Solution()
M = [[0, 1],
     [1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 1, 0],
     [0, 0, 0],
     [0, 1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 1, 1],
     [0, 0, 0],
     [0, 1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 1, 1],
     [1, 0, 0],
     [0, 1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 0, 0],
     [0, 0, 0],
     [0, 1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 1, 1, 0],
     [1, 0, 1, 1],
     [0, 0, 0, 0],
     [1, 1, 1, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")

M = [[0, 1, 1, 0],
     [1, 0, 0, 1],
     [0, 0, 0, 0],
     [1, 1, 0, 0]]
N = len(M)
print(f"{sol.celebrity(M, N)}th person is the celebrity of community {M}")
