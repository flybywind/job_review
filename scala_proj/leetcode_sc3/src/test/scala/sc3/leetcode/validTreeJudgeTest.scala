package sc3.leetcode

import org.scalatest.flatspec.AnyFlatSpec

class validTreeJudgeTest extends AnyFlatSpec {

  behavior of "validTreeJudgeTest"
  it should "invalidTree for disconnected nodes" in {
    assertResult(false) {
      validTreeJudge.validTree(4, Array[Array[Int]](
        Array[Int](2, 3),
        Array[Int](1, 0)
      ))
    }
    assertResult(false) {
      validTreeJudge.validTree(4, Array[Array[Int]](
        Array[Int](2, 3),
        Array[Int](1, 3),
        Array[Int](1, 2)
      ))
    }
  }
  it should "invalidTree for cycle nodes" in {
    assertResult(false) {
      validTreeJudge.validTree(4, Array[Array[Int]](
        Array[Int](0, 1),
        Array[Int](1, 3),
        Array[Int](2, 3),
        Array[Int](1, 4),
        Array[Int](1, 2)
      ))
    }
  }
  it should "happy returen" in {
    assertResult(true) {
      validTreeJudge.validTree(5, Array[Array[Int]](
        Array[Int](0, 1),
        Array[Int](0, 3),
        Array[Int](1, 4),
        Array[Int](0, 2)
      ))
    }
  }
}