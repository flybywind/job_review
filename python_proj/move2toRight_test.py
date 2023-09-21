from move0toRight import solution


class TestSuperpalindromesInRange:
    def testCase1(self):
        print(solution([1, 0, 1, 2, 5]))
        print(solution([1, 0, 1, 0, 2, 5]))
        print(solution([1, 0, 1, 0, 0, 2, 5]))
        print(solution([1, 0, 1, 0, 0, 2, 5, 0]))
        print(solution([0, 1, 1, 0, 1, 0, 0, 2, 5, 0]))
        print(solution([]))

    # def testCase2(self):
        # print(solution([1, 1, 2, 5]))

    # def testCase3(self):
    #     print(solution([1, 1, 2, 5]))
