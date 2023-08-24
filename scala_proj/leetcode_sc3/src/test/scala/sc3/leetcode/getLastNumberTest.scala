package sc3.leetcode

import org.scalatest.flatspec.AnyFlatSpec

class getLastNumberTest extends AnyFlatSpec {

  behavior of "getLastNumberTest"

  ignore should "solution 123" in {
    assert(1==getLastNumber.solution(1))
    assert(2==getLastNumber.solution(2))
    assert(2==getLastNumber.solution(3))
  }
  it should "solution 4,8,9,13,14" in {
    assert(2 == getLastNumber.solution(4)) // 1 2 3 4
    assert(6 == getLastNumber.solution(8)) // 1 2 3 4 5 6 7 8 ==> 2 4 6 8 ==> 6
    assert(6 == getLastNumber.solution(9)) // 1 2 3 4 5 6 7 8 9 ==> 2 4 6 8 ==> 6
    assert(6 == getLastNumber.solution(13))
    assert(8 == getLastNumber.solution(14))
  }
}
