import sys

class Solution:
    # @param ratings, a list of integer
    # @return an integer
    def candy(self, ratings):
        N = len(ratings)
        candy_list = [1 for i in xrange(N)]
        min_candy = 0
        cur = 0
        while cur + 1 < N:
            next = cur+1
            if ratings[cur] < ratings[next]:
                candy_list[cur] += min_candy
                min_candy += 1
            elif ratings[cur] == ratings[next]:
                candy_list[cur] += min_candy
                min_candy = 0
            else:
                s = cur
                min_candy2 = 0
                while next < N and ratings[s] >= ratings[next]:
                    next += 1
                    s += 1
                    if next == N or ratings[s] != ratings[next]:
                        min_candy2 += 1
                candy_list[cur] += max(min_candy, min_candy2)
                min_candy2 -= 1
                for i in xrange(cur + 1, next):
                    if ratings[i] == ratings[i-1] and \
                        (i + 1 == next or ratings[i] == ratings[i+1]):
                        candy_list[i] = 1
                    else:
                        candy_list[i] += max(0, min_candy2)
                        min_candy2 -= 1
                min_candy = 1
            cur = next
        if cur < N and ratings[cur - 1] < ratings[cur]:
            candy_list[cur] = candy_list[cur - 1]+1

        sum = 0
        for cn in candy_list:
            sum += cn
        return sum, candy_list


s = Solution()
rating = [2,4,3,3,3,3,2,3,4,5,3,2,1]
sum, candy_list = s.candy(rating)

print "rating:", rating
print "candy: ", candy_list
print "sum of candy:", sum