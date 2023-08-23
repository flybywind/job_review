package pat.observer

import scala.collection.mutable.ArrayBuffer
import pat.observer.Observer
import pat.observer.{Animal, Lion, Monkey}

import scala.concurrent.Future
import scala.concurrent.ExecutionContext.Implicits.global
import scala.util.Random

object ZooObserver:
  val observer = new AnimalObserver()
  var zoo = ArrayBuffer[Animal]()
  private def RegisterAnimal =
    for i <- 0 to 10 do
      val lion = new Lion(i*2 + 1, 1000, 200)
      lion.attach(observer)
      zoo.append(lion)

      val monkey = new Monkey(i*2 + 2, 200, 50)
      monkey.attach(observer)
      zoo.append(monkey)

  private def UpdateAnimal =
    val rand = Random(123)
    while true do
      val a = zoo(rand.nextInt(zoo.size))
      a.move
      Thread.sleep(100)

  @main def main(): Unit = {
    RegisterAnimal
    UpdateAnimal
  }







