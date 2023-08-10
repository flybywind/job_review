from typing import List
def solution(A, F, M):
    # Implement your solution here
    def check_valid(ret: List[int]) -> bool:
        return not (len(ret) == 1 and ret[0] == 0)
    def round(v) -> int:
        if v - int(v) > 0.5:
            return int(v+1)
        else:
            return int(v)
    def findPosibleSum(S, cur_res:List[int], res_sum:int) -> List[int]:
        leftNum = F - len(cur_res)
        leftSum = S - res_sum 
        if leftNum == 0 and leftSum == 0:
            return cur_res
        
        mean = round(leftSum/leftNum)
        for i in [0, -1, -2, -3, 1, 2, 3]:
            # search around mean
            m = mean + i
            if m > 6 or m < 1:
                continue
            next_res = findPosibleSum(S, cur_res+[m], res_sum+m)
            if check_valid(next_res):
                return next_res
        return [0]
    
    ss = M*(len(A)+F) - sum(A)
    mm = ss/F 
    if mm > 6 or mm < 1:
        return [0]

    return findPosibleSum(ss, [], 0)


# A, F, M = [3,2,4,3], 2, 4
# print(f'solution of {A}, given F = {F} and M = {M} is: {solution(A, F, M)}')

# A, F, M = [1, 3,2,4], 4, 6
# print(f'solution of {A}, given F = {F} and M = {M} is: {solution(A, F, M)}')

# A, F, M = [1, 3, 2, 4], 4, 6
# print(f'solution of {A}, given F = {F} and M = {M} is: {solution(A, F, M)}')

def generateTests(N):
    import random
    A = []
    for _ in range(N):
        A.append(random.randint(1, 6))
    F = random.randint(1, N-1)
    M = random.randint(2, 5)
    return A[:F], N-F, M

A, F, M = [5], 1, 5
sol = solution(A, F, M)
print(f'solution of {A}, given F = {F} and M = {M} is: {sol}, valide = {sum(A+sol)/(len(A)+F)}')

A, F, M = generateTests(10)
sol = solution(A, F, M)
print(f'solution of {A}, given F = {F} and M = {M} is: {sol}, valide = {sum(A+sol)/(len(A)+F)}')

A, F, M = generateTests(31)
sol = solution(A, F, M)
print(f'solution of {A}, given F = {F} and M = {M} is: {sol}, valide = {sum(A+sol)/(len(A)+F)}')