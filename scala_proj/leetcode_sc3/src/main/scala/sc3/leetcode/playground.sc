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

type Address = String

abstract class Person (var name: String, var address: Address) {
  def mock:String
  override def toString = if (address == null) name else s"$name @ $address"
}
class Employee (name: String, address: Address, var age: Int)
  extends Person (name, address) {
  // rest of the class
  override def mock: String = f"$address _mock"
}

val e = new Employee("john", "axxx", 24)
e.name = "xxx"
print(e, e.name)
