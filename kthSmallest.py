class Solution:
    def kthSmallest(self,arr, l, r, k):
        '''
        arr : given array
        l : starting index of the array i.e 0
        r : ending index of the array i.e size-1
        k : find kth smallest element and return using this function
        '''
        if r-l+1 <= 1:
            return arr[l]
        if k == r-l+1:
            # find max
            maxv = arr[l]
            for i in range(l+1, r+1):
                maxv = max(maxv, arr[i])
            return maxv
        if k == 1:
            # find min
            minv = arr[l]
            for i in range(l+1, r+1):
                minv = min(minv, arr[i])
            return minv

            
        mid = (l+r+1)//2
        arr[l], arr[mid] = arr[mid], arr[l]
        mv = arr[l]
        i, j = l+1, r
        while i < j:
            while i < j and arr[i] < mv:
                i += 1
            while i < j and arr[j] >= mv:
                j -= 1
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        if arr[i] < mv:
            arr[l], arr[i] = arr[i], arr[l]
        if i-l >= k:
            return self.kthSmallest(arr, l, i-1, k)
        else:
            return self.kthSmallest(arr, i, r, k-(i-l))
        

if __name__ == "__main__":
    sol = Solution()

    arr = [7, 10, 4 ,3, 20, 15]
    print(f"sol of arr: {arr} = {sol.kthSmallest(arr, 0, len(arr)-1, 3)}")

    arr = [1, 2, 7, 10, 4, 3, 20, 15] # [ 1, 2, 3, 4, 7, 10, 15, 20]
    print(f"sol of arr: {arr} = {sol.kthSmallest(arr, 0, len(arr)-1, 2)}")
    
    arr = [1, 2, 7, 10, 4, 3, 20, 15] # [ 1, 2, 3, 4, 7, 10, 15, 20]
    print(f"sol of arr: {arr} = {sol.kthSmallest(arr, 0, len(arr)-1, 7)}")

    arr = [76, 61, 990, 782, 594, 365, 605, 727]
    print(f"sol of arr: {arr} = {sol.kthSmallest(arr, 0, len(arr)-1, 2)}")