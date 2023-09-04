from heapq import * 
from typing import List

class Height:
    def __init__(self, h, pos) -> None:
        self.h = h
        self.pos = pos
    def __lt__(self, other) -> bool:
        return self.h > other.h 
    def __repr__(self) -> str:
        return f"height = {self.h}, pos = {self.pos}"
    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        hh = [Height(v, i) for i, v in enumerate(height)]
        heapify(hh)

        h1 = heappop(hh)
        h2 = heappop(hh)
        wx = abs(h1.pos - h2.pos)

        res = h2.h * wx
        # print(f"heap: pop {h1}")
        # print(f"heap: pop {h2}, area = {res}")
        while len(hh) > 0:
            h3 = heappop(hh)
            w1, w2 = abs(h3.pos - h1.pos), abs(h3.pos - h2.pos)
            width = max(w1, w2)
            if width < wx:
                continue
            
            if w1 > w2:
                h2 = h3
            else:
                h1 = h3
            wx = width
            area = width * h3.h 
            if area > res:
                # print(f"heap: pop {h3}, area = {area}")
                res = area

        return res
    

def bruteForceSol(height: List[int]) -> int:
    res = 0
    for i, h in enumerate(height):
        for j in range(i+1, len(height)):
            area = min(h, height[j]) * (j-i)
            if area > res:
                # print(f"[{i},{j}] height: {height[i], height[j]}, area = {area}")
                res = area 
    return res 


sol = Solution()
height = [6800, 6424, 2091, 5063, 4042, 6977, 2844, 2875, 4236, 7855, 9510, 3968, 3535, 5337, 9860, 2210, 4492, 8391, 1613, 6918, 8100, 4202, 1162, 7411, 339, 6, 5049, 9884, 6417, 4561, 3057, 1599, 3482, 6128]
bf = bruteForceSol(height)
print(f"max area for {height} = {bf}, correct ? {sol.maxArea(height)==bf}")

height = [1,8,6,2,5,4,8,3,7]
bf = bruteForceSol(height)
print(f"max area for {height} = {bf}, correct ? {sol.maxArea(height)==bf}")

from random import randint
for i in range(100):
    N = randint(2, 100)
    heigh = [randint(0, 10000) for _ in range(N)]
    bf = bruteForceSol(heigh)
    # print(f"max area for {heigh} = {bf}, correct ? {sol.maxArea(heigh)==bf}")
    print(f"correct ? {sol.maxArea(heigh)==bf}")

    

