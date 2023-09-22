from typing import List


class Solution:
    def isStackPermutation(self, N: int, A: List[int], B: List[int]) -> int:
        # code here
        stack = []
        i, j = 0, 0
        while i < N:
            if len(stack) > 0 and stack[-1] == B[j]:
                stack.pop()
                j += 1
            else:
                stack.append(A[i])
                i += 1
        while len(stack) > 0:
            if stack[-1] == B[j]:
                stack.pop()
                j += 1
            else:
                return 0
        return 1


sol = Solution()

A = [1]
B = [1]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')
A = [1, 2]
B = [2, 1]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')

A = [1, 2]
B = [1, 2]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')
A = [1, 2, 3]
B = [2, 1, 3]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')

A = [1, 2, 3]
B = [3, 1, 2]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')

A = [1, 2, 3]
B = [3, 2, 1]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')

A = [1, 2, 3, 4]
B = [3, 2, 4, 1]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')

A = [1, 2, 3, 4]
B = [3, 4, 1, 2]
print(f"B: {B}", "is" if sol.isStackPermutation(len(A), A, B)
      else "isn't", f'stack permutation of A: {A}')
