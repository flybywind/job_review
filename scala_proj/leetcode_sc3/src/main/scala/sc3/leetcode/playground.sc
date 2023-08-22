import scala.collection.mutable
val mm = mutable.Map[Int, Int]().withDefaultValue(0)
0.until(5).foreach(x=>mm(x)+=1)
val lst = List[Int]()
val l2 = 0::lst
print(lst, l2)

var seq = mutable.Seq[Int]()

seq = seq :++ List(9)

for (s <- seq) {
  println(s)
}

val zeroa = new Array[Int](10)
zeroa.size
zeroa(1) = 19
zeroa