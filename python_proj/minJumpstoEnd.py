#User function Template for python3
import sys
import heapq 

class AttempAction:
    cur: int 
    steps: int 
    def __init__(self, p, step=0) -> None:
        self.cur = p
        self.steps = step
    
    def __lt__(self, other) -> bool:
        if self.steps == other.steps:
            return self.cur > other.cur
        return self.steps < other.steps
    
class Solution:
    def minJumps(self, arr, n):
        far, near, step = 1, 0, 0
        while far < n:
            if near >= far:
                return -1
            last_far = far
            for i in range(near, far):
                if arr[i] == 0:
                    continue
                if arr[i]+i+1 > far:
                    far = arr[i]+i+1
            near = last_far
            step +=1 
        return step

    def minJumps1(self, arr, n):
        heap = [AttempAction(0)]
        procd = [False]*n
        while len(heap) > 0:
            prio = heapq.heappop(heap)
            procd[prio.cur] = True
            for d in range(arr[prio.cur], 0, -1):
                if d+prio.cur >= n-1:
                    return prio.steps+1
                if arr[d+prio.cur] > 0:
                    if procd[prio.cur+d]:
                        continue
                    heapq.heappush(heap, AttempAction(prio.cur+d, prio.steps+1))
        return -1

    def minJumps2(self, arr, n):
	    #code here
        inf = sys.maxsize//2
        if arr[0] == 0:
            return -1
        jumps_dp = [inf]*n
        if arr[n-1] > 0:
            jumps_dp[n-1] = 0
        for j in range(n-2, -1, -1):
            # jumps_dp[j] = min(jumps_dp[all avail pos])
            if arr[j] == 0:
                continue
            for d in range(arr[j], 0, -1):
                if j+d >= n-1:
                    jumps_dp[j] = 1
                    break
                if jumps_dp[j] > 1+jumps_dp[j+d]:
                    jumps_dp[j] = 1+jumps_dp[j+d]
            
        if jumps_dp[0] >= inf:
            return -1
        else:
            return jumps_dp[0]
    

if __name__ == "__main__":
    sol = Solution()

    arr = [1,3,5,8,9,2,6,7,6,8,9] 
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # 3

    arr = [1, 4, 3, 2, 6, 7]
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # 2
    
    arr = [0, 1, 1, 1, 1]
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # -1

    arr = [1, 5, 3, 5, 6, 1,1,1,2]
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # 3

    arr = [2, 3, 1, 1, 2, 4, 2, 0, 1, 1]
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # 4

    arr = [10] + [0]*10
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # 1

    arr = [2, 1, 0, 3]
    print("sol of input:", arr, sol.minJumps(arr, len(arr))) # -1