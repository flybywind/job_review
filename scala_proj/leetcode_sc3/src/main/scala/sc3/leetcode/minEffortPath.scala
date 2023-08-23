package sc3.leetcode

import org.w3c.dom.traversal.NodeFilter

import scala.collection.mutable

// https://leetcode.cn/problems/path-with-minimum-effort/description/
object minEffortPath {
  private case class NodeEff(loc:(Int, Int), effort: Int)

  private def orderNode(x:NodeEff) = -x.effort
  def minEffortPath(heights: Array[Array[Int]]): Int =
    var visited = Set[(Int, Int)]()
    val rowNum = heights.size
    val colNum = heights(0).size

    var nodeeff = NodeEff((0, 0), 0)
    val heap = new mutable.PriorityQueue[NodeEff]()(Ordering.by(orderNode))
    heap.enqueue(nodeeff)
    var minEff = Int.MaxValue
    while heap.nonEmpty do
      val head = heap.dequeue()
      val (i, j) = head.loc
      if i+1==rowNum && j+1==colNum then
        if minEff > head.effort then
          minEff = head.effort
      else
        visited = visited + head.loc
        for d <- Array((1, 0), (-1, 0), (0, 1), (0, -1)) do
          val (i2, j2) = (d._1+i, d._2+j)
          if (i2 >= 0 && i2 < rowNum) &&
            (j2 >= 0 && j2 < colNum) && !visited((i2, j2)) then
            nodeeff = NodeEff((i2, j2), math.max(head.effort, math.abs(heights(i)(j) - heights(i2)(j2))))
            heap.enqueue(nodeeff)

    minEff


}
