package sc3.leetcode

object getLastNumber {

  private enum Direction(val v: Int):
    def next = this match
      case Front => Back
      case Back => Front
    case Front extends Direction(1)
    case Back extends Direction(-1)

  def solution(n: Int) =
    if n == 1 then 1 else
    solRecur(n, 2, 2, Direction.Front)

  private  def solRecur(n: Int, firstRem: Int, step:Int, dir: Direction): Int =
    if n <= 3 then
      firstRem
    else
      solRecur(n/2, firstRem+dir.v*(step*(n/2 - 2)), step*2, dir.next)
}
