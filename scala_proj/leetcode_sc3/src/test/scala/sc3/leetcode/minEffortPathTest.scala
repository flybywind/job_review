package sc3.leetcode

import org.scalatest.flatspec.AnyFlatSpec
import minEffortPath.minimumEffortPath
class minEffortPathTest extends AnyFlatSpec {

  behavior of "minEffortPathTest"

  it should "minEffortPath" in {
    assertResult(1) {
      minimumEffortPath(Array[Array[Int]](
        Array[Int](1,2,3),
        Array[Int](3,8,4),
        Array[Int](5,3,5)
      ))
    }

    assertResult(2) {
      minimumEffortPath(Array[Array[Int]](
        Array[Int](1, 2, 2),
        Array[Int](3, 8, 2),
        Array[Int](5, 3, 5)
      ))
    }

    assertResult(0) {
      minimumEffortPath(Array[Array[Int]](
        Array[Int](1,2,1,1,1),
        Array[Int](1,2,1,2,1),
        Array[Int](1,2,1,2,1),
        Array[Int](1,2,1,2,1),
        Array[Int](1,1,1,2,1)
      ))
    }
  }

}
