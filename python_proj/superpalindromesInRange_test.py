from superpalindromesInRange import Solution


class TestSuperpalindromesInRange:
    def testCase1(self):
        sol = Solution()
        assert 4 == sol.superpalindromesInRange('4', '1000')

    def testCase2(self):
        sol = Solution()
        assert 2 == sol.superpalindromesInRange(
            '40000000000000000', '50000000000000000')

    def testCase3(self):
        sol = Solution()
        assert 4 == sol.superpalindromesInRange(
            '1', '213')

    def testCase4(self):
        sol = Solution()
        sol.supperpalindromes10000(398904669, 13479046850)
        assert 6 == sol.superpalindromesInRange('398904669', '13479046850')
