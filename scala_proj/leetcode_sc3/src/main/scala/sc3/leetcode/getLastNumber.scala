package sc3.leetcode

import sc3.leetcode.getLastNumber.Direction.{Back, Front}

object getLastNumber {

  enum Direction:
    def next = this match
      case Front => Back
      case Back => Front

    case Front
    case Back

  def solution(n: Int) =
    1

  def solRecur(n: Int, m: Int, dir: Direction): Int =
    if n == 1 then
      m
    else
      dir match
        case Front =>
          solRecur(n/2, m*2, dir.next)
//          n%2 == 0 match
//            case true => //even
//              solRecur(n/2, m*2)
//            case false =>
//              solRecur()
        case Back =>
          solRecur()



}
