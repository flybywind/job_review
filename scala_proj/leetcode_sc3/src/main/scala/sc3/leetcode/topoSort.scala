package sc3.leetcode

import java.util
import scala.collection.mutable
class topoSort(nodeNum:Int, adjList:List[List[Int]]):
  private val ingreeMap = mutable.Map[Int, Int]() ++ (0.until(nodeNum).map(x => (x, 0)).toMap)
  private val childrenMap = mutable.Map[Int, List[Int]]().withDefault(_=>List())

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
    val starts = ingreeMap.filter(kv => kv._2 == 0).keys
    val ret = util.ArrayList[Int]()
    for (node <- starts) {
      dfs(ret, node)
    }
    if ret.size == nodeNum then ret else util.ArrayList[Int]()
  }



