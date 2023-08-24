import scala.collection.mutable
import scala.collection.mutable.ArrayBuffer
import mutable.Stack
import mutable.Queue
import scala.concurrent.{Await, Future}
import concurrent.ExecutionContext.Implicits.global
import scala.concurrent.duration.{Duration, SECONDS}
//import scala.collection.mutable
//val mm = mutable.Map[Int, Int]().withDefaultValue(0)
//0.until(5).foreach(x=>mm(x)+=1)
//val lst = List[Int]()
//val l2 = 0::lst
//print(lst, l2)
//
//var seq = mutable.Seq[Int]()
//
//seq = seq :++ List(9)
//
//for (s <- seq) {
//  println(s)
//}
//
//val zeroa = new Array[Int](10)
//zeroa.size
//zeroa(1) = 19
//zeroa

//case class NodeEff(i:Int, j: Int, effort: Int)
//
//val n = Array[NodeEff](
//  NodeEff(0, 0, 1),
//  NodeEff(0, 1, 2),
//  NodeEff(1, 3, 0),
//  NodeEff(2, 2, 4)
//)
//n.sortBy(-_.j)
var ll = 0::1::3::Nil

while ll.nonEmpty do
  ll match
    case head::tail =>
      println(f"$head $tail")
      ll = tail
    case Nil => println("end")

val buf = ArrayBuffer[Int](1,2,3,4,5)
buf.append(8)
buf

val q = mutable.Queue[Int](0,1,2,3,4,5,6)
q.append(9)
q
q.dequeue()
q

val stk = mutable.Stack[Int](1, 2, 3,4,8)
stk.push(9)
stk
stk.pop()
stk.pop()
stk

//buf.slice(0, 4) = buf.slice(1, 5)
val fut = Future{"hello future"}
//fut.onComplete()
Await.result(fut, Duration(1, SECONDS))