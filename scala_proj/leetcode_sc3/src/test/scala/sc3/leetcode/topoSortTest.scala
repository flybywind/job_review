package sc3.leetcode

import sc3.leetcode.topoSort
import org.scalatest.flatspec.AnyFlatSpec


class topoSortTest extends AnyFlatSpec {
  it should "return empty for cycle dep" in {
    var adjList = List[List[Int]](List(1, 0), List(0, 1))
    var tops = new topoSort(2, adjList)
    assert("[]" == List(tops.getOrder).mkString(", "))

    adjList = List[List[Int]](List(0, 1), List(0, 2), List(0, 3), List(1, 4), List(4, 5), List(2, 6), List(3, 6), List(5, 0))
    tops = new topoSort(7, adjList)
    assert("[]" == List(tops.getOrder).mkString(", "))
  }

}

class topoSortTest2 extends AnyFlatSpec {
  it should "happy path for nonempty adj" in {
    var adjList = List[List[Int]](List(0, 1), List(0, 2), List(0, 3), List(1, 4), List(4, 5), List(2, 6), List(3, 6))
    var tops = new topoSort(7, adjList)
    assert("[5, 4, 1, 6, 2, 3, 0]" == List(tops.getOrder).mkString(", "))
  }
}