package sc3.leetcode

object playinherit {
  type Address = String

  abstract class Person(var address: Address, var name: String) {
    def mock: String

    override def toString = if (address == null) name else s"$name @ $address"
  }

  class Employee(_address: Address, _name: String,  var age: Int)
    extends Person(_address, _name) {
    // rest of the class
    override def mock: String = f"$address _mock"
  }

  @main def main()=
    val e = new Employee("john", "axxx", 24)
    println(e)
    println(e.age)
}
