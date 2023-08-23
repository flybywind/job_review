package pat.observer

import org.scalatest.flatspec.AnyFlatSpec

class MonkeyTest extends AnyFlatSpec {
  it should "update weight and height" in {
    val monkey = new Monkey(1, 100f, 20f)
    println(f"weight0 = ${monkey.weight}")
    monkey.move
    println(f"weight1 = ${monkey.weight}")
    assertResult(101f) { monkey.weight }
    assertResult(21f) { monkey.height }
    println(f"weight2 = ${monkey.weight}")
    monkey.move
    println(f"weight3 = ${monkey.weight}")
    assertResult(102f) {monkey.weight}
    assertResult(22f) { monkey.height}
  }

}

class LionTest extends AnyFlatSpec {
  it should "update weight and height" in {
    val lion = new Lion(1, 100f, 20f)
    lion.move
    assertResult(101f) { lion.weight }
    assertResult(21f) { lion.height }
    lion.move
    assertResult(102f) {lion.weight}
    assertResult(22f) { lion.height}
  }

}