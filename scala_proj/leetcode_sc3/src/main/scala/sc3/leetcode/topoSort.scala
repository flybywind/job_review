package sc3.leetcode

import java.util
import scala.collection.mutable
class topoSort(nodeNum:Int, adjList:List[List[Int]]):
  private val ingreeMap = Array.ofDim[Int](nodeNum)
  private val childrenMap = 0.until(nodeNum).map(x=>List[Int]()).toBuffer

  for (lst <- adjList) {
    ingreeMap(lst(0)) += 1
    childrenMap(lst(1)) = childrenMap(lst(1)) :+ lst(0)
  }
  private def dfs(ret:util.ArrayList[Int], node: Int) : Unit = {
    ret.add(node)
    for (ch <- childrenMap(node)) {
      ingreeMap(ch) -= 1
      if ingreeMap(ch) == 0 then
        dfs(ret, ch)
    }
  }
  def getOrder = {
    val starts = ingreeMap.zipWithIndex.filter(_._1 == 0).map(_._2)
    val ret = util.ArrayList[Int]()
    for (node <- starts) {
      dfs(ret, node)
    }
    if ret.size == nodeNum then ret else util.ArrayList[Int]()
  }



