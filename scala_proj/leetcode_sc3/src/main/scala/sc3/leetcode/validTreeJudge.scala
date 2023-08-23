package sc3.leetcode

import scala.util.boundary, boundary.break

class UnionSet(n: Int):
  private val parent = 0.until(n).toArray
  private val height = Array.ofDim[Int](n)

  def find(n: Int): Int =
    if parent(n) != n then
      val p = find(parent(n))
      if parent(n) != p then
        parent(n) = p
      p
    else
      parent(n)

  def union(p: Int, q: Int) =
    val r = if height(q) > height(p) then q else p
    height(r) += 1
    parent(p) = r
    parent(q) = r

object validTreeJudge {
  def validTree(n: Int, edges: Array[Array[Int]]): Boolean =
    if n-1 != edges.size then
      false
    else
      val uset = UnionSet(n)
      boundary:
        for e <- edges do
          val p1 = uset.find(e(0))
          val p2 = uset.find(e(1))
          if p1 != p2 then
            uset.union(p1, p2)
          else
            break(false)
        true
}
