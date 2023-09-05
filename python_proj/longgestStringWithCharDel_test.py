import pytest

from longgestStringWithCharDel import Solution


@pytest.fixture
def sol():
    return Solution()


class TestLonggestStringWithCharDel:

    def testCase1(self, sol):
        s = "abpcplea"
        dictionary = ["ale", "apple", "monkey", "plea"]
        assert 'apple' == sol.findLongestWord(s, dictionary)

        s = "abpcplea"
        dictionary = ["a", "b", "c"]
        assert 'a' == sol.findLongestWord(s, dictionary)

    def testCase2(self, sol):
        s = "abpcplea"
        dictionary = ["ale", "abppea", "appea", "apple", "monkey", "plea"]
        assert 'abppea' == sol.findLongestWord(s, dictionary)

        s = "abpcplea"
        dictionary = ["ale", "abppea", "appea",
                      "apple", "monkey", "plea", "bpcplea"]
        assert 'bpcplea' == sol.findLongestWord(s, dictionary)

    def testCase3(self, sol):
        s = "aaa"
        dictionary = ["aaa", "aa", "a"]
        assert 'aaa' == sol.findLongestWord(s, dictionary)
