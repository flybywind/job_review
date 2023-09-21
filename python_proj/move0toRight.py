from typing import List


def solution(arr: List[int]) -> List[int]:
    # Write your code here
    def _div_concur_iter(left, right: int) -> int:
        if right - left < 2:
            if arr[left] == 0:
                return left
            return right
        mid = (left+right)//2
        leftLastNz = _div_concur_iter(left, mid)
        rightLastNz = _div_concur_iter(mid, right)
        rn = rightLastNz - mid  # none-zero in right
        ln = leftLastNz - left  # none-zero in left
        if leftLastNz < mid:
            arr[(leftLastNz):(leftLastNz+rn)] = arr[mid:rightLastNz]
            for i in range(leftLastNz+rn, rightLastNz):
                arr[i] = 0

        return left + rn + ln

    if len(arr) == 0:
        return arr
    _div_concur_iter(0, len(arr))
    return arr
